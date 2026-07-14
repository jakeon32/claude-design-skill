---
name: qa-pipeline
description: "Claude Design QA 파이프라인 — 슬라이드 생성 후 자동 검증 → 검증된 레이아웃 카탈로그 구축. visual-refiner가 실행하는 자동 루프 정의."
---

# QA Pipeline

## 목적

슬라이드 생성 직후 품질을 자동으로 검증하고, 통과한 레이아웃을 **검증 완료 카탈로그**에 기록한다.
카탈로그가 쌓이면 새 프로젝트에서 "검증된 레이아웃"을 참조해 초안 품질을 처음부터 높게 유지할 수 있다.

> **순서 원칙**: B(자동 QA 루프)가 먼저 작동해야 A(검증된 샘플 카탈로그)가 만들어진다.

---

## QA 루프 전체 흐름

```
[0. 예산 검증]  ★ 2026-07-14 신설 — HTML 생성 *전*
  density-rules.md §2·§3 으로 줄 예산 / 글자수 계산
  → 넘칠 게 확정이면 HTML 을 만들지 말고 먼저 쪼갠다
  → "오버플로의 90%는 여기서 죽는다"
        ↓
[1. 생성]
  slide-deck-agent → HTML 슬라이드 파일 (d:\tmp\slides.html)
        ↓
[1.5 slide-lint]  ★ 2026-07-14 신설 — 기계 게이트. 실패 시 exit 1
  node tools/slide_lint.js <deck.html>
  ① 넘침(scrollHeight)  ② 안전영역 이탈(getBoundingClientRect)
  ③ 폰트 하한(D1 32 / D2 24 / D3 16)  ④ 제목 2줄 초과  ⑤ 차트 정크
  → 실패하면 스크린샷 찍지 말고 여기서 멈춘다 (사람 눈보다 기계가 먼저)
        ↓
[2. 스크린샷]
  Chrome DevTools / puppeteer → 각 슬라이드 PNG
        ↓
[3. 코드 분석 QA]           ← visual-refiner 1단계
  HTML 파일 직접 파싱
  → 타이포 스케일, 스페이싱, 금지 폰트, PPTX 제약 등
        ↓
[3.7 ★ codex 시각 검수]     ← 2026-07-14 신설. 제3자 눈.
  codex exec -i slide.png -- "시니어 디자이너 관점에서 시각 검수하라 …"
  → Claude가 놓치는 시각 문제를 잡는다 (실측: 8건 중 3건을 Claude가 못 봤음)
        ↓
[4. 시각 검사 QA]            ← visual-refiner 2단계
  스크린샷 이미지를 Claude가 직접 보고 판단
  → 가독성, 크리핑, 레이아웃 붕괴, Hero 명확성, 여백, 대비, 스타일 정체성
        ↓
[5. 결과 분류]
  ❌ 0개 + ⚠️ 0개 → [6. 카탈로그 기록] 진행
  ❌ 1~2개         → [5a. 자동 수정] → 재스크린샷 → 3단계로 복귀
  ❌ 3개 이상      → [5b. 레이아웃 재설계] → 1단계로 복귀
        ↓
[6. 카탈로그 기록]
  레이아웃 유형 + 스타일 + 스크린샷 경로 + 검증 날짜 기록
  → verified-layouts.md 업데이트
```

---

## 🔴 0·1.5 단계 — 넘침은 빌드 실패다

**2026-07-14 이전, 모든 `.slide` 에 `overflow:hidden` 이 걸려 있었다.**
내용이 넘치면 **에러도 경고도 없이 그냥 잘려 나갔다.** 무증상 정보 손실이었고,
사람이 스크린샷을 눈으로 보기 전엔 아무도 몰랐다.

**규격은 문서가 아니라 코드에 둔다.**

```bash
# 빌드 게이트 — 넘치면 exit 1
node plugins/claude-design/skills/claude-design/tools/slide_lint.js d:/tmp/slides.html
```

**린터가 잡는 것**

| 검사 | 방법 | 왜 |
|---|---|---|
| 세로·가로 넘침 | `scrollHeight > clientHeight` | 잘림 = 정보 손실 |
| 안전영역 이탈 | `getBoundingClientRect()` | **absolute·음수마진·transform 은 scrollHeight 로 안 잡힌다** — 반드시 병행 |
| 폰트 하한 | `getComputedStyle` vs 밀도 등급 | **폰트를 줄여 넘침을 "해결"한 흔적 적발** |
| 제목 3줄 | 높이 / line-height | Action Title 2줄 초과 = 하드 실패 |
| 차트 정크 | box-shadow / gradient | 3D·그림자·그라디언트 금지 |

