# Minimalist Monochrome Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#FFFFFF", fg: "#000000", muted_bg: "#F5F5F5", muted_fg: "#525252", border: "#000000", border_light: "#E5E5E5" }
typography: { heading: "Playfair Display", body: "Source Serif 4", label: "JetBrains Mono", weight: "Playfair Display: elegant italic / Source Serif 4: readable / JetBrains Mono: dates/metadata", size_hero: "8xl–9xl (128–160px)", tracking: "-0.025em to -0.05em (headline) / 0.1em (small-caps labels) / 0 (body)" }
style_traits: [Austere Editorial Luxury, pure black+white only, serif typography as hero, oversized type scale, line-based visual system, 0px corners, dramatic negative space, inversion emphasis]
radius: "0px — 예외 없음"
shadow: "없음 — depth는 inversion/border weight/scale/negative space로만"
effects:
  h_lines: "repeating-linear-gradient(0deg, transparent 1px, #000 1px, #000 2px) bg-size 100% 4px, opacity 0.015"
  grid_pattern: "linear-gradient(#00000008 1px, transparent) + 90deg, 40px, opacity 0.015 (editorial sections)"
  diagonal_lines: "repeating-linear-gradient(45deg, transparent 40px, #00000008 40px, #00000008 42px) opacity 0.01"
  noise: "SVG fractalNoise overlay opacity 0.02 — paper-like quality"
  inversion: "black bg white text — accent 없이 drama 생성"
  inverted_stats: "vertical white lines bg, opacity 0.03"
  inverted_cta: "radial-gradient white circle-top opacity 0.05"
animation:
  timing: "0–100ms instant — no easing"
  hover: "full color inversion 100ms / image scale+grayscale-0 300ms"
layout: [strict 90-degree everywhere, line-based structure (hairline/thin/medium/thick/ultra borders), inversion sections for stats/CTA, dramatic negative space, section separators: thick 4px or ultra 8px rules]
components:
  buttons: "primary: black bg white text uppercase tracking-widest / outline: transparent 2px black border / ghost: text underline / hover: instant invert / focus-visible: 3px outline 3px offset"
  cards: "white bg black 1px border 0px radius, serif title, no shadow / hover: full invert 100ms"
  inputs: "2px black border (bottom only or full), no radius, placeholder #525252 italic / focus: border→4px no outline"
  nav: "hairline bottom border, serif or JetBrains Mono links, black pill CTA"
  hero: "9xl Playfair Display leading-none, word-scale fills viewport, thick rule + bordered square decorative element"
  stats: "inverted black bg, white text, vertical-lines texture"
  testimonials: "large italic serif 5xl+, oversized quotation marks, hover: quote opacity↑ border-t thickens"
  lines: "hairline 1px #E5E5E5 / thin 1px #000 / medium 2px / thick 4px / ultra 8px"
special_notes:
  - "순수 흑백만 — accent color 절대 금지"
  - "0px border-radius 예외 없음"
  - "drop shadow 없음"
  - "serif 타이포그래피 필수 — sans-serif 금지"
  - "gray는 secondary text/border only (#525252, #E5E5E5)"
  - "Minimalist Modern(Inter+blue+gradient)과 엄격히 구분"
  - "texture overlay 필수 — flat 방지"
  - "transition 100ms max — bouncy/slow animation 금지"
  - "hero 8xl+ 오버사이즈 타이포 필수"
  - "4px black horizontal rule 모든 major section 구분"
