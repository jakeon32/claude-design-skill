# Neo-Brutalism Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#FFFDF5", fg: "#000000", accent: "#FF6B6B", secondary: "#FFD93D", muted: "#C4B5FD", white: "#FFFFFF" }
typography: { heading: "Space Grotesk", body: "Space Grotesk", weight: "900 black (all headings) / 700 bold (body+buttons) — light weights forbidden", size_hero: "8xl–9xl (96–128px)", tracking: "tighter–tight (headlines) / widest (labels)", leading: "none/0.85 (display) / snug-relaxed (body)" }
style_traits: [Digital punk anti-corporate, Y2K zine energy, hard black borders border-4 everywhere, offset solid shadows 0 blur, sticker layering rotated elements, mechanical button click, card physical lift, halftone/grid/noise textures]
radius: "0px default — rounded-full ONLY for pill badges/circles. Never rounded-md/lg."
shadow: "hard offset 0-blur — small:4px_4px / medium:8px_8px / large:12px_12px / massive:16px_16px — all #000"
border: "border-4 border-black 기본 — border-2 ghost only / border-8 major dividers"
effects:
  text_stroke: "-webkit-text-stroke: 2px black + color: transparent — massive hollow headlines"
  halftone: "radial-gradient(#000 1.5px, transparent 1.5px) 20px 20px"
  grid_pattern: "linear-gradient rgba(0,0,0,0.1) 1px 40px — graph paper"
  noise_texture: "SVG fractalNoise baseFrequency 0.65 numOctaves 3"
  radial_dots: "radial-gradient(circle, #000 2px, transparent 2.5px) 30px 30px"
animation:
  timing: "duration-100 buttons / duration-200 cards / ease-linear or ease-out"
  button_press: "active:translate-x-[2px] active:translate-y-[2px] active:shadow-none — mechanical click"
  card_lift: "hover:-translate-y-2 hover:shadow-[16px_16px_0px_0px_#000]"
  badge_rotate: "hover:rotate-12"
  spin_slow: "@keyframes spin-slow 10s linear infinite — decorative stars"
  bounce: "animate-bounce on attention badges"
layout: [max-w-7xl py-16–py-32, sticker rotations (rotate-1/-rotate-2/rotate-3) on containers+text, marquee trust indicators + testimonials, overlapping absolute floats, color blocking sections, 60/40 asymmetric splits]
components:
  nav: "border-4 border-black logo, uppercase bold links, hover:bg-accent+border+shadow snap"
  hero: "Space Grotesk 8xl–9xl text-stroke hollow + solid overlay, stacked badge visual chaos zone, accent section bg"
  marquee: "react-fast-marquee trust bar + testimonial carousel + section dividers"
  buttons: "h-12–h-14 rounded-none border-4 black shadow-[4px_4px_0px_0px_#000], active:translate press"
  cards: "bg-white border-4 border-black shadow-[8px_8px_0px_0px_#000], hover:-translate-y-2 grow shadow"
  inputs: "border-4 border-black h-14–h-20 font-bold text-xl, focus:bg-secondary + shadow, no ring"
  badges: "rounded-full border-4 black bg-accent/secondary, absolute rotate-3, font-black uppercase"
  icons: "stroke-[3–4px] h-8–h-12, inside border-4 black bg-accent p-4 box"
  color_blocks: "red accent / yellow secondary / violet muted / black / cream alternating sections"
special_notes:
  - "border-4 border-black 모든 요소에 필수 — 없으면 존재하지 않는 것"
  - "subtle gray 절대 금지 — #000 또는 색상만"
  - "blur/backdrop-blur 금지 — 모든 shadow는 hard 0-blur"
  - "rounded-md/lg/xl 금지 — 0px 또는 rounded-full만"
  - "button active:translate press 필수 — mechanical click feel"
  - "텍스처 필수 — 배경 flat 금지 (halftone/grid/noise)"
  - "rotation 필수 — rotate-1/-rotate-2 sticker effect"
  - "font-light/400 forbidden — 700 minimum"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Digital punk rebellion against "Corporate Memphis" and polished SaaS.** Neo-brutalism combines raw structural honesty with Pop Art energy, sticker culture, and DIY zine spirit. It demands to be seen — structure enforced with thick hard-edged black lines, shadows as solid ink blocks.

