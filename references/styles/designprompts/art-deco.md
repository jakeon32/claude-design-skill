# Art Deco Style (The "Gatsby" Aesthetic)
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#0A0A0A", fg: "#F2F0E4", card_bg: "#141414", gold: "#D4AF37", gold_light: "#F2E8C4", midnight_blue: "#1E3D59", muted: "#888888" }
typography: { heading: "Marcellus / Italiana", body: "Josefin Sans", weight: "Marcellus: 400 (inherently bold-looking) / Josefin Sans: 400 body / uppercase all display", size_hero: "6xl–7xl", tracking: "tracking-widest (headings+buttons) / tracking-[0.2em]", leading: "tight–normal (headings) / relaxed (body)" }
style_traits: [Great Gatsby opulence, 1920s machine-age geometry, obsidian black + metallic gold, sunburst radials, stepped zigzurat corners, diamond rotations, double-frame images, roman numerals, all-caps theatrical]
radius: "0px 엄격 — Art Deco is sharp edges. rounded-sm (2px) max 예외"
shadow: "glow only: box-shadow 0 0 15px rgba(212,175,55,0.2) — drop shadow 금지"
border: "gold border-[#D4AF37], default 30% opacity → hover 100%, thin 1px precise lines"
effects:
  diagonal_bg: "repeating-linear-gradient 45° + -45° gold lines 3–5% opacity — vintage crosshatch"
  diamond_icon: "rotate-45 container + -rotate-45 content inside — instant Art Deco"
  double_frame: "outer gold border + inner dark inset border = frame-within-frame"
  sunburst: "radial-gradient gold 10–20% opacity from hero focal point"
  stepped_corners: "L-bracket absolute pseudo-elements at opposite corners (border-t border-l + border-b border-r)"
  gold_glow: "0 0 15px rgba(212,175,55,0.2) → 0 0 20px rgba(212,175,55,0.4) on hover"
  section_divider: "h-px w-24 gold lines above + below headings (never full-width)"
  grain_texture: "noise overlay on background for vintage film quality"
animation:
  timing: "duration-300 standard / duration-500 theatrical / ease-out mechanical"
  hover: "cards: -translate-y-2 + border opacity → 100% + glow intensify"
  button: "bg flip + glow expansion 300ms"
  faq: "chevron rotate-180"
  lines: "width 0 → full on scroll-into-view"
layout: [max-w-6xl sections, max-w-5xl hero centered, py-32 generous breathing room, even column counts (2/3), centered symmetrical axis, gap-8 between cards]
components:
  nav: "gold border-b 1px, Josefin Sans uppercase tracking-widest, transparent gold-glow CTA"
  hero: "sunburst radial bg, Marcellus 6xl–7xl uppercase tracking-widest, centered symmetry, decorative gold divider lines"
  section_headings: "uppercase tracking-widest with h-px w-24 gold lines above+below, Marcellus"
  cards: "bg-[#141414] border border-[#D4AF37]/30 → hover border-[#D4AF37]/100, stepped corner L-brackets, -translate-y-2 hover"
  buttons: "default: transparent gold border+text → hover: gold bg black text glow / solid: gold bg black text"
  inputs: "border-b-2 border-[#D4AF37] bg-transparent, focus: lighter gold + bottom shadow glow"
  diamond_frames: "rotate-45 wrapper + -rotate-45 inner for icons/avatars"
  roman_numerals: "I II III IV instead of 1 2 3 4, Marcellus display font"
  images: "double-frame grayscale default → hover: color+gold-overlay"
  dividers: "vertical absolute w-px gold/30 lines for architectural height"
accessibility:
  contrast: "gold #D4AF37 on black #0A0A0A: ~7:1 AA ✓ / cream #F2F0E4 body: excellent / muted #888888: ~4.5:1 secondary"
  focus: "ring-2 ring-[#D4AF37] ring-offset-2 ring-offset-black"
  touch: "h-12 (48px) minimum buttons"
  aria: "decorative corners/dividers aria-hidden=true"
