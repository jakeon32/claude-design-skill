# Organic / Natural Design System
source: designprompts.dev
category: light

```yaml
palette: { bg: "#FDFCF8", fg: "#2C2C24", primary: "#5D7052", primary_fg: "#F3F4F1", secondary: "#C18C5D", accent: "#E6DCCD", muted: "#F0EBE5", muted_fg: "#78786C", border: "#DED8CF", destructive: "#A85448" }
typography: { heading: "Fraunces (variable serif, old-style warmth 600-800)", body: "Nunito or Quicksand (rounded terminals 필수, 날카로운 sans 금지)", scale: "1.25 moderate / hero text-5xl→7xl / section text-4xl→5xl" }
style_traits: [와비-사비 유기적 자연, 블롭 border-radius (60% 40% 30% 70% / 60% 30% 70% 40%), 그레인 노이즈 텍스처 3-5% multiply, 모스 그린+테라코타+샌드 팔레트, blur-3xl 블롭 배경, -rotate-2 이미지 프레임, 비대칭 카드 반경 6패턴 cycling, curved SVG 연결선]
radius: { standard: "rounded-2xl (16px) / rounded-3xl (24px) / rounded-[2rem]", blob: "60% 40% 30% 70% / 60% 30% 70% 40% (inline style)", image_mask: "rounded-[30%_70%_70%_30%_/_30%_30%_70%_70%]", nav: "rounded-full", button: "rounded-full (pill 필수)" }
shadow: "자연 색상 틴티드만 — moss: 0 4px 20px -2px rgba(93,112,82,0.15) / float-clay: 0 10px 40px -10px rgba(193,140,93,0.2) / hover: 0 20px 40px -10px rgba(93,112,82,0.15) — pure black shadow 절대 금지"
border: "#DED8CF/50 (50% opacity timber, 섬세한 분리) — harsh border 금지"
effects:
  grain_texture: "noise overlay fixed 3-5% opacity mix-blend-multiply 전체 배경 — 종이 질감 필수 (없으면 flat digital)"
  blur_blobs: "absolute blob-shaped div blur-3xl — 섹션별 ambient color wash (Hero 2개, Features, CTA)"
  blob_shapes: "border-radius: 60% 40% 30% 70% / 60% 30% 70% 40% — inline style, 섹션별 varied"
  rotated_image: "rotate-[-2deg] + border-4 border-white — 핸드크래프트 사진 느낌"
  organic_image_mask: "rounded-[30%_70%_70%_30%_/_30%_30%_70%_70%] — benefits 섹션 이미지"
  asymmetric_cards: "6가지 다른 rounded 패턴 cycling (tl-4rem, tr-5rem 등) — 비균일성"
  svg_connector: "curved dashed SVG path — How It Works 곡선 연결선 (직선 대신)"
animation:
  timing: "300ms (버튼/링크) / 500ms (카드 lift) / 700ms (이미지 scale) — gentle only"
  hover_btn: "scale-105 + shadow deepen / active:scale-95 tactile press"
  hover_card: "-translate-y-1 (lift) or hover:rotate-1 (testimonial tilt)"
  hover_icon: "bg-[#5D7052]/10 → bg-[#5D7052] + text-white fill transition"
  hover_image: "scale-105 duration-700 — slow organic reveal"
  no_snap: "harsh snap 금지 — 300~700ms ease-out natural motion"
layout: [max-w-7xl primary, max-w-5xl CTA, py-32 sections, gap-8~16, varied section bg (off-white/stone/sand/moss/terracotta), sticky floating pill nav]
components:
  button_primary: "rounded-full bg-[#5D7052] text-[#F3F4F1] font-bold h-12 px-8 shadow-moss / hover:scale-105 shadow-[0_6px_24px_-4px_rgba(93,112,82,0.25)] / active:scale-95 / focus:ring-2 ring-[#5D7052]/30"
  button_outline: "rounded-full border-2 border-[#C18C5D] text-[#C18C5D] bg-transparent h-12 px-8"
  button_ghost: "rounded-full text-[#5D7052] h-12 px-8 hover:bg-[#5D7052]/10"
  cards: "rounded-[2rem] bg-[#FEFEFA] border border-[#DED8CF]/50 shadow-[0_4px_20px_-2px_rgba(93,112,82,0.15)] p-8 / hover:-translate-y-1 hover:shadow-[0_20px_40px_-10px_rgba(93,112,82,0.15)] duration-500 / asymmetric radius variations"
  inputs: "rounded-full border border-[#DED8CF] bg-white/50 h-12 px-6 / focus:ring-2 ring-[#5D7052]/30 ring-offset-2"
  nav: "sticky top-4 rounded-full bg-white/70 backdrop-blur-md border border-[#DED8CF]/50 shadow-sm"
  icon_container: "h-14 w-14 rounded-2xl bg-[#5D7052]/10 text-[#5D7052] / hover:bg-[#5D7052] hover:text-white duration-300"
special_notes:
  - "Fraunces serif 필수 — old-style warmth + modern softness, system font = 콘셉트 소멸"
  - "Nunito or Quicksand rounded terminals 필수 — 날카로운 sans-serif 금지"
  - "그레인 노이즈 텍스처 (3-5% mix-blend-multiply) 필수 — 없으면 flat digital"
  - "블롭 border-radius (60% 40% 30% 70% / ...) inline style 필수"
  - "colored shadow만 — pure black rgba(0,0,0,x) shadow 금지, moss/clay 틴트"
  - "active:scale-95 버튼 눌림 + hover:scale-105 필수 — 촉각 피드백"
  - "blur-3xl 블롭 ambient wash 섹션마다 필수"
  - "-rotate-2 이미지 프레임 핸드크래프트 feel"
  - "비대칭 카드 반경 6패턴 cycling — 균일한 rounded 금지"
  - "rounded-full pill nav sticky + backdrop-blur-md glassmorphism"
  - "자연에 직선 없음 — 90도 각도 요소 최소화"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Wabi-sabi** — acceptance of transience and imperfection. Rejects cold digital precision in favor of warmth, softness, and natural connection. Tactile, grounded, calming.

**Core Tenet:** "There are no straight lines in nature." Everything feels eroded by wind and water, or shaped by hand.

**Visual DNA:**
- Soft amorphous blob shapes with complex percentage border-radius
- Global grain/noise texture overlay at 3-4% opacity with multiply blend
- Earth palette: forest floors, clay pottery, unbleached paper, dried grass, river stones
- Colored shadows (moss green, clay orange tints) — never pure black
- Fraunces serif: old-world warmth with modern softness
- Asymmetry: rotated images, offset elements, varied card shapes

### Colors (Earth Palette)
```
background:           #FDFCF8  (Rice Paper / Off-white)
foreground:           #2C2C24  (Deep Loam / Charcoal)
primary:              #5D7052  (Moss Green)
primary-foreground:   #F3F4F1  (Pale Mist)
secondary:            #C18C5D  (Terracotta / Clay)
accent:               #E6DCCD  (Sand / Beige)
muted:                #F0EBE5  (Stone)
muted-foreground:     #78786C  (Dried Grass)
border:               #DED8CF  (Raw Timber)
destructive:          #A85448  (Burnt Sienna)
```
**Contrast:** #2C2C24 on #FDFCF8: 14.5:1 (AAA) / #5D7052: 6.2:1 (AA) / #78786C: 4.8:1 (AA)

### Typography
- **Headings:** `"Fraunces", Georgia, serif` — variable font, soft axes, 600-800
- **Body:** `"Nunito", system-ui, sans-serif` (or Quicksand) — rounded terminals essential

Scale: 1.25 moderate. Hero: `text-5xl md:text-7xl`. Section: `text-4xl md:text-5xl`.

### Radius & Organic Shapes
```
Standard card:  rounded-2xl (16px) or rounded-[2rem]
Blobs:          inline style only (no Tailwind class)
Nav / Buttons:  rounded-full (pill)
```

**Blob border-radius (primary):**
```css
border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
```

**Image organic mask (benefits):**
```css
border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
```

**Asymmetric card patterns (6 cycling variants):**
```jsx
const radii = [
  "rounded-tl-[4rem] rounded-tr-[2rem] rounded-br-[4rem] rounded-bl-[2rem]",
  "rounded-tl-[2rem] rounded-tr-[5rem] rounded-br-[2rem] rounded-bl-[4rem]",
  "rounded-tl-[5rem] rounded-tr-[2rem] rounded-br-[3rem] rounded-bl-[2rem]",
  // ...etc
]
```

### Shadows (Nature-Tinted — No Pure Black)
```css
/* Moss shadow (primary) */
shadow-soft: 0 4px 20px -2px rgba(93, 112, 82, 0.15);
shadow-soft-hover: 0 20px 40px -10px rgba(93, 112, 82, 0.15);

