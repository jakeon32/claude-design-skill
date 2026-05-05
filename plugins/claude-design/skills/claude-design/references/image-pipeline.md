# 이미지 파이프라인 (Image Pipeline)

슬라이드 덱(및 기타 모드)에서 **이미지 슬롯**을 식별·placeholder로 1차 완료한 뒤, **사용자 검토 후 이미지 패스**에서 한 장씩 채우는 워크플로의 단일 출처.

> 이 문서는 "어떻게 이미지를 채울지(파이프라인)"를 다룬다. "어떻게 사진을 슬라이드에 배치할지(레이아웃)"는 `photo-layouts.md`. 두 문서는 보완 관계.

---

## 1. 핵심 원칙

```
1) 이미지 단서는 자료에 이미 있다 — project-planner가 추출한다
2) 디자인이 먼저 — 이미지는 placeholder로 1차 완료 후 채운다
3) 한 장씩 컨펌 — 비용·결과 품질 양쪽을 사용자가 통제한다
4) placeholder 이름 = 파일 이름 — 매칭은 자동으로 된다
5) 다이어그램은 placeholder가 아니라 인라인 처리 — 1차 완료에 포함된다
```

**왜 1차 완료 후인가?** 디자인이 확정돼야 슬롯의 비율·위치·메시지·스타일이 명확해진다. 그 컨텍스트가 있어야 codex 프롬프트가 정확해지고 사용자 제공 이미지도 제대로 배치된다.

---

## 2. 이미지 슬롯 타입 (3분기)

각 슬롯은 다음 중 하나로 분류된다 — **타입에 따라 처리 경로가 다르다**.

| 타입 | 정의 | 처리 경로 |
|------|------|----------|
| **`photo`** (사진) | 실사 사진 — 풍경, 인물, 동물, 제품, 현미경/위성 사진 등 | placeholder → 이미지 패스 (codex AI 생성 또는 사용자 제공) |
| **`illust`** (일러스트) | 컨셉 그림 — 비유 일러스트, 카드/도식 표현, 캐릭터 일러스트 등 | placeholder → 이미지 패스 (codex AI 생성 또는 사용자 제공) |
| **`diagram`** (다이어그램·그래프·지도) | 데이터 차트, 공식 도식, 지도, 플로우, 표 시각화 | **인라인 HTML/CSS/SVG 생성** — placeholder 아님, 1차 완료에 포함 |

### 분류 기준

```
hint 텍스트 분석:
  "사진" / "현미경" / "지도(위성)" / "실사 풍경"     → photo
  "일러스트" / "도식" / "비유" / "캐릭터 그림"        → illust
  "그래프" / "분포" / "차트" / "공식" / "표" / "지도(데이터)" → diagram
  
복합 hint (예: "사진 + 분포 그래프 비교"):
  → 슬롯을 둘로 분리. 각각 photo + diagram으로.
```

**왜 다이어그램은 인라인인가?**
- 데이터(수치·관계)가 자료에 이미 있다 — codex보다 정확하다
- HTML/CSS/SVG는 픽셀이 아니라 코드 → 검수·수정·다국어 대응 모두 쉽다
- codex 가이드의 "PIL 우회" 사례와 같은 결정 — 텍스트·정확 데이터 위주는 코드 합성이 안전하다

---

## 3. 슬롯 ID 컨벤션

```
slot_{NN}_{sNN}_{type}_{hint_slug}

예시:
  slot_01_s01_photo_lake_cover
  slot_07_s08_illust_card_game
  slot_18_s20_photo_seal_cheetah
  slot_22_s28_diagram_florida_map  (인라인 처리되더라도 ID는 부여 — 디버깅용)
```

| 부분 | 의미 |
|------|------|
| `NN` | 이미지 패스 처리 순서 (전체 photo+illust 슬롯 통틀어 1부터) |
| `sNN` | 슬라이드 번호 (deck 내 위치) |
| `type` | `photo` / `illust` / `diagram` |
| `hint_slug` | 한글 hint를 영문 1~3 단어 슬러그로 압축 (검수·디버깅용) |

**slug 규칙**:
- 소문자, 하이픈 없이 underscore (예: `lake_cover`, `card_game`)
- 한글 음차가 아니라 의미 번역 (예: "낫 모양 적혈구" → `sickle_cell`)
- 단어 1~3개 이내. 길면 자르고 의미 핵심만

---

## 4. Placeholder 마크업 표준 (HTML)

### 4-1. photo / illust 슬롯 — placeholder 단계

