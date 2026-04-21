# Academia / Classical Design System
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#1C1714", bg_alt: "#251E19", fg: "#E8DFD4", muted: "#3D332B", muted_fg: "#9C8B7A", accent: "#C9A962", accent_secondary: "#8B2635", border: "#4A3F35", accent_fg: "#1C1714" }
typography: { heading: "Cormorant Garamond (serif, calligraphic)", body: "Crimson Pro (serif, book-style)", display: "Cinzel (engraved all-caps, labels/buttons)", weight: "400-500 headings (let serif do the work) / 400 body / 500-600 Cinzel labels — italic emphasis over bold", size_display: "text-5xl–text-7xl (48-72px)", tracking: "tracking-tight headings / tracking-[0.2em]–tracking-[0.3em] Cinzel labels", leading: "leading-[1.1] display / leading-relaxed 1.625 body" }
style_traits: [19세기 대학 도서관 물질 현실감, 마호가니 목재+골동품 양피지+광택 황동+진홍 가죽, 엄격한 타이포 계층, 세피아 사진→컬러 전환, 건축적 서명 요소]
radius: { default: "4px (rounded)", arch_top: "40% 40% 0 0 / 20% 20% 0 0 — cathedral arch, hero/feature images 필수", circle: "rounded-full (icons/badges/wax seals)" }
shadow: "카드 default 없음 — 배경 차이로 깊이 / 버튼 inset engraved: inset 0 1px 0 rgba(255,255,255,0.2) + inset 0 -1px 0 rgba(0,0,0,0.2) + 0 2px 8px rgba(0,0,0,0.3) / wax seal: inset ±2px 4px + 0 4px 8px rgba(0,0,0,0.4) / hover brass glow: 0 4px 12px rgba(201,169,98,0.3)"
border: "1px solid #4A3F35 (wood grain) 기본 — 2px solid #C9A962 (brass) interactive/decorative — focus: ring-2 ring-[#C9A962] ring-offset-2 ring-offset-[#1C1714]"
effects:
  paper_texture: "SVG fractalNoise feTurbulence 3% opacity fixed overlay blend-mode:overlay"
  vignette: "radial-gradient(ellipse at center, transparent 50%, rgba(28,23,20,0.4) 100%) fixed overlay"
  sepia_image: "default: sepia(0.6) contrast(0.95) brightness(0.9) — hover: sepia(0) contrast(1) brightness(1) — 700ms ease-out (aged photos come to life)"
  brass_gradient: "linear-gradient(180deg, #D4B872 0%, #C9A962 50%, #B8953F 100%)"
  engraved_text: "text-shadow: 1px 1px 1px rgba(0,0,0,0.4), -1px -1px 1px rgba(255,255,255,0.1)"
  drop_cap: "Cinzel text-7xl float-left mr-4 leading-[0.8] text-[#C9A962] text-shadow 2px 2px 4px rgba(0,0,0,0.3)"
  corner_flourish_hero: "::before top-left + ::after bottom-right — 40×40px 2px solid #C9A962, border-right/bottom none"
  corner_flourish_card: "24×24px 같은 패턴, opacity-60 → opacity-100 hover"
  ornate_divider: "h-px linear-gradient(90deg, transparent→#4A3F35→#C9A962→#4A3F35→transparent) + centered glyph (✶ ❧ ✤ ❦) bg-[#1C1714] px-3"
  wax_seal: "circular bg-[#8B2635] radial-gradient + inset shadows, -top-3 right-6 absolute, star icon centered"
animation:
  timing: "ease-out only — bounce/spring/ease-in-out 금지"
  duration: "150ms fast (button press/focus) / 300ms standard (hover/borders) / 500ms deliberate (card lift) / 700ms dramatic (sepia→color/scale)"
  hover_image: "scale-105 700ms on img only, overflow-hidden on container"
  hover_card: "border→#C9A962/50, shadow 0 8px 24px rgba(0,0,0,0.3) 300ms"
  hover_stat: "number scale-110, label→brass, bg darkens"
  faq: "chevron rotate-180 + color to brass on open"
  brass_shimmer: "hover:brightness-110 (gentle pulse optional)"
