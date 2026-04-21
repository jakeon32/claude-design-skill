# Cinematic Noir
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#000000", zinc: "#09090B", surface: "#18181B", white: "#FFFFFF", ghost: "#FAFAFA", text: "#E5E5E5", muted: "#888888", highlight: "#EF4444" }
typography: { heading: "ZTNature", body: "ZTNature", weight: "900/300-400", size_hero: "11vw~12vw", tracking: "-0.03em", body_size: "1.25rem", label: "14px mono" }
style_traits: [시네마틱 누아르, 갤러리 몰입형, 렌즈 포컬 심도 시뮬레이션, 극단 웨이트 대비(Thin Italic↔Black), 선택 색상만 레드]
radius: "0px (sharp architectural, 곡선 일체 금지)"
selection: "background #EF4444"
effects:
  noise: "grain overlay 15% opacity, mix-blend-mode: overlay"
  radial_bg: "radial-gradient(ellipse at center, rgba(139,69,69,0.4) 0%, rgba(20,20,20,0.8) 60%, rgba(0,0,0,0.95) 100%)"
  nav_blend: "mix-blend-mode: difference (흰/검 섹션 전환 자동 대응)"
scroll_transforms:
  bg_scale: "scroll 0-30% → scale 1.0→1.27 (배경 줌인)"
  heading_scale: "scroll 0-30% → scale 1.0→0.89 (헤딩 후퇴 = 렌즈 초점 이동)"
  label_fade: "절대위치 레이블 scroll 시 opacity 0으로"
  gpu: "transform-style: preserve-3d, will-change: transform"
animation:
  entrance: "cubic-bezier(0.16,1,0.3,1)"
  manifesto_line: "width 0→100% (max 320px) on scroll-into-view"
  card_reveal: "메타데이터 translateY 4px→0, 액션 버튼 opacity 0→1, 300ms"
layout: [fixed mix-blend-difference 네비(px-6 py-8, 18px 500 tracking-tight), 100vh 3레이어 히어로(bg scale↑ + heading scale↓ + fade label), #FFFFFF 2-col 프로젝트 그리드, #09090B 100vh 매니페스토, #FAFAFA 풀와이드 START A PROJECT 푸터]
components:
  hero: "Layer1: 배경이미지+radial tint+grain(scale 1→1.27) / Layer2: 12vw #E5E5E5(scale 1→0.89) / Layer3: 32px 레이블(absolute left calc(100%+1rem), scroll fade)"
  project_grid: "#FFFFFF bg, 'SELECTED WORKS' 8vw Black + 'WORKS' italic Thin, 16:10 카드, hover white circle ArrowUpRight"
  project_card: "#18181B, 이미지 hover scale(1.05), 하단 절대위치 정보(5xl title + 메타 translateY reveal)"
  manifesto: "5-7vw weight 500 centered, 하단 width-animate 수평선 rgba(255,255,255,0.3)"
  footer: "#FAFAFA, 12vw 'START A PROJECT' 풀와이드 border-b, 3-col(소셜 wavy underline / 이메일 3xl / 저작권)"
special_notes:
  - "ZTNature Thin Italic ↔ Black 극단 웨이트 대비 필수"
  - "#EF4444 선택 색상만 — 다른 진동 색상 금지"
  - "곡선 일체 금지 — 건축적 날카로운 엣지만"
  - "mix-blend-difference 네비 필수 — 흰/검 섹션 양쪽 가시성"
```