**실패 시 대응 — 자동으로 폰트를 줄이지 않는다.**
```
삭제 → 분할 → 부록 → 열/등급 → 폰트(1단계) → 실패
```
(→ [`density-rules.md` §5`](density-rules.md) 결정 트리)

> **puppeteer 없으면** `puppeteer-core` + 시스템 Chrome 으로 자동 폴백한다.
> 실행: `NODE_PATH=<puppeteer-core 있는 node_modules> node tools/slide_lint.js <deck.html>`

---

## 🔴 3.7 단계 — codex 시각 검수 (제3자 눈)

**기계는 수치를, codex는 시각을, 사람은 맥락을 본다.**

```bash
codex exec --skip-git-repo-check -i slide-01.png -- \
  "이 1280x720 슬라이드를 시니어 디자이너 관점에서 시각 검수하라.
   여백 균형, 시각 위계, 그룹핑, 정렬, 타이포, 강조 분산을 본다.
   칭찬 말고 고칠 것만 우선순위 순으로. 각 항목 (무엇/왜/어떻게) 한 줄씩. 한국어."
```

**왜 필요한가 — 실측 결과 (2026-07-14)**
검증 덱 슬라이드 1장에 대해 codex가 8건을 지적했고, **그중 3건은 Claude가 전혀 못 봤다**:
- 우측 결론 블록이 리스트와 너무 멀어 관계가 약해 보임
- 제목이 한 줄로 과도하게 퍼져 하단 콘텐츠보다 시각 무게가 압도적
- **문장 끝 "것이다."가 한 줄로 고립돼 의도치 않은 강조가 됨**

**주의: codex도 100%는 아니다.**
같은 검수에서 "제목에 파란 그림자가 있다"고 했는데 그림자는 없었다.
**그대로 받아들이지 말고 검증할 것.** 지적을 코드로 확인한 뒤 반영한다.

**운영 규칙**
- 이미지는 **1장씩** 보낸다 (4장 동시 전달 시 7분 타임아웃 발생)
- 타임아웃 280초 권장
- **칭찬 금지·우선순위 요구**를 프롬프트에 명시해야 실용적인 답이 나온다

---

## 단계별 상세

### 1단계: 생성

`slide-deck-agent`가 검증 대상 슬라이드를 생성한다.

**샘플 작업 시**: 모든 레이아웃 유형을 체계적으로 커버하기 위해 아래 순서로 작업한다:

```
우선순위 1 (핵심): Cover, Photo Split, Centered Statement, Feature Cards 3-col, Section Title
우선순위 2 (콘텐츠): Simple List, 2×2 Grid, 3-Column Text, Highlight, Numbered List
우선순위 3 (데이터): Bar/Column Chart, Line Chart, Funnel, Timeline, Venn
우선순위 4 (비주얼): Full Bleed Photo, 2/3-Col Image+Caption, Quote
우선순위 5 (특수): Mobile Mockup, Desktop Mockup, Team Grid, Closing/CTA
```

각 레이아웃을 **2~3개 스타일 조합**으로 검증한다:
- 라이트 스타일 1개 (예: corporate-trust, minimal-editorial)
- 다크 스타일 1개 (예: dark-editorial, cyberpunk)
- 브랜드 기반 1개 (사용자 색상 주입)

### 2단계: 스크린샷

```bash
# Chrome DevTools MCP 사용 시
mcp__chrome-devtools__new_page("file:///d:/tmp/slides.html")
mcp__chrome-devtools__take_screenshot()

# 또는 capture_compare.py
python tools/capture_compare.py
# → d:\tmp\captures\slide_01.png, slide_02.png ...
```

### 3단계: 코드 분석 QA

`visual-refiner.md` §1단계 체크리스트 실행 (HTML 파일 직접 읽기):

| 항목 | 기준 |
|------|------|
| 타이포 스케일 | h1→h2→h3 인접 비율 ≥ 1.2× |
| 스페이싱 | 모든 padding/gap/margin이 8px 배수 |
| 금지 폰트 | Inter/Roboto/Arial/Space Grotesk 없음 |
| [PPTX] gradient | linear/radial-gradient 0건 |
| [PPTX] `<p>` 래핑 | 텍스트 div/span 단독 사용 없음 |
| 본문 최소 폰트 | 16px 이상 |
| 제목 최소 폰트 | 40px 이상 |
| 스타일 예외 | 스타일별 Anti-slop 예외 적용 |

### 4단계: 시각 검사 QA

스크린샷 이미지를 직접 보고 판단:

| 항목 | 판단 기준 |
|------|---------|
| 가독성 | 썸네일(절반) 크기에서도 텍스트 읽힘 |
| 텍스트 크리핑 | 컨테이너 밖으로 텍스트 잘림 없음 |
| 레이아웃 붕괴 | 요소가 의도한 위치, 겹침 없음 |
| Hero 명확성 | 시선이 먼저 가는 요소 1개 명확 |
| 여백 분포 | 한쪽 방향 쏠림 없음, 전체 25%+ 여백 |
| 색상 대비 | 배경-텍스트 대비 육안 충분 (≥4.5:1) |
| 스타일 정체성 | 선택 스타일의 특징이 실제로 보임 |

**슬라이드 모드 가중치**: 스크롤 없는 단일 화면이므로 텍스트 크리핑·균형 기준을 웹보다 1단계 엄격하게 적용.

### 5단계: 결과 분류 및 수정

**[자동 수정 — ❌ 1~2개]**:

```
금지 폰트 감지 → font-family 교체
스페이싱 불일치 → 8px 배수로 반올림
타이포 비율 미달 → 인접 단계 크기 조정
텍스트 크리핑 → padding 증가 또는 폰트 축소
```

자동 수정 후 → 재스크린샷 → 3단계로 복귀.

**[재설계 권장 — ❌ 3개 이상]**:

```
레이아웃 유형 교체 또는 구조 재검토 → 1단계로 복귀
```

### 6단계: 카탈로그 기록

❌ 0개, ⚠️ 0개 시 `references/verified-layouts.md`에 기록:

```markdown
| 레이아웃 | 스타일 | 스크린샷 | 검증일 | 비고 |
|---------|--------|---------|--------|------|
| Photo Split | corporate-trust | captures/photosplit-corporate.png | 2026-04-25 | PPTX OK |
| Centered Statement | dark-editorial | captures/statement-dark.png | 2026-04-25 | — |
```

---

## 레이아웃 유형별 패스 기준

각 레이아웃 유형에 특화된 추가 기준:

| 레이아웃 유형 | 특화 기준 |
|-------------|---------|
| **Title/Cover** | 텍스트 요소 ≤ 2개, 이미지가 배경 역할만, 장식이 타이틀보다 눈에 띠지 않음 |
| **Photo Split** | 이미지-텍스트 경계가 자연스러움 (gradient blend 또는 solid 분리), Visual 60%+ |
| **Centered Statement** | 텍스트 1개가 확실한 Hero, 여백이 전체 40%+ |
| **Feature Cards** | 카드 높이 균등, 한 카드만 accent(Hero) 또는 모두 동등 중립 |
| **Data Chart** | 차트가 Visual 70%+, 설명 텍스트가 차트를 방해하지 않음 |
| **Simple List** | 리스트 항목 ≤ 4개, 각 항목 1줄 내외 |
| **Timeline** | 단계 ≤ 5개, 선형 흐름이 명확 |
| **Mobile Mockup** | 기기 비율 정확 (9:19.5 = iPhone), 기기 내 UI가 readable |
| **Full Bleed Photo** | z-index 3레이어 구조, 텍스트 대비 확보 |
| **Team Grid** | 멤버 ≤ 11명, 2행 균형, 이름+역할 readable |
| **Closing/CTA** | CTA 버튼/텍스트가 명확한 Hero, Visual 75%+ |

---

## 검증 완료 카탈로그 구조

`references/verified-layouts.md` 파일에 누적 기록:

```markdown
# Verified Layout Catalog

> 자동 QA 통과 = ❌ 0 + ⚠️ 0
> 이 카탈로그의 HTML 패턴을 새 프로젝트의 초안 기반으로 사용한다.

## Cover / Title
| 레이아웃 | 스타일 | 모드 | 스크린샷 경로 | 검증일 |
|---------|--------|------|-------------|--------|
| Title/Cover | corporate-trust | HTML | ... | YYYY-MM-DD |

## Text Layouts
...

## Visual / Photo
...

## Data / Chart
...

## Mockup
...
```

---

## 샘플 덱 구성 권장 (레이아웃 QA 전용)

레이아웃 검증 전용 샘플 덱 구성:

```
슬라이드 1  — Title/Cover (Pattern F — 톤온톤 아크)
슬라이드 2  — Section Title
슬라이드 3  — Centered Statement (숫자 강조)
슬라이드 4  — Photo Split (텍스트 좌 + 이미지 우)
슬라이드 5  — Simple List (H2 좌 + 3항목)
슬라이드 6  — 2×2 Grid
슬라이드 7  — 3-Column Text
슬라이드 8  — Feature Cards 3-col
슬라이드 9  — Bar Chart
슬라이드 10 — Timeline (4단계)
슬라이드 11 — Mobile Mockup (1)
슬라이드 12 — Full Bleed Photo
슬라이드 13 — Closing/CTA
```

→ 이 13장을 2개 스타일(라이트 + 다크)로 생성하면 26슬라이드 QA로 핵심 레이아웃 전체 검증 가능.

---

## 실행 체크리스트 (QA 수행 시)

```
□ HTML 파일 경로 확인 (d:\tmp\slides.html)
□ Chrome DevTools MCP 연결 확인
□ 스크린샷 저장 경로 확인 (d:\tmp\captures\)
□ 적용 스타일 확인 (스타일별 예외 적용 위해)
□ QA 결과를 verified-layouts.md에 기록
```