```html
<div class="image-slot empty" 
     data-slot-id="slot_01_s01_photo_lake_cover"
     data-slot-type="photo"
     data-slot-hint="잔잔한 호수, 청록·녹색 톤"
     data-slot-ratio="16:9"
     data-slot-status="placeholder">
  <!-- placeholder 시각: 회색 그라디언트 + 라벨 -->
  <div class="image-slot__label">
    <span class="image-slot__icon">📷</span>
    <span class="image-slot__id">#01</span>
    <span class="image-slot__hint">잔잔한 호수, 청록·녹색 톤</span>
  </div>
</div>
```

**필수 data-* 속성**:

| 속성 | 값 | 용도 |
|------|---|------|
| `data-slot-id` | 컨벤션 슬롯 ID | 파일 매칭 키 |
| `data-slot-type` | `photo` / `illust` | 라우팅 |
| `data-slot-hint` | 자료에서 추출한 hint 원문 | codex 프롬프트 재료 |
| `data-slot-ratio` | `16:9` / `4:3` / `1:1` 등 | codex 비율 강제 + placeholder 박스 |
| `data-slot-status` | `placeholder` / `filled` / `skipped` | 패스 진행 추적 |

### 4-2. photo / illust 슬롯 — filled 단계

```html
<div class="image-slot filled"
     data-slot-id="slot_01_s01_photo_lake_cover"
     data-slot-type="photo"
     data-slot-status="filled"
     style="background-image: url('images/slot_01_s01_photo_lake_cover.png')">
</div>
```

배경 이미지로 채울지(`background-image`), `<img>` 태그로 채울지는 슬라이드 레이아웃에 따른다 (`photo-layouts.md` 참조).

### 4-3. diagram 슬롯 — 인라인 (placeholder 아님)

```html
<div class="image-slot inline-diagram"
     data-slot-id="slot_22_s07_diagram_genotype_dist"
     data-slot-type="diagram"
     data-slot-status="filled">
  <!-- 실제 SVG/CSS 차트가 여기 인라인으로 들어감 -->
  <svg viewBox="0 0 400 200">...</svg>
</div>
```

`data-slot-status`는 처음부터 `filled`. 이미지 패스에서 건너뛴다.

### 4-4. CSS 가이드 (placeholder 시각)

```css
.image-slot.empty {
  background: repeating-linear-gradient(
    45deg,
    color-mix(in srgb, var(--c-text) 5%, transparent),
    color-mix(in srgb, var(--c-text) 5%, transparent) 10px,
    color-mix(in srgb, var(--c-text) 8%, transparent) 10px,
    color-mix(in srgb, var(--c-text) 8%, transparent) 20px
  );
  border: 1px dashed color-mix(in srgb, var(--c-text) 30%, transparent);
  display: flex;
  align-items: center;
  justify-content: center;
  aspect-ratio: 16 / 9; /* data-slot-ratio 기반으로 동적 처리 */
}

.image-slot__label {
  text-align: center;
  font-size: 14px;
  color: color-mix(in srgb, var(--c-text) 70%, transparent);
  font-family: var(--font-mono, monospace);
}
```

**색상 토큰화 의무 준수** — `rgba` 금지, `color-mix` 사용 (memory: feedback_color_mix_obligation).

---

## 5. 저장 경로 컨벤션

```
outputs/
  {프로젝트명}/
    deck.html
    deck-color-tuner.html
    showcase.html
    images/                                    ← ✨ 이미지 패스 산출물
      slot_01_s01_photo_lake_cover.png
      slot_07_s08_illust_card_game.png
      ...
    images.manifest.json                       ← 슬롯 메타·진행 추적
```

`deck.html`에서 이미지 참조는 **상대 경로**: `images/{slot_id}.png`.

### 프로젝트명 결정

- **시점**: project-planner 단계
- **규칙**: 자료 파일명 슬러그 → 영문 케밥 케이스 (예: `유전자풀_40분발표_슬라이드구성안.md` → `gene-pool-deck`)
- 사용자가 명시한 이름이 있으면 그것 우선
- 메모리 룰 적용: 합리적 추론 가능하면 자동 결정 (`feedback_auto_decide`)

---

## 6. images.manifest.json 스키마

선택 산출물 — 슬롯별 진행 상태와 메타를 추적한다. 재개·검수·비용 분석에 사용.