**Core DNA:**
1. **Unapologetic Visibility:** `border-4` everywhere. Hard offset shadows, zero blur. Every element has visual weight.
2. **Digital Tactility:** Screen as collage board. Elements feel like physical stickers. Buttons click down mechanically. Cards lift physically.
3. **Organized Chaos:** Slight rotations, intentional overlaps, asymmetric layouts — planned messiness.
4. **Raw & Default:** Pure black for ALL borders/text. High-saturation primary colors. Cream background mimics aged newsprint.
5. **Mechanical Interactivity:** Buttons snap, don't fade. Fast transitions (`duration-100`).

**Vibe:** Y2K punk zine + early web forum + rave poster energy. Loud, retro-modern, anti-corporate, confident.

### Colors
```
background: #FFFDF5  (Cream — aged newsprint, never pure white)
foreground: #000000  (Pure Black — ALL borders, text, shadows)
accent:     #FF6B6B  (Hot Red — primary CTA, important badges)
secondary:  #FFD93D  (Vivid Yellow — secondary buttons, focus states)
muted:      #C4B5FD  (Soft Violet — tertiary, FAQ, subtle bg)
white:      #FFFFFF  (contrast on dark backgrounds)
```
**Rules:** No subtle grays. No `#333` or `#666`. It's black or a color. Color blocking creates section rhythm.

### Typography (Space Grotesk)
- **Font:** `"Space Grotesk"` — geometric, quirky, bold enough for 900 weight
- **Weights:** 900 (all headings) and 700 (body/buttons) ONLY. Regular/400 forbidden.

| Role | Size | Notes |
|:-----|:-----|:------|
| Hero display | `text-8xl md:text-9xl` | `font-black leading-none tracking-tighter` |
| Section H2 | `text-6xl md:text-8xl` | `font-black uppercase` |
| H3 | `text-4xl md:text-5xl` | `font-black` |
| Body large | `text-2xl md:text-3xl` | `font-bold` |
| Body | `text-lg md:text-xl` | `font-bold` |
| Labels | `text-sm` | `font-bold uppercase tracking-widest` |

**Text stroke display technique:**
```css
-webkit-text-stroke: 2px #000;
color: transparent;
/* Overlay solid version for depth */
```

### Radius & Borders
- **Radius: 0px (sharp). ONLY `rounded-full` for pill badges/circles.**
- Never `rounded-md`, `rounded-lg`, `rounded-xl`.
- **Borders: `border-4 border-black` default on ALL elements**
- Thin: `border-2` for ghost buttons only
- Thick: `border-8` for major dividers/hero

### Shadows (Hard Offset — Zero Blur — Always #000)
```css
Small:   shadow-[4px_4px_0px_0px_#000]   /* buttons, small elements */
Medium:  shadow-[8px_8px_0px_0px_#000]   /* standard cards */
Large:   shadow-[12px_12px_0px_0px_#000] /* featured cards */
Massive: shadow-[16px_16px_0px_0px_#000] /* hover state, hero elements */
White:   shadow-[20px_20px_0px_0px_#fff] /* elements on black backgrounds */
```

### Textures (Required — Never Flat Backgrounds)
```css
/* Halftone dots */
background-image: radial-gradient(#000 1.5px, transparent 1.5px);
background-size: 20px 20px;

/* Graph paper grid */
background-image: linear-gradient(rgba(0,0,0,0.1) 1px, transparent 1px),
                  linear-gradient(90deg, rgba(0,0,0,0.1) 1px, transparent 1px);
background-size: 40px 40px;

/* SVG noise */
/* fractalNoise baseFrequency=0.65 numOctaves=3 */

/* Radial dots */
background-image: radial-gradient(circle, #000 2px, transparent 2.5px);
background-size: 30px 30px;
```

### Buttons
- `rounded-none border-4 border-black h-12 md:h-14 font-bold uppercase tracking-wide`
- **Primary:** `bg-[#FF6B6B]` + `shadow-[4px_4px_0px_0px_#000]`
- **Secondary:** `bg-[#FFD93D] text-black`
- **Outline:** `bg-white border-4 border-black`
- **MANDATORY press effect:**
  ```
  active:translate-x-[2px] active:translate-y-[2px] active:shadow-none
  ```
  This is the most important Neo-brutalism interaction — mechanical button click.
- Hover: `duration-100` fast background darken

### Cards
- `bg-white border-4 border-black rounded-none shadow-[8px_8px_0px_0px_#000] p-8`
- **Hover lift:**
  ```
  hover:-translate-y-2 hover:shadow-[16px_16px_0px_0px_#000] duration-200
  ```
