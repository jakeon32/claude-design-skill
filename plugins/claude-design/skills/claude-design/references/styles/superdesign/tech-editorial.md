# Tech Editorial Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#f7f6f2", fg: "#1c1c1c", forest: "#3d7068", border: "#e5e4de", muted: "#B4B4B4", scan_blue: "#3b82f6" }
typography: { heading: "Playfair Display", label: "Space Mono", body: "Space Grotesk", weight: "Playfair Display: light tight-tracking / Space Mono: uppercase 0.2–0.3em / Space Grotesk: readable", size_hero: "9vw", tracking: "0.2–0.4em (mono) / tight (serif)" }
style_traits: [Editorial Tech, fixed 40px grid bg radial mask, high-contrast serif, 1px borders no-shadow, word-reveal scroll, 4-column vertical guides]
radius: "2px max — 날카로운 모서리 유지"
shadow: "금지 — 1px border 구분만"
effects:
  bg_grid: "fixed 40px square grid #e5e4de, radial transparency mask (40% center→0% edge)"
  vertical_guides: "fixed 1px #e5e4de lines at 25% 50% 75% width"
  nav_scroll: "floating top → fixed bottom-border #f7f6f2/80 backdrop-blur on scroll"
  scan_line: "2px container #e5e4de bg, #3b82f6 line -100%→100% 2s infinite cubic-bezier(0.8,0,0.2,1)"
  cta_hover: "tracking 0.2em→0.4em + white/20% overlay slide-up from bottom"
  word_reveal: "IntersectionObserver — span opacity 0.15→1.0 as scroll activates each word"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1) 700–1000ms"
  reveal: "translateY(20px)→0 + opacity 0→1"
  step_expand: "inactive steps opacity→0.4, active step expands description"
layout: [fixed bg grid + guides, max-w-7xl fixed-to-floating nav (mono 10px 0.3em), 9vw serif uppercase hero (italic muted key words, forest CTA), 3col stat grid (1px dividers, 48px bordered icon, serif 4xl number), word-reveal section (serif 3xl–6xl scroll-sync opacity), 2col workflow accordion (mono steps 01–03 + sticky card grayscale img), tab switcher (giant ghost icon bg, 3col benefit grid), 2col contact form (serif heading + bottom-border inputs)]
components:
  nav: "floating → fixed scroll, brand: '|—SUPERDESIGN—|' bars, Space Mono 10px 0.3em links"
  hero: "9vw serif light uppercase, italic #B4B4B4 accent words, pulse-dot badge, forest CTA mono"
  stat_grid: "3col 1px-dividers, 40px padding, 48px bordered icon box, serif 4xl + mono uppercase label, white hover"
  word_reveal: "serif 3xl–6xl, JS scroll-sync opacity 0.15→1.0 per span"
  workflow: "2col — mono 01/02/03 expand L (inactive 0.4) / sticky card grayscale multiply + scan-line progress R"
  tab_switcher: "pill tabs centered, bordered card, 240px ghost icon 5%, 3col benefit grid"
  form: "serif 'Request Access', bottom-border-only inputs mono placeholder 10px, full-width forest btn"
special_notes:
  - "#f7f6f2 배경 필수 — clinical white 금지"
  - "1px border 구분 — shadow 금지"
  - "Space Mono 모든 메타데이터·숫자 데이터 필수"
  - "rounded corners 2px 초과 금지"
  - "vivid gradient 금지 — solid fill + opacity transition만"
```
