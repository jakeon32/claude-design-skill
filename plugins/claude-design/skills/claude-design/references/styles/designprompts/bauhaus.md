# Bauhaus Style
source: designprompts.dev
category: light

```yaml
palette: { bg: "#F0F0F0", fg: "#121212", red: "#D02020", blue: "#1040C0", yellow: "#F0C020", border: "#121212", muted: "#E0E0E0" }
typography: { heading: "Outfit", body: "Outfit", weight: "900 black uppercase tight-tracking headlines / 700 bold subheadings / 500 medium body / labels: 700 uppercase tracking-widest", size_display: "4xl→6xl→8xl", leading: "0.9 (headlines) / relaxed (body)" }
style_traits: [Bauhaus Constructivist Modernism, form follows function, geometric purity circles/squares/triangles, primary color blocking, thick 2px–4px black borders, hard offset shadows, asymmetric grid, 1920s poster aesthetic]
radius: "0px (rectangles) OR rounded-full (circles) — 중간값 금지"
shadow: "hard offset no-blur: 3–4px small / 6px medium / 8px large — all #000000"
effects:
  dot_grid: "radial-gradient(#fff 2px, transparent 2px) 20px 20px — section texture"
  color_blocking: "hero blue/stats yellow/blog blue/benefits red/cta yellow/footer #121212"
  geo_overlay: "large geometric shapes 10–20% opacity bg decoration (circle+rotated square+triangle)"
  button_press: "active: translate(+2px,+2px) shadow-none — physical press"
  card_hover: "hover:-translateY(1–2px) lift"
  accordion_open: "bg-red white text header / bg-[#FFF9C4] content / border-t-4 black"
  geo_logo: "3 shapes nav — circle+square+triangle in primary colors"
  image_treatment: "grayscale default / hover:grayscale-0"
  rotated_elements: "45deg rotation every 3rd shape / step numbers / bg decorative shapes"
animation:
  timing: "duration-200–300 ease-out — mechanical snappy"
  button: "active: translate+2px shadow-none"
  card: "hover: translateY(-1–2px)"
  accordion: "ChevronDown rotate-180 + max-height reveal"
  icon: "group-hover:scale-110"
layout: [max-w-7xl, py-12–py-24 sections, border-b-4 black section dividers, stats 1→2→4col divide-x-y, features 1→2→3col, pricing 3col center-elevated, geometric compositions asymmetric]
components:
  nav: "4px bottom border, geometric 3-shape logo, Outfit 700 uppercase links, primary CTA"
  hero: "split: left text + right blue color-block panel with geometric composition"
  buttons: "red/blue/yellow/outline variants — all: 2–4px black border + 4px hard shadow + press effect"
  cards: "white 4px black border 8px shadow, geo corner decoration (8px circle/square/triangle in primary), hover lift"
  accordion: "closed: white 4px border 4px shadow / open: red header + #FFF9C4 content"
  stats: "yellow bg section, numbers in geo containers (circle/square/rotated-square)"
  blog_images: "alternate rounded-full/rounded-none, grayscale→color hover"
  testimonials: "circular avatar grayscale, Quote icon"
special_notes:
  - "순수 primary 색상 필수 — 혼합/tinted 금지"
  - "0px OR rounded-full — 중간 radius 절대 금지"
  - "gradient 금지 — solid fills only"
  - "border color 항상 #121212"
  - "모든 headline uppercase tracking-tighter leading-[0.9]"
  - "color-block sections 필수 — generic white bg 금지"
  - "geometric shape compositions 필수 (circle+square+triangle)"
  - "duration-200–300 ease-out — slow/bouncy animation 금지"
```

---

## Full Design System Prompt

<design-system>

### Design Philosophy
"Form follows function" + pure geometric beauty + primary color theory. Constructivist modernism — every element composed from circles, squares, triangles. Like a 1920s Bauhaus poster come alive: bold, asymmetric, architectural, unapologetically graphic.

**Vibe**: Constructivist, Geometric, Modernist, Artistic-yet-Functional, Bold, Architectural

### Colors
```
background:    #F0F0F0  (Off-white canvas)
foreground:    #121212  (Stark Black)
primary-red:   #D02020  (Bauhaus Red)
primary-blue:  #1040C0  (Bauhaus Blue)
primary-yellow:#F0C020  (Bauhaus Yellow)
border:        #121212
muted:         #E0E0E0
```

### Typography
Font: **Outfit** (wght@400;500;700;900) — circular letterforms embody Bauhaus principles.