/* Clay float shadow */
shadow-float: 0 10px 40px -10px rgba(193, 140, 93, 0.2);

/* Button hover shadow */
0 6px 24px -4px rgba(93, 112, 82, 0.25);

/* NEVER: rgba(0, 0, 0, x) pure black shadows */
```

### Grain Texture (MANDATORY)
```jsx
{/* Fixed background grain overlay */}
<div
  aria-hidden="true"
  className="pointer-events-none fixed inset-0 z-10"
  style={{
    opacity: 0.04,
    mixBlendMode: "multiply",
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E")`,
    backgroundRepeat: "repeat",
  }} />
```
**Without grain texture: flat, digital, soulless. It is non-negotiable.**

### Ambient Blobs (Background Depth)
```jsx
{/* Hero blobs */}
<div aria-hidden="true" className="pointer-events-none absolute inset-0 overflow-hidden -z-10">
  <div className="absolute -top-20 -left-20 h-[500px] w-[500px]
    bg-[#5D7052]/20 blur-3xl"
    style={{ borderRadius: "60% 40% 30% 70% / 60% 30% 70% 40%" }} />
  <div className="absolute bottom-0 right-0 h-[400px] w-[400px]
    bg-[#C18C5D]/15 blur-3xl"
    style={{ borderRadius: "40% 60% 70% 30% / 40% 70% 30% 60%" }} />
</div>
```

### Floating Pill Navigation
```jsx
<nav className="sticky top-4 rounded-full bg-white/70 backdrop-blur-md
  border border-[#DED8CF]/50
  shadow-[0_4px_20px_-2px_rgba(93,112,82,0.1)] z-50">
```

### Buttons
**Primary:**
```
rounded-full bg-[#5D7052] text-[#F3F4F1] font-bold h-12 px-8
shadow-[0_4px_20px_-2px_rgba(93,112,82,0.15)]

hover: scale-105 shadow-[0_6px_24px_-4px_rgba(93,112,82,0.25)]
active: scale-95
focus: ring-2 ring-[#5D7052]/30 ring-offset-2
transition: all 300ms ease-out
```

**Outline:** `rounded-full border-2 border-[#C18C5D] text-[#C18C5D] bg-transparent h-12 px-8`

**Ghost:** `rounded-full text-[#5D7052] h-12 px-8 hover:bg-[#5D7052]/10`

### Cards
```jsx
<div
  className="bg-[#FEFEFA] border border-[#DED8CF]/50
    shadow-[0_4px_20px_-2px_rgba(93,112,82,0.15)] p-8
    hover:-translate-y-1
    hover:shadow-[0_20px_40px_-10px_rgba(93,112,82,0.15)]
    transition-all duration-500 ease-out"
  style={{ borderRadius: "..." }}  // cycle through 6 asymmetric patterns
>
```

**Testimonial cards:** `hover:rotate-1` — picking up a physical card feel.

### Inputs
```
rounded-full border border-[#DED8CF] bg-white/50 h-12 px-6
placeholder: text-[#78786C]
focus: ring-2 ring-[#5D7052]/30 ring-offset-2
transition: all 300ms ease-out
```

### Icon Containers
```jsx
<div className="h-14 w-14 rounded-2xl bg-[#5D7052]/10
  flex items-center justify-center group
  transition-colors duration-300
  hover:bg-[#5D7052]">
  <Icon className="text-[#5D7052] group-hover:text-white" size={28} />
</div>
```

### Rotated Image (Product Detail)
```jsx
<div className="rotate-[-2deg] border-4 border-white
  shadow-[0_10px_40px_-10px_rgba(193,140,93,0.2)]">
  <img className="hover:scale-105 transition-transform duration-700" />
</div>
```

### Curved SVG Connector (How It Works)
```jsx
<svg className="absolute top-1/2 w-full hidden md:block" viewBox="0 0 800 60">
  <path d="M100,30 Q300,0 400,30 Q500,60 700,30"
    fill="none" stroke="#DED8CF" strokeWidth="2"
    strokeDasharray="8,6" />
</svg>
```

### Non-Negotiable Bold Choices
1. **Grain texture** 3-5% opacity mix-blend-multiply — mandatory
2. **Blob border-radius** inline style for organic shapes
3. **Fraunces + Nunito/Quicksand** — no substitutes
4. **Colored shadows only** — moss/clay tints, no pure black
5. **active:scale-95 + hover:scale-105** buttons — tactile physics
6. **blur-3xl ambient blobs** in backgrounds
7. **-rotate-2 image frames** — handcrafted feel
8. **Asymmetric card radii** cycling 6 patterns
9. **Curved dashed SVG** connector between steps
10. **Floating pill nav** `rounded-full backdrop-blur-md`

### Animation
```css
/* Buttons, links */
transition: all 300ms ease-out;

/* Cards, lifts */
transition: all 500ms ease-out;

/* Images */
transition: transform 700ms ease-out;

/* NEVER: harsh snap, duration < 200ms */
/* YES: organic, gentle, breathing motion */
```

### Layout
```
Max widths: max-w-7xl (primary) / max-w-6xl / max-w-5xl (CTA)
Sections: py-32
Gaps: gap-8, md:gap-12 to gap-16
Section BG variation: off-white / stone / sand / moss / terracotta
```

### Responsive
- Hero: `text-5xl md:text-7xl`
- Sections: `py-32`
- Grids: 1-col mobile → `md:grid-cols-3` desktop
- Blobs: `overflow-hidden` on mobile to prevent layout issues
- Hamburger nav on mobile → floating pill on desktop
- Touch: `h-12` (48px) all interactive elements

### Accessibility
- #2C2C24 on #FDFCF8: 14.5:1 (AAA)
- Focus: `ring-2 ring-[#5D7052]/30 ring-offset-2`
- Grain texture: `aria-hidden="true"`
- Icon containers: always paired with text or `aria-label`

</design-system>