special_notes:
  - "0px radius 철저 — rounded-sm (2px) 최대"
  - "drop shadow 금지 — gold glow (0 0 15px rgba) 사용"
  - "pure black #000 아닌 obsidian #0A0A0A"
  - "gold large area 금지 — border/hover/accent sparingly"
  - "diamond rotation 필수 — rotate-45 wrapper + -rotate-45 inner"
  - "roman numerals 필수 — 1,2,3 사용 금지"
  - "모든 display uppercase + tracking-widest"
  - "double-frame 이미지 — plain img 금지"
  - "sunburst radial-gradient hero 필수"
  - "diagonal crosshatch bg pattern 필수 (5% opacity)"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Opulence, mathematical precision, architectural grandeur.** The Great Gatsby meets Fritz Lang's Metropolis — champagne towers in skyscraper ballrooms, chrome elevator grilles, sunburst marquees. **Maximalist restraint** — every element is intentional, ornamental, yet precisely placed.

**Core Principles:**
1. **Geometry as Decoration:** Triangles, chevrons, ziggurat shapes, sunbursts, fan motifs. Borders are multi-layered frames.
2. **Extreme Tonal Contrast:** Obsidian black vs metallic gold. No muddy middle ground.
3. **Symmetry:** Content radiates from centerlines. Ceremonial, like a grand hotel entrance.
4. **Verticality:** Vertical lines + stacked elements reach skyward like skyscrapers.
5. **Material Luxury:** Polished brass, etched glass, lacquered surfaces — simulated through glows and metallic sheens.
6. **Theatricality:** Announces, never whispers. All-caps, wide tracking, imposing scale.

**Emotional Resonance:** Confidence, Heritage, Exclusivity, Sophistication. For luxury brands, premium services, cultural institutions.

### Colors
```
background:  #0A0A0A  (Obsidian Black — never pure #000)
foreground:  #F2F0E4  (Champagne Cream — warm, readable)
card-bg:     #141414  (Rich Charcoal — depth against bg)
gold:        #D4AF37  (Metallic Gold — core luxury element)
gold-light:  #F2E8C4  (Hover gold — brighter)
midnight:    #1E3D59  (Midnight Blue — depth, inactive)
muted:       #888888  (Pewter — secondary text)
```
Gold is used sparingly but decisively — borders, headings, accents, hover states. Never for large fill areas.

### Typography
- **Display:** `"Marcellus"` or `"Italiana"` (Roman serif with Art Deco flair)
- **Body/UI:** `"Josefin Sans"` (geometric, vintage-feel sans)
- **H1:** `text-6xl md:text-7xl` UPPERCASE `tracking-widest leading-tight`
- **Body:** `text-lg leading-relaxed`
- **Labels/Buttons:** UPPERCASE `tracking-[0.2em]` Josefin Sans
- **Numbers:** Roman numerals (I, II, III, IV) in Marcellus — never Arabic numerals for lists/steps

### Radius & Borders
- **Radius: 0px. No exceptions. Max `rounded-sm` (2px) only if absolutely necessary.**
- Border: `1px` or `2px` gold `#D4AF37`
- Default opacity: 30% → hover: 100%
- Double-frame pattern: outer gold border + inner dark inset = frame-within-frame

### Shadows — Gold Glow Only
```css
/* Standard glow */
box-shadow: 0 0 15px rgba(212,175,55,0.2);
/* Hover glow (intensified) */
box-shadow: 0 0 20px rgba(212,175,55,0.4);
/* Input focus underline shadow */
box-shadow: 0 4px 10px rgba(212,175,55,0.2);
```
No drop shadows. No hard offsets. Only soft gold halos.

### Textures & Patterns (Required)
```css
/* Diagonal crosshatch background — vintage print quality */
background-image:
  repeating-linear-gradient(45deg, rgba(212,175,55,0.03) 0px, rgba(212,175,55,0.03) 1px, transparent 1px, transparent 10px),
  repeating-linear-gradient(-45deg, rgba(212,175,55,0.03) 0px, rgba(212,175,55,0.03) 1px, transparent 1px, transparent 10px);

/* Sunburst radial — hero focal point */
background: radial-gradient(ellipse at center, rgba(212,175,55,0.15) 0%, transparent 70%);

/* Grain noise overlay — vintage film quality */
/* SVG fractalNoise, opacity: 0.03, fixed position */
```

### Buttons
- **Default:** `bg-transparent border-2 border-[#D4AF37] text-[#D4AF37] rounded-none uppercase tracking-widest`
  hover: `bg-[#D4AF37] text-black shadow-[0_0_20px_rgba(212,175,55,0.4)]`
- **Solid:** `bg-[#D4AF37] text-black rounded-none uppercase tracking-widest`
  hover: `bg-[#F2E8C4]` (brightness shift)
- **Outline Thin:** `border border-[#D4AF37]/50 text-[#D4AF37]`
  hover: `bg-[#1E3D59] border-[#1E3D59]`
