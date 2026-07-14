---
name: table-layouts
description: "슬라이드 표(Table) 레이아웃 HTML 템플릿 — 비교표, 스펙표, 요금표. 얼룩말 무늬 기본 OFF, tabular-nums 숫자 정렬, 수직 격자선 금지, 행≤7·열≤6 상한(ISO 역산). 표를 쓸지 차트를 쓸지 판단하는 결정표 포함."
---

# Table Layouts

> **2026-07-14 신설.** 그 전까지 이 스킬에는 **표 템플릿이 0개**였다. 카탈로그에 카테고리조차
> 없어서 AI가 "비교표를 만들어야겠다"는 판단 자체를 못 했고, 만들 때마다 즉흥적으로 짰다.

**근거 등급**: ◎ 실험적 근거 / ○ 표준·전문가 규범 / △ 관례(무해하나 근거 없음) / ✕ 근거 없는 통념(따르지 말 것)

---

## 0. 슬라이드 표는 웹 표가 아니다

웹/앱 데이터 테이블 연구(NN/g, Material 등)를 그대로 옮기면 틀린다.

| 축 | 웹 데이터 테이블 | 슬라이드 표 |
|---|---|---|
| 과업 | 검색·정렬·조회(lookup) | 발표자가 지목하는 **결론 1개** 확인 |
| 행 수 | 수십~수백 (스크롤) | 3~8 |
| 시청 거리 | 40~60cm | 화면 높이의 4~8배 |

이 문서의 수치는 전부 **1280×720 캔버스 + 투사(가장 먼 관객 = 화면 높이의 5배)** 기준으로 유도했다.

---

## 1. ★ 먼저: 이게 표여야 하는가 (표 vs 차트)

> **표는 기본값이 아니라 예외다.** 슬라이드는 대부분 "패턴"을 보여주지 "값 조회"를 시키지 않는다.

**Tufte** ○: *"표는 20개 이하의 작은 데이터 집합을 보고할 때 그래픽을 능가한다."*
→ 뒤집으면 **숫자가 20개(행×열)를 넘으면 차트가 유리하다.**

### 결정표 (생성기가 이대로 적용)

| 상황 | 선택 |
|---|---|
| **값 자체가 결론** (요금 3만 vs 5만, 8GB vs 16GB) | **표** |
| **단위가 서로 다른 항목**을 나란히 (가격/용량/기간/지원여부) | **표** — 차트로는 불가능 |
| 항목 ≤5, 지표 ≤4, **숫자 총 20개 이하** | **표** |
| 셀의 절반 이상이 **텍스트**(○/×, "지원", "베타") | **표** (비교 매트릭스) |
| 관객이 값을 **받아적어야** 함 | **표** |
| 시간에 따른 추이 | **선 차트** → data-layouts.md |
| 항목 간 크기 순위·격차 (항목 6개 이상) | **막대 차트** → data-layouts.md |
| 부분-전체 구성 | **100% 누적 막대** → data-layouts.md |
| 두 변수 관계·분포 | 산점도 → data-layouts.md |
| **숫자 25개 이상** | **차트**, 또는 표 + 히트맵 |

**혼합안**: 값도 패턴도 필요하면 → 표 + 마지막 열에 **인라인 바**(막대 폭 = 값). §6

---

## 2. 크기 상한 — 관례가 아니라 기하학으로 유도한다

떠도는 "3~5열, 10행 이하"는 △ 관례다(근거 없음). 우리는 **가독 최소 글자 크기에서 역산**한다.

**근거 사슬** ○
1. **ISO 9241-303**: 라틴 문자 최소 높이 **16 arcmin**(시각), 권장 20~22 arcmin
2. 가장 먼 관객 거리 D = 화면 높이 H의 5배, 캔버스 720px
3. 역산: 16 arcmin → 대문자 높이 ≈ 0.0233 H ≈ 17px → **font-size ≈ 24px**

⇒ **본문 24px = 절대 하한, 26~30px = 기본값.**
흔히 쓰는 16~18px 표는 **뒷줄에서 ISO 최소치 미달**이다.
글자를 줄여 행·열을 늘리는 선택지는 없다 — 그래서 상한이 생긴다.