```json
{
  "project": "gene-pool-deck",
  "created": "2026-05-05T10:23:00Z",
  "totals": {
    "slots_total": 29,
    "slots_filled": 18,
    "slots_placeholder": 11,
    "slots_skipped": 0,
    "tokens_used": 1234567,
    "estimated_cost_usd": 14.81
  },
  "slots": [
    {
      "id": "slot_01_s01_photo_lake_cover",
      "slide": 1,
      "type": "photo",
      "ratio": "16:9",
      "hint_original": "잔잔한 호수 사진 또는 DNA 이중나선과 다양한 동물 실루엣이 어우러진 일러스트, 청록·녹색 톤",
      "hint_normalized": "잔잔한 호수, 청록·녹색 톤",
      "status": "filled",
      "source": "codex",
      "tokens": 67200,
      "regenerated_count": 1,
      "created": "2026-05-05T10:24:30Z",
      "file": "images/slot_01_s01_photo_lake_cover.png"
    }
  ]
}
```

**status 값**:
- `placeholder` — 1차 완료 직후, 아직 미처리
- `filled` — 이미지 적용됨 (codex / user / inline)
- `skipped` — 사용자가 명시적으로 skip
- `pending` — 패스 진행 중 (재생성 등 대기 상태)

---

## 7. 이미지 패스 — 한 장씩 컨펌 흐름

### 7-1. 발동 시점

- **자동 트리거 X** — 핸드오프 시점에 placeholder가 있으면 메인이 사용자에게 옵션 제시
- 사용자가 "이미지 채워줘" / "image pass" / "패스 시작" 등으로 명시 응답 시 진입
- placeholder 0건이면 옵션 자체 표시 안 함

### 7-2. 진행 방식 선택 (한 번)

```
이미지 패스 시작 — 슬롯 29개 (사진 12 + 일러스트 17)

진행 방식:
  [1] 한 장씩 — 슬롯마다 결정·컨펌 (디폴트, 비용 통제 우선)
  [2] 일괄 사전 분류 + AI만 한 장씩 컨펌
  [3] 모두 직접 제공 (한 번에 경로 입력)
  
선택: > 1
```

### 7-3. 슬롯 단위 인터랙션 (한 장씩)

```
──────── #1 / 29 ────────
Slide 1 — Cover
hint: 잔잔한 호수, 청록·녹색 톤
타입: photo · 비율: 16:9

처리: [a] AI 생성  [b] 직접 제공  [c] skip
> a

▼ codex 프롬프트 미리보기:
  "잔잔한 호수, 청록·녹색 톤, 발표 커버 와이드 16:9.
   자연 사진, 평온한 분위기, 부드러운 빛.
   결과를 slot_01_s01_photo_lake_cover.png로 저장."
   
[Enter=실행] [e=수정] [s=skip]
> Enter

⏳ codex 호출 중... (예상 ~30초, ~65k tokens)
✓ 생성 완료. 미리보기 [이미지]

[Enter=OK 적용] [r=재생성] [s=skip] [q=패스 중단]
> Enter

✓ Slide 1 적용 → outputs/gene-pool-deck/images/slot_01_s01_photo_lake_cover.png
누적: 67k tokens / ~$0.81

──────── #2 / 29 ────────
...
```

### 7-4. 비용·품질 통제

| 컨트롤 | 동작 |
|--------|------|
| `q` (패스 중단) | 그 시점까지 처리한 슬롯만 적용. 나머지는 placeholder 유지. 다음 세션에서 재개 가능 |
| `r` (재생성) | 최대 2회. 3회째는 명시적 컨펌("계속할까요?") |
| `e` (프롬프트 수정) | hint가 모호할 때 사용자가 직접 프롬프트 수정 |
| 누적 토큰·비용 표시 | 매 슬롯 끝에 1줄 — 비용 감각 유지 |
| 슬롯 단위 적용 | 한 슬롯 OK 후 즉시 deck.html에 반영. 사용자가 새로고침해 즉시 확인 가능 |

### 7-5. 재생성 시 프롬프트 보강

`r` 누르면 사용자에게 짧은 보강 입력을 받는다:

```
재생성 — 어떻게 다르게?
> 색감 더 차갑게, 새벽 분위기

▼ 보강 프롬프트:
  "잔잔한 호수, 청록·녹색 톤, ...
   추가 요청: 색감 더 차갑게, 새벽 분위기."

[Enter=실행]
```

---

## 8. codex 호출 패턴

`Codex CLI 이미지 생성 가이드`(vault: `04 Knowledge/AI/Tools/`) 검증된 호출:

```bash
# 프롬프트를 파일로 저장 (한글 안전)
cat > "outputs/{프로젝트}/.codex-prompt.txt" << 'EOF'
{프롬프트 본문}
결과를 {slot_id}.png 파일명으로 저장.
EOF

# codex 호출
cat "outputs/{프로젝트}/.codex-prompt.txt" | codex exec \
  --full-auto \
  --skip-git-repo-check \
  -C "outputs/{프로젝트}/images/" \
  [-i "{참조이미지}"] \
  -

# 결과는 ~/.codex/generated_images/{session-id}/ig_*.png에 생성됨
# 위 -C 폴더로 자동 복사되도록 프롬프트에 명시
```