- Card headers: colored bg (`bg-[#C4B5FD]/20` or `bg-[#FFD93D]`) + `border-b-4 border-black`

### Inputs
- `border-4 border-black rounded-none h-14 md:h-20 bg-white font-bold text-xl`
- Placeholder: `placeholder:text-black/40 font-bold uppercase`
- **Focus:** `focus-visible:bg-[#FFD93D] focus-visible:shadow-[4px_4px_0px_0px_#000] focus-visible:outline-none focus-visible:ring-0`
- No soft glow rings — yellow bg + hard shadow on focus

### Badges
- `rounded-full border-4 border-black bg-[#FF6B6B] or bg-[#FFD93D]`
- `font-black text-sm uppercase tracking-widest`
- Position: `absolute -top-4 -right-4 rotate-3`
- hover: `hover:rotate-12 duration-200`

### Icons (lucide-react)
- `stroke-[3px]` to `stroke-[4px]` — thick, bold
- Size: `h-8 w-8` to `h-12 w-12`
- Inside: `border-4 border-black bg-[#FF6B6B] p-4 rounded-none`

### Layout & Sticker Effect
- Container: `max-w-7xl mx-auto`
- Section padding: `py-16 md:py-32`
- **Rotation (mandatory for sticker feel):**
  - Text blocks: `rotate-1`, `-rotate-2`, `rotate-3`
  - Badges: `rotate-3`, `rotate-6`
  - Headlines: `inline-block -rotate-1` on key words
- Asymmetric: 60/40 splits, staggered grids — no perfect 50/50
- Overlapping: Absolute floaters, decorative shapes, background large numbers

### Non-Negotiable Bold Choices
1. **border-4 border-black on every visual element** — if no border, it doesn't exist
2. **Hard 0-blur shadows** — `shadow-[8px_8px_0px_0px_#000]` on all cards
3. **Mechanical button press** — `active:translate + active:shadow-none`
4. **Physical card lift** — `hover:-translate-y-2 + shadow-grows`
5. **Sticker rotations** — `rotate-1/-rotate-2/rotate-3` on containers/text
6. **Text stroke hollow** — `-webkit-text-stroke: 2px` on hero headline
7. **Color blocking sections** — red / yellow / violet / black / cream alternating
8. **Texture every background** — halftone or grid pattern always
9. **Star decorative elements** — slow spin `animate-spin-slow` 10s
10. **Marquee dividers** — trust bar + testimonial marquee

### Anti-Patterns
- Blur or `backdrop-blur` → hard shadows only
- Opacity/transparency on backgrounds → solid colors
- `bg-gradient-to-r` smooth → hard color stops
- `rounded-md/lg/xl` → `rounded-none` or `rounded-full` only
- Subtle grays `#333/#666` → pure `#000` or a color
- Slow `ease-in-out` → `ease-linear` or `ease-out` fast
- Large empty whitespace → fill with texture/pattern/decoratives
- font-400/light → 700 minimum

### Animation
```css
/* Buttons */
transition-all duration-100 ease-linear
active:translate-x-[2px] active:translate-y-[2px] active:shadow-none

/* Cards */
transition-all duration-200 ease-out
hover:-translate-y-2 hover:shadow-[16px_16px_0px_0px_#000]

/* Decorative stars */
@keyframes spin-slow { to { transform: rotate(360deg); } }
animation: spin-slow 10s linear infinite;

/* Attention badges */
animate-bounce
```

### Responsive
- Mobile: `text-4xl sm:text-6xl md:text-8xl` hero scaling
- Shadows: `shadow-[6px_6px_0px_0px_#000] sm:shadow-[8px_8px_0px_0px_#000]`
- Buttons: `w-full sm:w-auto`
- Grids: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- Keep thick borders + hard shadows + bold type on mobile — never go generic
- Touch targets: `h-14` minimum

### Accessibility
- `#000000` on `#FFFDF5`: 19:1 AAA ✓
- `#000000` on `#FFD93D`: 15:1 AAA ✓
- `#FFFFFF` on `#FF6B6B`: 4.6:1 AA ✓
- Focus: `focus-visible:ring-2 focus-visible:ring-black focus-visible:ring-offset-2` or yellow bg change
- `prefers-reduced-motion`: disable `animate-spin-slow`, `animate-bounce`, `animate-pulse`
- Semantic HTML: `<button>`, `<nav>`, `<header>`, `<main>`
- Touch targets: 44px minimum (`h-12` or `h-14`)

</design-system>