layout: [max-w-6xl standard / max-w-4xl narrow / max-w-7xl full-width, py-24–py-32 sections, 8px grid system, 3-col grid-cols-1 md:grid-cols-3, 60/40 or 7/5 asymmetric hero]
components:
  button_primary: "Cinzel uppercase tracking-[0.15em] text-xs h-12 px-8, brass gradient bg, text-[#1C1714], engraved shadow, hover:brightness-110 + brass glow, active: deeper inset"
  button_secondary: "transparent bg, border-2 border-[#C9A962] text-[#C9A962], hover: bg-[#8B2635] border-[#8B2635] text-[#E8DFD4]"
  button_ghost: "no bg/border, text-[#C9A962], hover: text-[#D4B872] + underline-offset-4"
  cards: "bg-[#251E19] border-[#4A3F35] rounded p-8, corner-flourish, hover: border-[#C9A962]/50 + shadow lift 300ms"
  cards_featured: "border-2 border-[#C9A962] + wax seal badge top-right"
  inputs: "bg-[#251E19] border-[#4A3F35] h-12 px-4 rounded, Crimson Pro, placeholder italic text-[#9C8B7A], focus: border-[#C9A962] ring-2 ring-[#C9A962]/30"
  section_label: "Cinzel uppercase tracking-[0.25em] text-xs text-[#C9A962] — 'Volume I / Volume II' prefix on all major sections"
  dividers: "full-width border-y border-[#4A3F35] between sections"
  icons: "lucide stroke-[1.5px], h-4–h-6, text-[#C9A962], circular container rounded-full border-[#C9A962]/30 bg-[#1C1714] h-12 w-12"
special_notes:
  - "arch-top 이미지 필수 — cathedral arch radius 없으면 스타일 실패"
  - "세피아→컬러 700ms 전환 필수 — 모든 이미지에 적용"
  - "Roman numerals Volume I/II/III 필수 — 모든 major 섹션에 prefix"
  - "drop cap Cinzel 필수 — major 섹션 첫 단락에"
  - "brass (#C9A962) = 유일한 interactive color — 버튼/링크/focus/아이콘 전부"
  - "crimson (#8B2635) 절약 — featured/wax seal/secondary hover 변환에만"
  - "pure black #000 / pure white #fff 절대 금지 — warm mahogany + parchment만"
  - "sans-serif 절대 금지 — 세 가지 serif 패밀리만"
  - "paper texture 3% + vignette overlay 필수 — atmospheric depth"
  - "corner flourish 과용 금지 — hero(large 40px) + cards(small 24px)만"
  - "custom CSS 필수 — arch-top/drop-cap/flourish/ornate divider Tailwind 단독 불가"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Scholarly gravitas meets timeless elegance.** Centuries-old university libraries, Victorian study halls, Renaissance manuscripts. Every element belongs in a prestigious institution — combining rich material references (aged parchment, dark mahogany, polished brass, crimson leather) with traditional typographic excellence and measured ornamentation.

**Vibe:** Scholarly, Prestigious, Warm, Timeless, Dignified, Intellectual. Not a modern dark theme with serifs — a complete transformation into a physical library environment.

### Colors (Library at Night)
```
background:       #1C1714  (Deep Mahogany — warmest dark)
backgroundAlt:    #251E19  (Aged Oak — card/panel surface)
foreground:       #E8DFD4  (Antique Parchment — primary text, 8.5:1)
muted:            #3D332B  (Worn Leather — disabled/tertiary bg)
mutedForeground:  #9C8B7A  (Faded Ink — secondary text, 4.5:1)
accent:           #C9A962  (Polished Brass — ALL interactive elements)
accentSecondary:  #8B2635  (Library Crimson — special emphasis only)
border:           #4A3F35  (Wood Grain — subtle dividers)
accentForeground: #1C1714  (Dark text on brass)
```
**Brass gradient (buttons):** `linear-gradient(180deg, #D4B872 0%, #C9A962 50%, #B8953F 100%)`

Rules: No pure `#000` or `#FFF`. Warm tones exclusively. Brass for ALL interactive elements. Crimson: featured pricing / wax seals / secondary button hover ONLY.

### Typography
- **Heading:** `"Cormorant Garamond", serif` — calligraphic elegance, 400-500 weight
- **Body:** `"Crimson Pro", serif` — book-style extended reading, 400 weight
- **Display/Labels:** `"Cinzel", serif` — engraved all-caps, buttons/labels/overlines

| Role | Size | Font | Notes |
|:-----|:-----|:-----|:------|
| Display H1 | `text-5xl–text-7xl` | Cormorant | `leading-[1.1] tracking-tight` |
| Section H2 | `text-4xl–text-5xl` | Cormorant | `tracking-tight` |
| H3 | `text-2xl–text-3xl` | Cormorant | |
| Body | `text-base–text-lg` | Crimson Pro | `leading-relaxed` |
| Labels/Buttons | `text-xs` | Cinzel | `uppercase tracking-[0.15em]–[0.3em]` |

**Drop Cap** (major section intros):
```css
.drop-cap::first-letter {
  font-family: 'Cinzel';
  font-size: 4.5rem; /* text-7xl */
  float: left;
  line-height: 0.8;
  margin-right: 1rem;
  color: #C9A962;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
```