### 프롬프트 구성 요소 (자동 생성)

```
[hint] 자료에서 추출한 시각 묘사
[style] DESIGN_SYSTEM의 mood·industry·tone 키워드
[ratio] data-slot-ratio (예: "16:9 와이드")
[purpose] 슬라이드 메시지 (예: "발표 커버 — 호수의 비유로 시작")
[file_save] "결과를 {slot_id}.png로 저장"
[guard] (필요 시) "image_gen 툴 사용. PIL/코드 합성 금지"
```

### 병렬 실행 가능 여부

- **단일 codex 세션**: 순차 (병렬 시 파일 충돌 — vault 가이드 경고)
- **다중 codex 세션 (서로 다른 -C 폴더)**: 4세션까지 병렬 검증됨
- 한 장씩 컨펌 모드에서는 **순차가 디폴트** — 사용자가 매 결과를 보고 결정해야 하므로
- "전부 자동" 모드에서만 병렬 옵션 (선택지 [2]·[3] 변형으로 향후 추가 가능)

### 참조 이미지 (-i) 사용 조건

- 슬라이드 시리즈에서 **시각 일관성**이 중요할 때 (예: 같은 캐릭터, 같은 톤)
- 첫 슬롯 결과를 다음 슬롯 참조로 넘기는 흐름
- 참조 이미지 첨부 시 "X만 참고, Y는 무시" 분리 지시 필수 (vault 가이드)

---

## 9. 사용자 제공 이미지 처리

### 9-1. 입력 방식

```
처리: > b
경로 또는 URL: > D:/assets/team_photo.jpg
```