**상한 유도** (본문 26px, 행 높이 56px, 콘텐츠 영역 1120×500px)
- **행**: 500 ÷ 56 ≈ 8.9 → 머리글 1 + **데이터 행 7** (합계 행 쓰면 6)
- **열**: 라벨 열 300px 확보 후 (1120−300) ÷ 180 ≈ 4.5 → **데이터 열 4~5**, 총 **5~6열**

| 항목 | 기본 | **하드 상한** | 초과 시 |
|---|---|---|---|
| 데이터 행 | 5 | **7** (합계 포함 8) | §3 |
| 총 열 | 4 | **6** (라벨 1 + 데이터 5) | §3 |
| 본문 폰트 | 26px | **하한 24px** | 줄이지 말고 **데이터를 줄인다** |

> △ "작업기억 4±1이므로 열은 4개까지"라는 논증도 보이지만, Cowan(2001)은 기억 청크 연구이지
> 표의 열 수를 실험한 게 아니다. **보조 논거로만 쓰고 근거로 인용하지 말 것.**

---

## 3. 상한 초과 시 처리 (우선순위 순)

1. **잘라내기** — 결론에 기여하지 않는 열·행 삭제. (대부분 여기서 끝난다)
2. **집계** — 하위 항목을 "기타 N건"으로 묶어 1행으로
3. **분할** — 의미 단위로 2~3장. 각 장의 제목이 서로 다른 주장을 하도록
4. **요약 열로 대체** — 원시 값 대신 파생값(차이·순위·증감률)만 남기고 원표는 **부록**으로
5. **차트로 전환** — §1

→ 전체 결정 트리는 [`density-rules.md` §5](../density-rules.md) 참조. 순서는 동일하다.

---

## 4. 데이터-잉크 — 수직 격자선을 지운다

**규칙**: 지워도 정보가 안 없어지는 잉크(수직 격자선, 이중선, 셀 테두리, 배경 채움)는 전부 지운다.
남기는 선은 **머리글 아래 1줄 + 표 끝 1줄**뿐.

**근거** ○◎
- LaTeX `booktabs`(학술 조판 사실상 표준)는 두 가지를 **명시적으로 금지**한다:
  **"수직 괘선을 절대 쓰지 말 것", "이중 괘선을 절대 쓰지 말 것."**
- Schwabish *Ten Guidelines for Better Tables* #1·#2: 머리글을 본문에서 분리, 무거운 격자선 대신 절제된 구분선
- Few: 괘선은 데이터 대비 시각적으로 억제 — 최대한 얇고 옅게

**✕ 통념**: "열을 구분하려면 수직선이 필요하다" — 근거 없음.
**열 구분은 여백이 한다.** 수직선은 시선을 세로로 가두어 행 단위 읽기를 방해한다.

---

## 5. 🔴 얼룩말 무늬(Zebra Striping) — 가장 오해가 많은 항목

**규칙: 슬라이드 표(≤8행)에는 기본값 OFF.**
**6행 이상 AND 5열 이상**으로 가로 추적이 필요할 때만 켠다. 켤 때는 단일 행 교대, 매우 옅은 단색.

**근거의 실제 상태** ◎ (조건부)
- **1차 실험** (A List Apart, n=244): 줄무늬 유/무 간 **정확도에 통계적 유의차 없음.**
  속도도 6문항 중 1개에서만 유의. 선호도만 46%.
- **2차 실험** (같은 저자, 유효 세션 2,276, **15초 시간 압박 + 빈 셀 + 스크롤 필요한 넓고 긴 표**):
  8문항 중 **3문항에서 정확도 유의 개선**. 특히 오른쪽→왼쪽 되짚어 읽을 때 이득.

**해석 (중요)**: 이득이 확인된 조건은 **긴 행 + 많은 열 + 시간 압박 + 스크롤**이다.
**6행 × 4열짜리 슬라이드 표에 그 결과를 옮기는 것은 근거 없는 외삽이다.**