Scale: Display text-4xl(mobile)→text-6xl(tablet)→text-8xl(desktop) / Subheadings text-2xl→text-4xl / Body text-base→text-lg

Weights: Headlines font-black(900) uppercase tracking-tighter leading-[0.9] / Subheadings font-bold(700) uppercase / Body font-medium(500) / Labels font-bold(700) uppercase tracking-widest

### Radius & Border
- Radius: ONLY `rounded-none` (0px) OR `rounded-full` (9999px) — no in-between
- Border widths: border-2(mobile) → border-4(desktop) / nav: border-b-4
- Border color: always #121212

### Shadows (Hard Offset — never soft/blurred)
```
Small:  shadow-[3px_3px_0px_0px_black] or shadow-[4px_4px_0px_0px_black]
Medium: shadow-[6px_6px_0px_0px_black]
Large:  shadow-[8px_8px_0px_0px_black]
```
Button press: `active:translate-x-[2px] active:translate-y-[2px] active:shadow-none`
Card hover: `hover:-translate-y-1` or `hover:-translate-y-2`

Patterns:
- Dot grid: `radial-gradient(#fff 2px, transparent 2px)` background-size: 20px 20px
- Geometric shapes at 10–20% opacity as background decoration

### Buttons
- Primary (Red): `bg-[#D02020] text-white border-2 border-black shadow-[4px_4px_0px_0px_black]`
- Secondary (Blue): `bg-[#1040C0] text-white border-2 border-black shadow-[4px_4px_0px_0px_black]`
- Yellow: `bg-[#F0C020] text-black border-2 border-black shadow-[4px_4px_0px_0px_black]`
- Outline: `bg-white text-black border-2 border-black shadow-[4px_4px_0px_0px_black]`
- Shapes: rounded-none OR rounded-full only
- States: hover opacity/90 / active: translate+2px shadow-none / focus: 2px offset ring
- Typography: uppercase font-bold tracking-wider

### Cards
- Base: white bg, border-4 border-black, shadow-[8px_8px_0px_0px_black]
- Corner decoration: 8px geometric shape (circle/square/triangle) in primary color
- Hover: `hover:-translate-y-1`

### Accordion (FAQ)
- Closed: white bg, border-4 border-black, shadow-[4px_4px_0px_0px_black]
- Open header: bg-[#D02020] white text
- Open content: bg-[#FFF9C4] black text, border-t-4 border-black
- Icon: ChevronDown rotate-180 when open

### Layout
- Container: max-w-7xl
- Section padding: py-12 px-4 (mobile) → py-24 px-8 (desktop)
- Section dividers: border-b-4 border-black (every section)
- Stats grid: 1col → 2col(sm) → 4col(lg) with divide-y/divide-x borders
- Features: 1col → 2col(md) → 3col(lg), 8px gaps
- Pricing: 1col → 3col(lg), center tier elevated

### Mandatory Bold Choices (Non-Negotiable)
1. **Color Blocking**: Hero right panel→blue / Stats→yellow / Blog→blue / Benefits→red / CTA→yellow / Footer→#121212
2. **Geometric Logo**: 3 shapes (circle+square+triangle) in primary colors
3. **Geometric Compositions**: Overlapping shapes in hero panel, product detail, CTA corners
4. **Rotated Elements**: 45° on every 3rd shape, step numbers, bg decorative shapes
5. **Image Treatment**: grayscale default → grayscale-0 on hover. Blog: alternate rounded-full/rounded-none
6. **Corner Decorations**: 8–16px geometric shapes on cards (3 primary colors rotating)

### Icons
- Library: lucide-react (Circle, Square, Triangle, Check, Quote, ArrowRight, ChevronDown)
- Stroke: 2px default, 3px emphasis / Size: h-6 w-6 to h-8 w-8
- Features: icon in white bordered box with shadow
- Benefits: check in yellow circular badge
- Stats: numbers in geometric shape containers

### Animation
- Feel: Mechanical, snappy, geometric — no soft organic movement
- Duration: duration-200 or duration-300 / Easing: ease-out
- Button: translate+shadow-none on active
- Card: translateY lift on hover
- Accordion: ChevronDown rotate-180 + max-height transition
- Icon: group-hover:scale-110
- Background patterns: static (no animation)

### Responsive
- Mobile-first. Hamburger nav < 768px.
- Typography: text-4xl sm:text-6xl lg:text-8xl
- Border/shadow scale up on desktop
- Hide connecting line in "How It Works" on mobile

</design-system>