지원 형식:
- 로컬 절대 경로 (Windows: `D:/...`, Mac: `/Users/...`)
- URL (https://, Unsplash 등)
- "나중에 줄게" — placeholder 유지하고 다음 슬롯으로

### 9-2. 처리

1. 파일 복사·다운로드 → `outputs/{프로젝트}/images/{slot_id}.{원본확장자}`
2. 비율 검증 — `data-slot-ratio`와 차이 크면 경고 + 옵션:
   - `[c]` 자동 crop (center crop)
   - `[k]` 그대로 사용 (비율 다름 감수)
   - `[d]` 다른 이미지로 다시 시도
3. HTML의 `data-slot-status`를 `filled`로 갱신 + `style="background-image:..."` 추가

### 9-3. 저작권·라이선스 (한 줄 가이드)

```
사용자 제공 = 사용자 책임. AI 생성 = 라이선스 명확.
Unsplash·Pexels 등 stock URL 입력 시 → 그 사이트 라이선스 적용.
codex 생성 = OpenAI 약관(상업·비상업 사용 OK).
```

스킬은 라이선스 검증 책임 없음. 사용자 입력 그대로 진행.

---

## 10. 재개(resume) 메커니즘

### 10-1. 자동 감지

다음 세션에서 동일 프로젝트 진입 시:

```
1. outputs/{프로젝트}/images.manifest.json 확인
2. status='placeholder' 슬롯 목록 추출
3. 사용자에게 "이미지 패스 11개 미처리. 재개할까요?" 1회 질문
```

### 10-2. 부분 재개

```
이미지 패스 재개
미처리 슬롯: 11개 (#19 ~ #29)
다음 슬롯부터 진행:
  #19 / 29 — slot_19_s21_photo_amish_community
  ...
```

### 10-3. 슬롯 교체

이미 `filled`인 슬롯도 사용자가 명시 요청 시 재처리:
```
"slot_07 다시 만들어줘"
→ 해당 파일 삭제 + status=placeholder 복귀 → 단일 슬롯 패스
```

---

## 11. PPTX 변환 시 처리

`slide-pptx-agent`가 변환할 때:

1. `data-slot-id`가 있는 모든 요소를 스캔
2. `status='filled'` → 해당 PNG 파일을 picture로 삽입
3. `status='placeholder'` → 회색 박스 + hint 텍스트 (PPTX placeholder)
4. `type='diagram'` → 인라인 SVG/HTML을 PPTX shape으로 변환 (또는 캡처 이미지 fallback)
5. 비율은 `data-slot-ratio` 따라 PPTX picture box 크기 결정

---

## 12. project-planner 책임 (요약)

자료 분석 시 다음을 추출해 BRIEF에 포함한다:

```yaml
image_hints:
  - slot_seq: 1
    slide: 1
    type: photo
    ratio: "16:9"          # 슬라이드 레이아웃에 따라 추정 — DSM·SDA가 확정
    hint_original: "잔잔한 호수 사진 또는 DNA 이중나선..."
    hint_normalized: "잔잔한 호수, 청록·녹색 톤"
    slug: "lake_cover"
  - slot_seq: 2
    slide: 2
    type: illust
    hint_original: "호수 위 물고기들 사진 + 그 아래에 DNA 가닥들이 모여 있는 일러스트"
    hint_normalized: "호수와 DNA 가닥 비유 일러스트"
    slug: "lake_dna_split"
  ...
```

**추출 패턴**:
- `**시각자료**` 섹션 (마크다운 — 본 자료처럼 명시적 케이스)
- "그림 N", "사진:", "일러스트:" 등 caption 키워드
- 본문 비유적 묘사 ("호수처럼", "복권 같은") — 명시적 시각 묘사가 없을 때만 보조적
- hint가 명시 없으면 슬롯 생성하지 않음 — 텍스트만 슬라이드는 텍스트만으로 둠

세부 추출 규칙은 `project-planner.md`의 "이미지 단서 추출" 섹션 참조.

---

## 13. slide-deck-agent 책임 (요약)

슬라이드 HTML 생성 시:

1. BRIEF의 `image_hints` 슬롯 목록을 받아 **레이아웃 결정에 반영**
   - `photo` / `illust` 슬롯이 있는 슬라이드 → `photo-overlay` / `photo-split` / `1col-full` 레이아웃 우선 선택
   - hint 없는 슬라이드 → 일반 grid 레이아웃
2. 슬롯별 마크업 생성:
   - `photo` / `illust` → §4-1 placeholder 마크업
   - `diagram` → §4-3 인라인 마크업 (SVG/CSS 직접 생성)
3. 1차 완료 시점에 슬롯 인벤토리를 `images.manifest.json`에 초기화 (status: `placeholder`)
4. **이미지 채우기는 본 에이전트 책임 X** — 1차 완료까지만. 이후 메인이 이미지 패스 발동.

세부 마크업·CSS는 `slide-deck-agent.md`의 "이미지 슬롯 처리" 섹션 참조.

---

## 14. 흐름 통합도 (전체 그림)

```
[STEP 1] project-planner
  └─ image_hints 추출 → BRIEF에 포함

[STEP 2] design-system-manager
  └─ 모드·스타일 확정 (image_hints는 layout 결정에 영향)

[STEP 3] slide-deck-agent (2차 호출)
  └─ photo/illust 슬롯 → placeholder 마크업
  └─ diagram 슬롯 → 인라인 SVG/CSS
  └─ images.manifest.json 초기화
  → 1차 완료 (deck.html + placeholder 박힘)

[STEP 4] slide-qa-agent
  └─ placeholder도 검수 대상 (data-slot-* 속성 일관성, ratio 적용 등)

[STEP 5] visual-refiner
  └─ placeholder 시각도 평가 (디자인 통일성)

[STEP 5.5] 사용자 컨펌 게이트 (디자인)
  └─ 디자인 OK 받은 후 ↓

[STEP 6] 핸드오프
  └─ 옵션 제시: "이미지 슬롯 N개 placeholder. 채울까요? [y/n]"
  └─ y → 이미지 패스 진입 (§7) → 슬롯별 채우기 → 다시 핸드오프
  └─ n → placeholder 유지하고 핸드오프 종료. 다음 세션에 재개 가능

[STEP 7] (선택) slide-pptx-agent
  └─ §11 PPTX 변환 시 처리
```

---

## 15. 메모리·다른 reference와의 관계

- **photo-layouts.md** — 사진 레이아웃 (`photo-overlay`, `photo-split`, `full-bleed`) + Unsplash ID 표. 본 문서가 "어떻게 채울지", 그 문서가 "어떻게 배치할지"
- **color-rules.md** — 전체화면 배경 이미지 z-index 3레이어 구조. placeholder도 동일 구조 따름
- **slide-layouts/** — 그리드별 레이아웃 — `image-slot` 요소가 들어갈 자리 정의
- **memory/feedback_color_mix_obligation.md** — placeholder CSS도 `rgba` 금지 / `color-mix` 의무
- **vault: 04 Knowledge/AI/Tools/Codex-CLI-이미지생성-가이드.md** — codex 호출 검증된 패턴. §8은 그 가이드의 슬라이드 컨텍스트 적용판