**Roman Numeral Volume System (MANDATORY):**
```
"Volume I", "Volume II", "Volume III" — prefix for ALL major sections
Standalone I, II, III for list items and sub-elements
Cinzel font, uppercase, tracking-[0.25em], text-[#C9A962]
```

**Engraved text effect (buttons/special headings):**
```css
text-shadow: 1px 1px 1px rgba(0,0,0,0.4), -1px -1px 1px rgba(255,255,255,0.1);
```

### Radius & Borders
- **Default:** `4px` (`rounded`) — buttons, cards, inputs
- **Arch-top signature:** `border-radius: 40% 40% 0 0 / 20% 20% 0 0` — hero/feature/blog images, mandatory
- **Circle:** `rounded-full` — icon containers, wax seals
- Border: `1px solid #4A3F35` default, `2px solid #C9A962` interactive/decorative

### Shadows
```css
/* Card: no shadow at rest — background differentiation carries depth */
hover: box-shadow: 0 8px 24px rgba(0,0,0,0.3)

/* Button engraved */
box-shadow: inset 0 1px 0 rgba(255,255,255,0.2),
            inset 0 -1px 0 rgba(0,0,0,0.2),
            0 2px 8px rgba(0,0,0,0.3);
hover: + 0 4px 12px rgba(201,169,98,0.3) brass glow

/* Wax seal */
box-shadow: inset 0 2px 4px rgba(255,255,255,0.2),
            inset 0 -2px 4px rgba(0,0,0,0.3),
            0 4px 8px rgba(0,0,0,0.4);
```

### Textures & Atmospheric Effects (All Required)

**Paper texture overlay:**
```html
<svg aria-hidden="true" class="fixed inset-0 pointer-events-none z-50 opacity-[0.03] mix-blend-overlay w-full h-full">
  <filter id="paper"><feTurbulence baseFrequency="0.65" numOctaves="3" /></filter>
  <rect width="100%" height="100%" filter="url(#paper)" />
</svg>
```

**Vignette overlay:**
```html
<div aria-hidden="true" class="fixed inset-0 pointer-events-none z-40"
  style="background: radial-gradient(ellipse at center, transparent 0%, transparent 50%, rgba(28,23,20,0.4) 100%)" />
```

**Sepia image treatment:**
```css
.academia-img { filter: sepia(0.6) contrast(0.95) brightness(0.9); transition: filter 700ms ease-out; }
.academia-img:hover { filter: sepia(0) contrast(1) brightness(1); }
```

**Arch-top images:**
```css
.arch-top { border-radius: 40% 40% 0 0 / 20% 20% 0 0; }
```

**Corner flourishes (hero 40px / cards 24px):**
```css
.ornate-frame { position: relative; }
.ornate-frame::before {
  content: ""; position: absolute; top: -1px; left: -1px;
  width: 40px; height: 40px;
  border: 2px solid #C9A962; border-right: none; border-bottom: none;
}
.ornate-frame::after {
  content: ""; position: absolute; bottom: -1px; right: -1px;
  width: 40px; height: 40px;
  border: 2px solid #C9A962; border-left: none; border-top: none;
}
/* Cards: 24px, opacity-60 → opacity-100 hover */
```

**Ornate divider:**
```css
.ornate-divider {
  position: relative; height: 1px;
  background: linear-gradient(90deg, transparent 0%, #4A3F35 20%, #C9A962 50%, #4A3F35 80%, transparent 100%);
}
.ornate-divider::before {
  content: "✶"; position: absolute; left: 50%; top: 50%;
  transform: translate(-50%, -50%);
  color: #C9A962; font-size: 12px;
  background: #1C1714; padding: 0 12px;
}
```

**Wax seal badge:**
```jsx
<div className="absolute -top-3 right-6 h-10 w-10 rounded-full flex items-center justify-center"
  style={{ background: "radial-gradient(circle at 35% 35%, #A03040, #8B2635 60%, #6B1A26)", boxShadow: "inset 0 2px 4px rgba(255,255,255,0.2), inset 0 -2px 4px rgba(0,0,0,0.3), 0 4px 8px rgba(0,0,0,0.4)" }}>
  <Star className="h-4 w-4 text-[#E8DFD4]" strokeWidth={1.5} />
</div>
```

### Buttons

**Primary (brass):**
```
font: Cinzel uppercase tracking-[0.15em] text-xs
h-12 px-8 rounded bg-[brass-gradient] text-[#1C1714]
shadow: engraved inset shadows
hover: brightness-110 + brass glow 0 4px 12px rgba(201,169,98,0.3)
active: deeper inset shadow
```