| 통념 | 판정 |
|---|---|
| "얼룩말 무늬는 무조건 가독성을 높인다" | ✕ 1차 실험에서 정확도 개선 없음. **작은 표에서의 이득은 입증되지 않았다** |
| "2행씩 묶어 칠하면 더 좋다" | ✕ 어떤 실험에서도 검증된 바 없음. 저자 권고는 **단일 행 교대** |
| "줄무늬 대신 옅은 수평선" | △ 2차 실험 저자가 인정한 차선책. **슬라이드에선 잉크가 적어 오히려 이쪽이 낫다** |

---

## 6. 숫자 정렬 — tabular figures

**규칙**: 숫자는 **우측 정렬 + 소수 자릿수 통일 + tabular figures**, 텍스트는 좌측 정렬,
**머리글은 그 열의 데이터 정렬을 따라간다**.

**tabular figures가 필요한 진짜 이유** ◎
비례(proportional) 숫자는 글리프 폭이 다르다("1"은 좁고 "8"은 넓다).
그래서 **우측 정렬을 해도 내부 자릿수가 세로로 어긋난다.**
`font-variant-numeric: tabular-nums`(OpenType `tnum`)가 모든 숫자를 동일 폭으로 만든다.

> ⚠️ **폰트에 `tnum` 글리프가 없으면 조용히 무시된다.**
> 폰트 화이트리스트: **Pretendard · Inter · Arial · Helvetica · Roboto**.
> Georgia류 old-style 숫자 폰트 금지. **PPTX 내보낼 때 대체 폰트로 바뀌면 정렬이 깨진다.**

**✕ 통념**: "숫자 열에는 monospace를 써라" (NN/g 포함 여러 가이드) — **처방이 과하다.**
필요한 건 **등폭 숫자**지 등폭 문자가 아니다. monospace는 한글 라벨과 섞이면 조판이 망가진다.

**✕ 통념**: "숫자 가운데 정렬이 깔끔하다" — 자릿수 정렬이 깨져 **비교 자체가 불가능**해진다. 금지.

### 데이터 규칙 (생성기가 강제)

1. 한 열의 소수 자릿수는 **동일** (`1.0 / 12.5 / 103.2` ○ — `1 / 12.5 / 103.24` ✕)
2. **유효숫자 3자리 이하**로 반올림 (Ehrenberg ○◎ — 암산 비교가 가능해야 표가 기능한다)
3. **단위는 셀이 아니라 머리글에** → `매출 (억원)`, 셀은 `1,240`
4. 음수는 하이픈이 아니라 **U+2212 −**, 결측은 빈칸이 아니라 `—`
5. 행 순서는 가나다순이 아니라 **값 크기순** (시계열은 시간순)

---

## 7. 강조 — "이 행이 결론"임을 보여주는 법

**규칙: 표당 강조 채널은 하나만.** 결론 행은 **옅은 배경 + 해당 값만 굵게.**
굵게를 행 전체에 바르지 않는다. **강조는 희소성으로 작동한다.**

| 순위 | 수단 | 언제 |
|---|---|---|
| 1 | **행 배경 옅은 틴트** (accent 8~12%) | "이 행이 결론" — 가장 강하고 안전 |
| 2 | **굵기(600~700)** — 강조할 **값 셀에만** | 결론 행 안의 핵심 숫자 1개 |
| 3 | **색상(텍스트)** | 증감처럼 **의미가 이분법**일 때 |
| 4 | **히트맵 셀** | 3열 이상 × 4행 이상의 **동일 단위 숫자 격자**일 때만 |
| ✕ | 테두리 박스·굵은 외곽선 | 잉크 대비 정보 0. 금지 |

**히트맵 규칙**
- **동일 단위·동일 스케일** 격자에서만. 단위가 섞이면 색이 거짓말을 한다
- 단일 색상 5단계. 기준선 위/아래 구분이 필요할 때만 발산형
- **텍스트 대비 유지** — 어두운 셀에서는 글자색 흰색 반전 (WCAG 4.5:1)
- **색만으로 정보 전달 금지** — 셀에 항상 숫자 병기

---

## 8. 복붙용 CSS (토큰 + 베이스)

