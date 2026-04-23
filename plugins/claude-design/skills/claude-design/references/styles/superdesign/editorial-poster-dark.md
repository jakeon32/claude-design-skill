# Editorial Poster Dark
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#0A0A0A", fg: "#FAFAFA", surface: "#1A1A1A", muted_fg: "#737373", accent: "#FF3D00", border: "#262626", card: "#0F0F0F" }
typography:
  primary: "Inter Tight / Inter"
  display: "Playfair Display (pull quote/testimonial 전용)"
  mono: "JetBrains Mono (레이블/스탯/기술 텍스트)"
  weight: "600~700/400"
  scale_hero: "text-4xl→5xl→6xl→7xl→8xl (모바일→데스크탑)"
  tracking: { display: "-0.06em", heading: "-0.04em", body: "-0.01em", label_wide: "0.1em", label_widest: "0.2em" }
  leading: { headline: "1", multiline: "1.1", body: "1.6", longform: "1.75" }
style_traits: [포스터 디자인→웹 번역, 타이포그래피가 전체 비주얼 언어, 갤러리/럭셔리 매거진, 극단적 크기 대비(6:1+), 절제된 버밀리언 액센트]
radius: "0px (예외 없음 — 샤프 엣지만)"
border: "1px (divider), 2px (accent underline)"
shadow: "없음 — layered type + underline + divider로만 깊이 표현"
texture: "SVG feTurbulence fractal noise, opacity 1.5% (거의 보이지 않는 촉각감)"
effects:
  layered_type: "대형 뮤트 텍스트(장식용) 뒤에 소형 밝은 텍스트 앞에 배치"
  accent_bar: "h-1 w-16 bg-accent (키 요소 시각 앵커)"
  text_depth: "border-color offset 복제 텍스트 (-z-10) — 그림자 없이 입체감"
animation:
  micro: "150ms cubic-bezier(0.25,0,0,1) (버튼/밑줄)"
  standard: "200ms (아코디언/컬러)"
  image: "500ms scale(1.05) (이미지 hover, 컨테이너 overflow-hidden)"
  scroll: "opacity 0→1 + translateY 20px→0, 500ms, stagger 80ms, once"
  no_bounce: "cubic-bezier(0.25,0,0,1) 고정 — bounce/spring 금지"
layout: [max-w-5xl(1200px), 비대칭 7/5 또는 8/4 그리드, 스태거드 정렬, py-20(80px)→py-40(160px) 섹션 패딩]
components:
  button_primary: "텍스트+밑줄only (fill 없음), accent 컬러, scale-x-100→110 애니 밑줄, uppercase tracking-wider, active:translate-y-px"
  button_outline: "1px solid fg border, hover: bg-fg + text-bg (완전 반전), 0px radius, px-6"
  button_ghost: "no border no fill, muted_fg→fg hover, h-px 밑줄 scale-x-0→100"
  card: "transparent bg, 0px radius, no shadow, 1px border, hover border 밝아짐"
  card_featured: "2px accent border + accent 배지(px-3 py-1 uppercase mono)"
  input: "#1A1A1A bg, 0px radius, h-12(mobile)/h-14(desktop), focus: border-accent no-ring"
  icons: "Lucide stroke 1.5px, outline only, currentColor, 16-24px"
special_notes:
  - "헤딩:바디 최소 6:1 크기 비율 유지"
  - "accent #FF3D00 아주 드물게 — 헤딩/CTA/밑줄만"
  - "모바일 대형 장식 텍스트(01, 브랜드명 등) hidden으로 가로 스크롤 방지"
  - "버튼 fill 없음 — underline이 primary interactive affordance"
  - "라운드 코너 0px 절대 예외 없음"
```
