# Bold Retro-Modernism Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F5F1E3", red: "#BC2C2C", blue: "#5DA4C9", yellow: "#FCD758", charcoal: "#2C2C2C", fg: "#2C2C2C" }
typography: { heading: "Montserrat", body: "Open Sans", weight: "Montserrat: 700–900 uppercase leading-0.85 -0.05em / Open Sans: 400–600 leading-1.6 / labels: Open Sans 900 10px 0.1em uppercase", size_hero: "9xl", tracking: "-0.05em (heading) / 0.1–0.15em uppercase (labels)" }
style_traits: [Bold Retro-Modernist 1970s Editorial, primary color blocks, solid 12–20px editorial offset shadows, infinite marquee ticker, grayscale→color hover, 90-degree corners]
radius: "0px — 날카로운 90도 모서리 필수"
shadow: "solid offset 20px #2C2C2C (no blur) / heavy 12px border #2C2C2C"
effects:
  editorial_shadow: "absolute div 2px solid #2C2C2C border, offset translate-x/y 16px behind main content"
  grayscale_hover: "filter: grayscale(100%)→grayscale(0%) 500ms ease-in-out"
  bg_watermark: "absolute bottom-0 right-0, Montserrat 900 25vw leading-0.8, white 8% opacity, pointer-events-none"
  marquee: "linear translate-x 0→-50% 40s infinite, Montserrat 18px white uppercase 0.2em"
  view_transition: "view-transition: same-origin"
animation:
  marquee: "40s linear infinite translate-x 0→-50%"
  hover: "grayscale→color 500ms ease-in-out"
layout: [sticky #BC2C2C nav (Montserrat black logo, 10px uppercase 0.15em links, cart badge white circle), full-bleed red hero (#BC2C2C bg, 25vw ghost text 8%, 9xl uppercase headline, blue+16px-shadow editorial image container), blue marquee ticker (2px charcoal borders 40s), 4col product grid (#F5F1E3, grayscale cards), 2-pane editorial (12px solid charcoal border split, serif headline L + watermark img R), dark #2C2C2C footer (7xl brand + #FCD758 labels)]
components:
  nav: "sticky #BC2C2C, Montserrat black logo, 10px uppercase 0.15em links, search+cart icons, cart badge white 8px text"
  hero: "full-bleed red, 25vw ghost 'STRIDE' 8%, Montserrat 9xl leading-0.85, blue container + 16px charcoal offset border, black CTA tracking-widest"
  ticker: "#5DA4C9 2px-charcoal borders, Montserrat 18px white uppercase 0.2em, 40s linear"
  product_grid: "4col #F5F1E3, white-bg cards light-gray border, grayscale→color hover, brand+price 10px meta"
  editorial: "12px charcoal border container, L 1/3 #F5F1E3 (serif headline + circle arrow), R 2/3 white (20% grayscale watermark + bottom-left 5xl headline)"
  footer: "#2C2C2C, L: 7xl brand + social, R: 3col links #FCD758 10px uppercase labels, border-top white/10"
special_notes:
  - "primary color 순수 hex 필수 — tinted 변형 금지"
  - "대형 헤드라인 line-height < 1.0 필수"
  - "rounded corners 금지 — 90도 각도 엄격 유지"
  - "모든 레이블·헤드라인 대문자 필수 — 본문 제외"
  - "soft shadow 금지 — solid offset만"
```
