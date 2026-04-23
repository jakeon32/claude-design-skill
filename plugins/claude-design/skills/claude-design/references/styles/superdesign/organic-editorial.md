# Organic Editorial Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F7F5EB", fg: "#202A2D", sage: "#CBD0B5", secondary_bg: "#F0EDE1" }
typography: { heading: "DM Serif Display", body: "Inter", accent: "Reenie Beanie", weight: "DM Serif Display: 400 (normal+italic) / Inter: 300–500 / Reenie Beanie: 48px 손글씨", tracking: "0.2em–0.3em uppercase (labels 10px)", size_hero: "up to 160px leading-0.85–1.1" }
style_traits: [Modern Organic Editorial, 따뜻한 크림 페이퍼 감성, DM Serif 대형 헤드라인, 노이즈 텍스처 0.4 opacity, 대형 border-radius 40–64px, 손그림 SVG 밑줄, grayscale→color 2000ms 전환]
radius: "40–64px (이미지 컨테이너) / 999px (pill buttons) — 최소 24px"
shadow: "subtle — 0 4px 20px -2px rgba(0,0,0,0.05)"
effects:
  noise: "natural paper texture 0.4 opacity, fixed global"
  hand_drawn_underline: "SVG path M2 8C50 9.5 100 -2 298 4, stroke-width 4, stroke-linecap round, color #CBD0B5"
  grayscale_transition: "filter: grayscale(100%)→grayscale(0%) + scale(1.05), 2000ms ease-out"
  philosophy_card: "#CBD0B5 bg → #202A2D bg, 500ms transition on hover"
  process_mask: "linear-gradient mask 좌우 edge on horizontal scroll"
animation:
  reveal: "translateY(20px)→0 + opacity 0→1, 0.8s ease-out"
  image_hover: "grayscale→color 2000ms + scale(1.05)"
  philosophy: "#CBD0B5→#202A2D bg flip 500ms"
layout: [sticky 80px nav (backdrop-blur-md #F7F5EB/80, 10px tracking uppercase, pill CTA #202A2D), 160px serif hero (italic first line, SVG 밑줄 #CBD0B5, Reenie Beanie annotation), 80vh 풀너비 이미지 (64px radius, overlay: hr + uppercase label + 72px italic serif), 4:5 team 스태거 그리드, 16:10 가로 process gallery (glassmorphism phase tag), #CBD0B5 48px-radius CTA card, #F0EDE1 footer]
components:
  nav: "80px sticky, logo(아이콘+serif 텍스트), 10px uppercase 0.2em tracking 링크, #202A2D pill CTA"
  hero: "160px DM Serif Display italic first-line, #CBD0B5 SVG 손그림 밑줄, Reenie Beanie 48px annotation + downward arrow"
  hero_image: "full-width 24–48px padding, 64px radius, 80vh height, bottom-left: hr 48px + uppercase label + 72px serif"
  team_grid: "4:5 grayscale→color 24px radius, 비대칭 col 2&4 -48px offset"
  process_gallery: "16:10 비율, left/right gradient mask, glassmorphism phase pill tag, serif title"
  cta_card: "#CBD0B5 bg, 48px radius, white glow blur-120px top, serif 'Ready to evolve?', scale hover pill"
special_notes:
  - "DM Serif Display + Inter 필수 조합"
  - "노이즈 overlay flat 방지용 필수"
  - "radius 24px 이하 금지"
  - "선명한 색상 사용 금지 — muted 팔레트 유지"
  - "섹션 간 최소 160px 여백"
```