```css
/* ============ Slide Table Tokens (1280×720) ============ */
:root{
  --tbl-font:        26px;    /* 본문. 하한 24px */
  --tbl-head-font:   22px;
  --tbl-row-h:       56px;    /* ≈ 2 × font */
  --tbl-pad-x:       20px;    /* ≈ 0.75em */
  --tbl-pad-y:       14px;
  --tbl-rule:        var(--text);        /* 머리글 아래 / 표 끝 */
  --tbl-rule-soft:   color-mix(in srgb, var(--text) 8%, transparent);
  --tbl-zebra:       color-mix(in srgb, var(--text) 3.5%, transparent);
}

.slide-table{
  width:100%;
  border-collapse:collapse;
  table-layout:fixed;                    /* 열폭 예측 가능하게 */
  font-size:var(--tbl-font);
  color:var(--text);
  font-variant-numeric: tabular-nums lining-nums;
  font-feature-settings:"tnum" 1,"lnum" 1;
}
.slide-table th,.slide-table td{
  border:0;                              /* 셀 테두리 전면 금지 */
  padding:var(--tbl-pad-y) var(--tbl-pad-x);
  height:var(--tbl-row-h);
  vertical-align:middle;
  white-space:nowrap;                    /* 셀 내 줄바꿈 금지 — 넘치면 데이터를 줄인다 */
  overflow:hidden; text-overflow:ellipsis;
}
.slide-table thead th{
  font-size:var(--tbl-head-font);
  font-weight:600;
  color:var(--muted);
  border-bottom:2px solid var(--tbl-rule);   /* booktabs \midrule */
  letter-spacing:.01em;
}
.slide-table tbody tr:last-child td{
  border-bottom:2px solid var(--tbl-rule);   /* booktabs \bottomrule */
}

/* 정렬 — 머리글은 열 데이터를 따라간다 */
.slide-table .text, .slide-table th.text{ text-align:left; }
.slide-table .num,  .slide-table th.num { text-align:right; }
.slide-table td:first-child{ padding-left:0; font-weight:500; }      /* 라벨 열 */
.slide-table td:nth-child(2), .slide-table th:nth-child(2){ padding-left:32px; }  /* 라벨↔데이터 분리 */

/* 밀집 표(행≥6 AND 열≥5)에서만 — 기본 OFF */
.slide-table.is-dense tbody td{ border-bottom:1px solid var(--tbl-rule-soft); }
.slide-table.is-dense tbody tr:nth-child(even) td{ background:var(--tbl-zebra); }

/* 결론 행 — 강조 채널은 하나만 */
.slide-table tr.is-key td{ background:color-mix(in srgb,var(--accent) 10%,transparent); }
.slide-table tr.is-key td.is-key-value{ font-weight:700; color:var(--accent); }
.slide-table.has-highlight tbody tr:nth-child(even) td{ background:transparent; } /* 줄무늬 무력화 */

/* 합계 행 */
.slide-table tr.is-total td{ border-top:1.5px solid var(--tbl-rule); font-weight:700; }

/* 인라인 바 (히트맵보다 슬라이드에서 우선) */
.bar-cell{ position:relative; }
.bar-cell::before{
  content:""; position:absolute; left:0; top:50%; transform:translateY(-50%);
  height:24px; width:var(--v);          /* --v: 값/축최댓값 × 100% — 눈대중 금지 */
  background:color-mix(in srgb,var(--accent) 18%,transparent); border-radius:2px;
}
.bar-cell > span{ position:relative; }
```

---

## 9. 템플릿 3종

형태는 하나고 변형만 다르다.

| 템플릿 | 라벨 열 | 데이터 열 | 강조 | 줄무늬 |
|---|---|---|---|---|
| **비교표** (제품 A/B/C) | 지표명 | 옵션별 (≤4) | 추천 **열** 전체 틴트 | OFF |
| **스펙표** | 항목명 | 값 1~2열 | 없음 (또는 차이 나는 행만) | 행 ≥6 시 ON |
| **요금표** | 플랜명(행) | 가격/한도/지원 (≤4) | 추천 **행** `.is-key` + 가격 셀 굵게 | OFF |

### 9-1. 요금표 (행 강조)