- All: `transition-all duration-300`, `h-12` minimum, 0px radius

### Cards
- `bg-[#141414] border border-[#D4AF37]/30 p-8 rounded-none`
- hover: `border-[#D4AF37]/100 -translate-y-2 shadow-[0_0_20px_rgba(212,175,55,0.2)]` `duration-500`
- **Stepped corner L-brackets:**
```css
/* Top-right corner */
.card::before { position: absolute; top: 8px; right: 8px; width: 16px; height: 16px;
  border-top: 2px solid #D4AF37; border-right: 2px solid #D4AF37; }
/* Bottom-left corner */
.card::after { position: absolute; bottom: 8px; left: 8px; width: 16px; height: 16px;
  border-bottom: 2px solid #D4AF37; border-left: 2px solid #D4AF37; }
```

### Inputs
- `border-b-2 border-[#D4AF37] bg-transparent h-12 px-3 py-2 rounded-none`
- Text: `text-[#F2F0E4]` placeholder: `text-[#888888]`
- Focus: `border-[#F2E8C4] shadow-[0_4px_10px_rgba(212,175,55,0.2)]` — no ring
- Label: uppercase `text-xs text-[#D4AF37] tracking-widest`

### Diamond Icon Containers
```jsx
<div className="rotate-45 h-16 w-16 border border-[#D4AF37]/50 flex items-center justify-center">
  <div className="-rotate-45 text-[#D4AF37]">
    <Icon />
  </div>
</div>
```

### Section Headings (Mandatory Pattern)
```jsx
<div className="text-center">
  {/* Decorative lines above */}
  <div className="flex items-center justify-center gap-4 mb-4">
    <div className="h-px w-24 bg-[#D4AF37]" />
    <span className="text-[#D4AF37] text-xs uppercase tracking-widest">Section Label</span>
    <div className="h-px w-24 bg-[#D4AF37]" />
  </div>
  <h2 className="font-['Marcellus'] text-5xl lg:text-6xl uppercase tracking-widest text-[#F2F0E4]">
    Heading
  </h2>
  <div className="h-px w-24 bg-[#D4AF37] mx-auto mt-4" />
</div>
```

### Double-Frame Images
```jsx
<div className="border-2 border-[#D4AF37]/50 p-1">
  <div className="border border-[#0A0A0A] p-1">
    <img className="grayscale hover:grayscale-0 transition-all duration-500 scale-100 hover:scale-105" />
  </div>
</div>
```

### Layout
- Container: `max-w-6xl mx-auto` (hero: `max-w-5xl` centered)
- Section: `py-32` — generous breathing room
- Cards: `p-8`, `gap-8`
- Alignment: Centered symmetry for hero/headings, precise columns for grids
- Even column counts: 2 or 3 (never 5 in feature grids)

### Non-Negotiable Bold Choices
1. **Diagonal crosshatch bg:** 45° gold lines at 3–5% opacity across entire page
2. **Diamond icon containers:** `rotate-45` + `-rotate-45` inner — mandatory
3. **Roman numerals:** I, II, III for all steps and tiers
4. **Stepped corner brackets:** Absolute L-shapes on cards (opposite corners)
5. **Double-frame images:** Two-border frame wrapper always
6. **Sunburst radial in hero:** `radial-gradient` gold glow from focal point
7. **Balanced decorative gold lines:** `h-px w-24` lines flanking headings
8. **Theatrical transition speed:** `duration-500` for cards — deliberate, mechanical
9. **Glow > shadows everywhere**

### Animation
- `duration-300 ease-out` standard, `duration-500 ease-in-out` theatrical
- Cards: `-translate-y-2` + glow intensify
- Buttons: bg flip + glow expand
- Gold lines: animate width `0 → full` on scroll-into-view
- FAQ: chevron `rotate-180` on open
- Icon diamonds: can `rotate-0` from `rotate-45` on hover
- No bounce, no spring — mechanical precision

### Accessibility
- `#D4AF37` on `#0A0A0A`: ~7:1 AA ✓
- `#F2F0E4` on `#0A0A0A`: ~13:1 AAA ✓
- `#888888` on `#0A0A0A`: ~4.5:1 AA ✓ (secondary only)
- Focus: `ring-2 ring-[#D4AF37] ring-offset-2 ring-offset-black`
- Decorative elements: `aria-hidden="true"`
- `h-12` (48px) minimum button height

</design-system>
