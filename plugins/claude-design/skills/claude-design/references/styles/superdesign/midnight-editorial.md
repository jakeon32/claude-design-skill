# Midnight Editorial
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", surface: "#111111", surface2: "#1A1A1A", primary: "#EBEBEB", muted: "#888888", dim: "#666666", faint: "#444444", accent: "#FF6B50", border: "#333333", border2: "#222222" }
gradient_card: "from #4F46E5 to #7C3AED (indigo→purple, 벤에핏 카드 2번)"
typography: { heading: "Satoshi", body: "Satoshi / Inter", weight: "300~800", size_hero: "13vw", leading_hero: "0.9", tracking_hero: "-0.05em", label: "10px bold uppercase tracking-widest" }
style_traits: [미드나잇 에디토리얼, Satoshi 타이포 중심, 코랄 액센트, 이중 네비게이션(상단+하단플로팅), 스태거드 갤러리 그리드]
selection: "background #FF6B50, color #FFFFFF"
effects:
  hero_bg: "radial-gradient circle at center, #1A1A1A 0%→#050505 70%, opacity 60%"
  image: "opacity 60%, grayscale → opacity 100% + grayscale(0) + scale(1.05) on group hover, 700ms"
  glass: "rgba(17,17,17,0.8), backdrop-blur(12px), border rgba(255,255,255,0.1)"
animation:
  float: "translateY 0→-10px, 4s ease-in-out infinite"
  logo_hover: "rotate(12deg)"
  social_hover: "bg-white + text-black + -translateY-2 (8px 위로)"
  work_arrow: "border circle → #FF6B50 bg + black text on hover"
layout: [fixed 상단 glass 네비, fixed 하단 pill 플로팅 네비, 100vh 중앙정렬 히어로('/design' 13vw), 벤에핏 2-col 그리드(rounded-2.5rem), 2-col 스태거드 work 갤러리(2번째 col +mt-24 오프셋), 대형 footer CTA]
components:
  top_nav: "logo(8×8 white square S. hover rotate12) + 중앙 링크(#888888→white) + Get started(#1A1A1A bg)"
  bottom_nav: "glass pill, 아이콘 5개(grid/globe/smartphone/package/megaphone) + #FF6B50 Contact 버튼"
  hero: "'/design' 13vw bold, 하단 좌: 팀 아바타 스택(grayscale→color group hover), 하단 우: 이메일 border-b 링크"
  benefit_card: "rounded-[2.5rem], 'Start faster.' / 'Earn sooner.'(#444→#666 hover), 우상단 pill 배지"
  work_article: "4:3 aspect, 60%→100% opacity + scale hover 700ms, 제목 hover coral, arrow circle button"
  footer: "10-14vw 'LET'S TALK.' font-black tracking-tighter, 소셜 14px 원형 버튼, 최하단 10px copyright"
special_notes:
  - "하단 플로팅 네비 유지 — 상단 네비와 역할 분리 (상단: 브랜드/링크, 하단: 기능/CTA)"
  - "Work 갤러리 2번째 col은 항상 mt-24 오프셋 (리듬 생성)"
  - "이미지 기본 opacity 60% — hover 시 full reveal (극적 효과)"
```