```html
<!-- [Pricing Table] 결론 행 강조 -->
<section class="slide" data-density="D2" style="
  display:flex; flex-direction:column; background:var(--bg); overflow:hidden;
">
  <!-- Action Title — 결론을 문장으로 (density-rules.md §8) -->
  <div style="flex-shrink:0; padding:40px 64px 24px;">
    <p style="font-family:var(--h-font); font-size:40px; font-weight:700;
              color:var(--text); letter-spacing:-0.02em; line-height:1.2;">
      Pro 플랜이 동일 한도에서 40% 저렴하다
    </p>
  </div>

  <div style="flex:1; padding:0 64px; min-height:0;">
    <table class="slide-table has-highlight">
      <thead>
        <tr>
          <th class="text">플랜</th>
          <th class="num">월 요금 (원)</th>
          <th class="num">한도 (건)</th>
          <th class="text">지원</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text">Enterprise</td>
          <td class="num">120,000</td>
          <td class="num">50,000</td>
          <td class="text">전담</td>
        </tr>
        <tr class="is-key">
          <td class="text">Pro</td>
          <td class="num is-key-value">72,000</td>
          <td class="num">50,000</td>
          <td class="text">이메일</td>
        </tr>
        <tr>
          <td class="text">Basic</td>
          <td class="num">29,000</td>
          <td class="num">10,000</td>
          <td class="text">문서</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- 출처 — 좌하단, 본문보다 확실히 작게 -->
  <div style="flex-shrink:0; padding:0 64px 20px;">
    <p style="font-family:var(--b-font); font-size:17px; color:var(--muted);">
      Source: 공식 요금표 (2026-07 기준)
    </p>
  </div>
</section>
```

### 9-2. 비교표 (열 강조)

열 방향 강조는 `td:nth-child(n)`에 틴트를 건다.

```css
/* 추천 열이 3번째일 때 */
.slide-table.col-key-3 td:nth-child(3),
.slide-table.col-key-3 th:nth-child(3){
  background: color-mix(in srgb, var(--accent) 10%, transparent);
}
.slide-table.col-key-3 th:nth-child(3){ color: var(--accent); font-weight:700; }
```

---

## 10. PPTX 내보내기 시 반드시 처리할 것

| CSS 기능 | PPTX | 대응 |
|---|---|---|
| `tr:nth-child(even)` 줄무늬 | 없음 | 생성 시 **셀별 인라인 배경**으로 베이크 |
| 셀 테두리 없애기 | PPTX 기본 테이블 스타일이 **격자선·밴딩을 강제** | 표 스타일 "No Style, No Grid" 지정, 또는 `tblPr`에서 `bandRow=0` `firstRow=1` 후 필요한 선만 XML 추가 |
| 셀 테두리(`a:lnB`) | python-pptx에 고수준 API 없음 | 헬퍼 `set_cell_border(cell, edge, color, width)` 하나 만들어 재사용 |
| 셀 배경 | `cell.fill.solid()` 지원 | 그대로 사용 |
| 셀 패딩 | `cell.margin_*` 지원 | CSS와 동일 값 명시 (20px ≈ 0.21in) |
| `tabular-nums` | CSS 속성 없음 | **폰트로 해결** — `tnum` 기본 폰트 지정 + **폰트 임베드 켜기** |
| `color-mix()` | 없음 | 생성 시 최종 HEX로 계산 |
| `text-overflow: ellipsis` | 없음 | 넘치는 셀은 **데이터를 줄여서** 해결 |

---

## 11. 체크리스트 (표 만들 때 순서대로)

1. [ ] **이게 표여야 하나?** §1 결정표 통과. (숫자 25개 초과 → 차트 재검토)
2. [ ] 데이터 행 ≤7, 총 열 ≤6인가? 아니면 §3 순서로 처리
3. [ ] 슬라이드 제목이 **표의 결론을 문장으로** 말하는가?
      ("2026 요금 비교" ✕ → "Pro 플랜이 동일 한도에서 40% 저렴하다" ○)