```

---

## Full Design System Prompt

<design-system>

### Design Philosophy

**Core Principle**: Reduction to Essence. Pure black (#000000) and white (#FFFFFF) only. No gradients, no shadows, no accent colors. Typography, scale, contrast, and negative space do all the work.

**Visual Vibe**: Austere, Authoritative, Timeless, Editorial — Vogue/Harper's Bazaar, luxury brand identities (Chanel, Celine), architectural monographs, gallery exhibition materials.

**NOT**: colorful/playful, soft/rounded/friendly, gradient-based, shadow-heavy, generic/template-like.

### Colors
```
background:       #FFFFFF
foreground:       #000000
muted:            #F5F5F5
mutedForeground:  #525252
accent:           #000000
accentForeground: #FFFFFF
border:           #000000
borderLight:      #E5E5E5
card:             #FFFFFF
ring:             #000000
```
Rule: No other colors. Ever.

### Typography
- Display/Headlines: "Playfair Display", Georgia, serif
- Body: "Source Serif 4", Georgia, serif
- Mono/Labels: "JetBrains Mono", monospace

Scale: xs(12px) → sm(14px) → base(16px) → lg(18px) → xl(20px) → 2xl(24px) → 3xl(32px) → 4xl(40px) → 5xl(56px) → 6xl(72px) → 7xl(96px) → 8xl(128px) → 9xl(160px)

Tracking: tracking-tight/-tighter (headlines) / tracking-normal (body) / tracking-widest (small caps/labels)
Leading: leading-none (1) for display / leading-relaxed (1.625) for body

### Border Radius
ALL VALUES: 0px — No exceptions.

### Borders & Lines
```
hairline:  1px solid #E5E5E5
thin:      1px solid #000000
medium:    2px solid #000000
thick:     4px solid #000000
ultra:     8px solid #000000
```

### Shadows: NONE
Depth via: color inversion / border weight variation / scale contrast / negative space

### Textures (REQUIRED — prevents flat design)
```css
/* Horizontal lines — global */
background-image: repeating-linear-gradient(0deg, transparent, transparent 1px, #000 1px, #000 2px);
background-size: 100% 4px; opacity: 0.015;

/* Grid — editorial sections */
background-image: linear-gradient(#00000008 1px, transparent 1px), linear-gradient(90deg, #00000008 1px, transparent 1px);
background-size: 40px 40px; opacity: 0.015;

/* Diagonal — process/timeline */
background-image: repeating-linear-gradient(45deg, transparent, transparent 40px, #00000008 40px, #00000008 42px);
opacity: 0.01;

/* Noise — paper quality */
background-image: url("data:image/svg+xml,...fractalNoise..."); opacity: 0.02;

/* Inverted vertical lines — stats section */
background-image: repeating-linear-gradient(90deg, transparent, transparent 1px, #fff 1px, #fff 2px);
background-size: 4px 100%; opacity: 0.03;

/* Inverted radial — final CTA */
background-image: radial-gradient(circle at top center, #ffffff, transparent 70%);
opacity: 0.05;
```

### Buttons
- Primary: bg-black text-white px-8 py-4 uppercase tracking-widest font-medium text-sm / hover: bg-white text-black border-2-black / transition: 0–100ms
- Outline: transparent bg, 2px solid black border / hover: fill black
- Ghost: transparent, text underline on hover
- Shape: Always rectangular (0px radius). Arrow (→) for CTAs.
- Focus: focus-visible:outline-3 focus-visible:outline-black focus-visible:outline-offset-3

### Cards
- Standard: bg-white border-1px-black p-6/p-8 no-shadow no-radius
- Inverted: bg-black text-white (use sparingly for emphasis)
- Hover: full color inversion 100ms

### Inputs
- border-2-black-bottom-only (or full), no radius
- placeholder: #525252 italic
- focus: border→4px, no outline ring

### Layout
- Container: max-w-6xl px-6 md:px-8 lg:px-12
- Sections: py-24 md:py-32 lg:py-40
- Between sections: 4px or 8px black horizontal rule

### Animation Philosophy: Minimal and Instant
- 0–100ms max. Binary on/off. No easing, no bounce, no parallax.
- Feature card hover: full color inversion 100ms
- Blog image hover: border 2px→4px + scale(1.05) + grayscale→0 300ms
- Testimonial hover: quote mark opacity↑, border-t thickens 100ms

### Bold Non-Negotiable Choices
1. Hero: at least one word 8xl+ (9xl on desktop)
2. Hero decorative: thick rule + small bordered square
3. Inverted Stats: black bg, white text, vertical line texture
4. No accent colors — black IS the accent
5. 4px black rules between ALL major sections
6. Testimonials: large italic serif, oversized quotation marks
7. Sharp 0px radius everywhere
8. 100ms max transitions
9. Typography as visual graphic element
10. Layered textures (NOT flat)
11. Boxed drop cap in Product Detail first paragraph
12. Pricing: highlighted tier extends vertically on desktop
13. Feature cards + pricing tiers invert on hover
14. Blog images: border thickens + scale on hover

### Accessibility
- Contrast: 21:1 (WCAG AAA)
- Focus: 3px solid black, 3px offset (focus-visible only)
- Touch targets: 44px minimum
- Skip links: visible black button at top

### Responsive
- 9xl → 5xl on mobile
- Stack columns vertically
- Borders → full-width horizontal rules
- Maintain monochrome drama on mobile

</design-system>
