# Newsprint Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#F9F9F7", fg: "#111111", muted: "#E5E5E0", red: "#CC0000", neutral_400: "#A3A3A3", neutral_500: "#737373", neutral_600: "#525252" }
typography: { heading: "Playfair Display", body: "Lora", label: "Inter / JetBrains Mono", weight: "Playfair: black/bold headlines / Lora: 400 body / Inter: UI labels buttons / JetBrains Mono: dates stats metadata", size_hero: "5xl→6xl→9xl (80–128px)", leading: "0.9 leading-none (hero) / relaxed 1.625 (body)", tracking: "tighter (hero headlines) / widest uppercase (labels metadata)" }
style_traits: [Newsprint Editorial Authority, ink-on-paper high contrast, 0px everywhere, collapsed grid borders, massive serif hierarchy, dot/line texture patterns, hard offset hover shadow, editorial red sparingly]
radius: "0px — 절대 원칙"
shadow: "flat design — hard offset hover only: 4px 4px 0px 0px #111111 + translate(-2px,-2px)"
effects:
  dot_bg: "SVG 4x4px dot pattern fill-opacity 0.04 — main background"
  line_grid: "::before linear-gradient 3px×3px 98% transparent + 2% rgba(0,0,0,0.02) — section texture"
  radial_dots: "bg radial-gradient #000 1px, 16px bg-size, opacity 10% — image placeholders"
  hard_shadow_hover: "box-shadow: 4px 4px 0px 0px #111111 + transform: translate(-2px,-2px)"
  editorial_red: "#CC0000 only for breaking news badges / CTA / hover states — 99% black/white"
  collapsed_grid: "adjacent elements share 1px borders — no double lines"
animation:
  timing: "instant or 150ms — no elaborate easing"
  hover: "hard offset shadow + translate(-2px,-2px)"
layout: [max-w-7xl collapsed border grid, 4px section dividers, newspaper column layouts dense information, visible structural borders celebrated, py-16–py-24 sections]
components:
  nav: "4px bottom border #111111, Inter uppercase tracking-widest, red accent CTA"
  hero: "9xl PD leading-0.9 tracking-tighter, 4px left-border editorial column, red BREAKING badge"
  article_cards: "0px radius 1px borders, PD bold title, Lora body, Inter xs metadata mono, hard-shadow hover"
  grid: "collapsed shared borders, explicit column divisions, newspaper layout"
  labels: "Inter/JetBrains Mono xs uppercase tracking-widest — dates/editions/metadata"
  section_dividers: "4px solid #111111 major / 1px secondary"
  image_placeholder: "radial dot pattern bg-size 16px opacity 10%"
special_notes:
  - "0px border-radius 절대 원칙"
  - "soft shadow 금지 — flat design"
  - "#CC0000 red 극소량만 — 99% black/white"
  - "4개 serif stack: PD (headlines) + Lora (body) + Inter (UI) + JetBrains Mono (data)"
  - "dot/line texture 필수 — flat bg 방지"
  - "collapsed grid borders — double-line 방지"
  - "고정 newspaper column feel — generous padding 금지"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality.
</role>

<design-system>

### Design Philosophy
**"All the News That's Fit to Print."** Golden age print journalism, reimagined for the web. Absolute clarity, hierarchy, and structure through high-contrast typography, grid-based layouts, and sharp geometric precision.

**Core DNA:**
- **Stark Geometry**: Zero border radius everywhere. Perfect rectangles.
- **High Information Density**: Tight padding, collapsed grid borders, newspaper column layouts.
- **Typographic Drama**: Massive serif headlines (up to 9xl) paired with small legible body text.
- **Visible Structure**: Grid lines celebrated — borders between columns/sections are explicit.
- **Paper Texture**: Subtle grain overlays simulate newsprint quality.

### Colors
```
background:   #F9F9F7  (Newsprint Off-White — warm, not pure white)
foreground:   #111111  (Ink Black — very deep, not pure black)
muted:        #E5E5E0  (Divider Grey)
accent-red:   #CC0000  (Editorial Red — used EXTREMELY sparingly)
border:       #111111
neutral-100:  #F5F5F5  (hover backgrounds)
neutral-400:  #A3A3A3  (muted text in dark sections)
neutral-500:  #737373  (metadata, captions)
neutral-600:  #525252  (body text variations)
```
Rule: 99% black and white. Red only for breaking news badges, CTAs, hover states.

### Typography
- **Serif Headlines:** Playfair Display (high-contrast, authoritative)
- **Serif Body:** Lora (highly legible for long-form)
- **Sans UI:** Inter (labels, buttons, navigation, metadata)
- **Mono Data:** JetBrains Mono (stats, dates, edition numbers)