4. [ ] 행 순서 = 값 크기순인가? (시계열 제외)
5. [ ] 열별 소수 자릿수 통일 + 유효숫자 3자리 이하 + 단위는 머리글로
6. [ ] 숫자 열: 우측 정렬 + `tabular-nums` + **머리글도 우측 정렬**
7. [ ] **수직선·셀 테두리 0개.** 가로선은 머리글 아래 + 표 끝(+합계 위)만
8. [ ] 강조 채널 1개만? 굵은 셀이 3개 넘으면 다시
9. [ ] 줄무늬는 **행≥6 AND 열≥5**일 때만, 강조 행과 동시 사용 ✕
10. [ ] 본문 ≥24px. 넘치면 **폰트를 줄이지 말고 데이터를 줄인다**
11. [ ] 색 쓴 셀: 대비 4.5:1 이상, 색만으로 정보 전달 ✕ (숫자 병기)

---

## 12. 통념 vs 근거 요약

| 주장 | 판정 |
|---|---|
| 얼룩말 무늬는 가독성을 높인다 | ✕ **조건부**. 작은 슬라이드 표에 대한 근거는 **없다** |
| 2행씩 묶은 줄무늬가 더 좋다 | ✕ 검증된 바 없음 |
| 열 구분에 수직 격자선이 필요하다 | ✕ booktabs·전문 조판: **수직 괘선 금지**. 여백으로 구분 |
| 숫자 열엔 monospace 폰트 | ✕ **처방 오류**. 필요한 건 등폭 *숫자*(`tabular-nums`) |
| 숫자 가운데 정렬 | ✕ 자릿수 정렬 파괴 |
| "슬라이드 표는 3~5열 10행 이하" | △→○ 관례엔 근거 없음. **ISO 9241-303 역산으로 ≤6열/≤7행** — 이쪽을 근거로 |
| 숫자 우측·텍스트 좌측·머리글은 데이터 따라 | ○ Schwabish·NN/g·Few 합의 |
| 과감한 반올림(유효숫자 2~3자리) | ○◎ Ehrenberg(1977) |
| 표는 숫자 20개 이하에서 차트를 이긴다 | ○ Tufte |
| 슬라이드 제목을 문장형 주장으로 | ◎ Alley & Neeley — 이해·회상 p<.01 유의 개선 |

---

## 출처

- [Enders — Zebra Striping: Does it Really Help? (A List Apart)](https://alistapart.com/article/zebrastripingdoesithelp/) · [More Data for the Case](https://alistapart.com/article/zebrastripingmoredataforthecase/)
- [Schwabish — Ten Guidelines for Better Tables (J. Benefit-Cost Analysis 11(2), 2020)](https://www.cambridge.org/core/journals/journal-of-benefit-cost-analysis/article/abs/ten-guidelines-for-better-tables/74C6FD9FEB12038A52A95B9FBCA05A12)
- [Ehrenberg — Rudiments of Numeracy (JRSS-A 140(3), 1977)](https://rss.onlinelibrary.wiley.com/doi/abs/10.2307/2344922)
- [Tufte — The Visual Display of Quantitative Information](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/) · [Data-Ink Ratio](https://infovis-wiki.net/wiki/Data-Ink_Ratio)
- [Few — Show Me the Numbers (요약)](https://principus.si/2021/03/22/stephen-few-show-me-the-numbers-designing-tables-and-graphs-to-enlighten/)
- [NN/g — Data Tables: Four Major User Tasks](https://www.nngroup.com/articles/data-tables/)
- [booktabs (CTAN)](https://ctan.org/pkg/booktabs?lang=en) — 수직 괘선·이중 괘선 금지
- [MDN — font-variant-numeric](https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric)
- [ISO 9241-303:2011 (발췌)](https://cdn.standards.iteh.ai/samples/57992/bddfd91165b444f6b9815a6993feadc5/ISO-9241-303-2011.pdf) · [AVIXA DISCAS](https://www.avixa.org/resources/standards/display-image-size-for-2d-content)
- [W3C — WCAG SC 1.4.3 Contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [Alley & Neeley — Rethinking the Design of Presentation Slides (PDF)](http://writing.engr.psu.edu/2005_alley_neeley.pdf)
- [python-pptx — Tables](https://python-pptx.readthedocs.io/en/latest/user/table.html) · [cell border issue #71](https://github.com/scanny/python-pptx/issues/71)
