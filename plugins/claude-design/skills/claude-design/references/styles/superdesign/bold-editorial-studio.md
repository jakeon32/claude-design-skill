# Bold Editorial Studio
source: superdesign.dev
category: light

```yaml
palette: { bg: "#FFFFFF", primary: "#000000", secondary: "#525252", meta: "#737373", border: "rgba(0,0,0,0.1)", footer_bg: "#0A0A0A", footer_text: "#FFFFFF" }
typography:
  heading: "Inter"
  body: "Inter"
  mono: "monospace"
  hero: { size: "12vw", weight: 700, tracking: "-0.05em", leading: "0.9" }
  body_spec: { weight: 400, tracking: "-0.02em", leading: "1.5" }
  meta: { size: "14px", transform: "uppercase", tracking: "0.1em" }
style_traits: [순수 흑백 에디토리얼, 타이포 퍼스트 스튜디오, difference 커서, 비대칭 라운드 마키 카드, 사진이 유일한 컬러 소스]
cursor: "32px circle, border 1px solid black, bg white, mix-blend-mode: difference, hover scale(2.5), lerp 부드러운 지연 추적"
border_rule: "1px 이상 절대 금지"
effects:
  image: "grayscale(1)→grayscale(0) + scale(1.05), 700ms"
  hover_overlay: "black 10% opacity"
  cursor_hidden: "cursor: none on body"
animation:
  reveal: "translateY(100%)→0, cubic-bezier(0.16,1,0.3,1) 1s, 글자별 stagger"
  marquee: "linear infinite 30s, 컨테이너 hover 시 pause"
  easing_rule: "cubic-bezier(0.16,1,0.3,1) 전용"
layout: [fixed mix-blend-difference 헤더(logo 'sd' + plus 토글), 80vh 중앙정렬 히어로(stagger 글자 reveal), 풀와이드 마키(5:7 비율 비대칭 카드), 2-col 프로젝트 그리드, #0A0A0A 4-col 푸터]
components:
  header: "mix-blend-mode: difference 컨테이너, lowercase 'sd' 좌 + plus 아이콘 우"
  marquee_card: "5:7 aspect, 비대칭 border-radius 교대: A(top-left 100px) / B(top-right 100px + bottom-left 40px) / C(40px 전체)"
  project_item: "4:3 이미지 + 10% black hover overlay, 하단 1px border-top + 타이틀/카테고리/연도(mono)"
  footer: "#0A0A0A, 4-col"
special_notes:
  - "팔레트 엄격히 흑백만 — 색상은 프로젝트 사진에서만 허용"
  - "모든 hover 최소 500ms 부드러운 easing"
  - "body cursor: none 필수 (커스텀 커서만 사용)"
  - "border 1px 초과 금지"
```