Scale:
- Hero H1: `text-5xl sm:text-6xl lg:text-9xl` — `leading-[0.9] tracking-tighter`
- H2: `text-4xl lg:text-5xl font-black`
- H3: `text-2xl lg:text-3xl font-bold`
- Body: `text-sm` to `text-lg` Lora `leading-relaxed`
- Labels: `text-xs uppercase tracking-widest font-mono`

### Radius & Borders
- **Radius: 0px everywhere. No exceptions.**
- `.sharp-corners { border-radius: 0px !important; }`
- Standard: `1px` solid `#111111`
- Heavy dividers: `border-b-4` or `border-4` (4px)
- Collapsed grids: adjacent cells share borders — no double lines

### Shadows
**Flat design. No soft drop shadows.**
- Hover hard offset: `box-shadow: 4px 4px 0px 0px #111111` + `transform: translate(-2px,-2px)`
- `.hard-shadow-hover:hover { box-shadow: 4px 4px 0px 0px #111111; transform: translate(-2px,-2px); }`

### Textures (Required — prevents flat design)
```css
/* 1. Dot Grid Background */
background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4'%3E%3Cpath fill='%23111111' fill-opacity='0.04' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E")

/* 2. Line Grid Section Texture */
.newsprint-texture::before {
  background-image: linear-gradient(0deg, transparent 98%, rgba(0,0,0,0.02) 100%),
                    linear-gradient(90deg, transparent 98%, rgba(0,0,0,0.02) 100%);
  background-size: 3px 3px; opacity: 0.5;
}

/* 3. Halftone Image Placeholders */
bg-[radial-gradient(#000_1px,transparent_1px)] opacity-10 [background-size:16px_16px]
```

### Buttons
- **Primary:** `bg-[#111111] text-[#F9F9F7]` → hover: `bg-white text-[#111111] border-[#111111]`
- **Secondary:** `border border-[#111111] bg-transparent` → hover: `bg-[#111111] text-[#F9F9F7]`
- **Ghost:** no border → hover: `bg-[#E5E5E0]`
- **Link:** `text-[#111111]` → hover: `underline decoration-2 decoration-[#CC0000]`
- All: `uppercase tracking-widest transition-all duration-200` — 44px min touch target

### Cards
- `border border-[#111111] bg-[#F9F9F7] p-6` — 0px radius enforced
- Hover: `hover:bg-neutral-100` + optional `.hard-shadow-hover`
- Collapsed grid: `border-r` on all-but-last, `border-b` on all rows

### Inputs
- `border-b-2 border-[#111111] bg-transparent px-3 py-2 font-mono text-sm`
- Focus: `bg-[#F0F0F0]` — no ring, no outline
- `border-radius: 0px` inline enforced

### Layout
- Container: `max-w-screen-xl` (1280px) centered
- Grid: 12-column `grid-cols-12`, col-span for editorial asymmetry (8/4, 5/7 splits)
- Collapsed borders: `border-l border-t` on container + `border-r border-b` on children
- Section padding: `py-16` standard, `p-6`–`p-8` cards
- High density: tighter than typical web design

### Non-Negotiable Bold Choices
1. **Vertical Grid Dividers:** `border-r` creates strict newspaper columns
2. **Drop Caps:** `text-7xl float-left` on first letter of key paragraphs
3. **Marquee Ticker:** Horizontal scrolling stats — black bg, white text, red badges
4. **Edition Metadata:** "Vol. 1 | [Date] | Edition" in header/footer
5. **Justified Text:** `text-justify` for multi-column body
6. **Grayscale Images:** `grayscale` default → `sepia-[50%]` on hover
7. **Asymmetric Layouts:** 8/4 or 5/7 column splits — never 50/50
8. **Uppercase Labels:** `uppercase tracking-widest text-xs font-mono` everywhere
9. **Inverted Sections:** At least one section black bg + white text, red numbered steps
10. **Ornamental Dividers:** `&#x2727; &#x2727; &#x2727;` between major sections

### Animation
Fast, snappy, mechanical — no bounce or organic easing.
- `transition-all duration-200 ease-out`
- Hover: color inversion, hard shadow + translate, red underlines
- Accordion: `grid-rows-[0fr]→[1fr]` + `opacity-0→1` over 300ms
- FAQ icon: rotate 45° when open
- Blog images: `scale-105` on hover
- Nav links: turn red on hover

### Responsive
- Mobile < 768px: single column, remove `border-r`, keep `border-b`
- Typography: scales down (`text-9xl` → `text-5xl` on mobile)
- Padding reduces one step
- Preserve: 0px radius, high contrast, grid separators, uppercase labels

### Accessibility
- `#111111` on `#F9F9F7`: >17:1 AAA ✓
- `#CC0000` on `#F9F9F7`: >5:1 AA ✓ — never red on black
- Focus: `focus-visible:ring-2 focus-visible:ring-neutral-950 focus-visible:ring-offset-2`
- 44px minimum touch targets

</design-system>