**Secondary:**
```
border-2 border-[#C9A962] text-[#C9A962] bg-transparent rounded
hover: bg-[#8B2635] border-[#8B2635] text-[#E8DFD4] — dramatic crimson transformation
```

**Ghost:**
```
text-[#C9A962] no bg/border
hover: text-[#D4B872] + underline-offset-4
```

All: `focus-visible:ring-2 focus-visible:ring-[#C9A962] focus-visible:ring-offset-2 focus-visible:ring-offset-[#1C1714]`, `disabled:opacity-50 disabled:pointer-events-none`

### Cards & Containers
```
bg-[#251E19] border border-[#4A3F35] rounded p-8 relative
hover: border-[#C9A962]/50, shadow 0 8px 24px rgba(0,0,0,0.3) — 300ms ease-out
corner-flourish (24px) opacity-60 → opacity-100 on hover
```
**Featured card:** `border-2 border-[#C9A962]` + wax seal badge top-right.
**Arch-top image card:** image container uses `.arch-top`, sepia filter on img, `scale-105` on card hover.

### Inputs
```
bg-[#251E19] border border-[#4A3F35] rounded h-12 px-4 py-2
text-[#E8DFD4] font-['Crimson_Pro'] placeholder:italic placeholder:text-[#9C8B7A]
focus: border-[#C9A962] ring-2 ring-[#C9A962]/30 outline-none
```
Label: Cinzel uppercase tracking-wide text-xs text-[#9C8B7A].

### Layout
- Container: `max-w-6xl mx-auto` standard / `max-w-4xl` narrow / `max-w-7xl` full-bg
- Section: `py-24 md:py-32` — generous breathing room for contemplation
- Grids: `grid-cols-1 md:grid-cols-3` features/pricing, `grid-cols-1 lg:grid-cols-2` hero split
- Stats: `grid-cols-2 md:grid-cols-4`
- Hero: 60/40 or 7/5 asymmetric column split
- Section separators: `border-y border-[#4A3F35]` full-width + optional `bg-[#251E19]/30`

### Non-Negotiable Bold Choices
1. **Arch-top images** — cathedral arch on every featured image (single most defining element)
2. **Sepia-to-color 700ms** — aged photographs come to life on hover
3. **Volume I / II / III Roman numerals** — every major section prefix in Cinzel brass
4. **Drop cap** — first paragraph of major sections
5. **Corner flourishes** — hero (40px), cards (24px)
6. **Ornate dividers** — gradient + centered glyph ✶ between sections
7. **Wax seal badges** — crimson circular for featured items
8. **Brass as sole interactive language** — every button/link/focus ring
9. **Engraved text shadow** — buttons and special headings
10. **Texture + vignette overlays** — both fixed overlays mandatory

### Animation
```css
/* Fast */    transition: all 150ms ease-out;   /* button press, focus */
/* Standard */ transition: all 300ms ease-out;   /* hover, borders */
/* Slow */     transition: all 500ms ease-out;   /* card lift */
/* Dramatic */ transition: all 700ms ease-out;   /* sepia→color, scale */

/* Never: ease-in-out, bounce, spring, playful delays */
/* Scale: scale-105 or scale-[1.02] max — never dramatic */
```

`@media (prefers-reduced-motion: reduce)` — collapse all durations to 0.01ms.

### Responsive
- Mobile: stack columns, `py-16`, hide large corner flourishes (`hidden md:block`), maintain arch-tops + sepia
- Touch targets: `h-12` minimum (48px)
- Stack email input + button vertically on mobile
- Keep all three serif fonts at all breakpoints — only scale sizes down slightly

### Accessibility
- `#E8DFD4` on `#1C1714`: 8.5:1 AAA ✓
- `#9C8B7A` on `#1C1714`: 4.5:1 AA ✓
- `#C9A962` on `#1C1714`: 7:1 ✓
- `#1C1714` on `#C9A962` button: 8:1 ✓
- Focus: `ring-2 ring-[#C9A962] ring-offset-2 ring-offset-[#1C1714]` — never remove
- Decorative flourishes/dividers: `aria-hidden="true"`
- Texture/vignette overlays: `aria-hidden="true" pointer-events-none`

### Custom CSS Required (cannot use Tailwind alone)
- `.arch-top` border-radius complex multi-value syntax
- `.drop-cap::first-letter` pseudo-element
- `.ornate-frame::before/::after` corner flourishes
- `.ornate-divider` gradient + `::before` glyph centering
- `.academia-img` sepia filter transitions
- Paper texture SVG noise filter
- Vignette radial gradient overlay
- Brass gradient buttons (inline style or CSS variable)

</design-system>
