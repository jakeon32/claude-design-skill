# Playful Geometric Design System
source: designprompts.dev
category: light

```yaml
palette: { bg: "#FFFDF5", fg: "#1E293B", muted: "#F1F5F9", muted_fg: "#64748B", accent: "#8B5CF6", accent_fg: "#FFFFFF", secondary: "#F472B6", tertiary: "#FBBF24", quaternary: "#34D399", border: "#E2E8F0", card: "#FFFFFF", ring: "#8B5CF6" }
typography: { heading: "Outfit (geometric sans, friendly rounded letterforms)", body: "Plus Jakarta Sans (geometric-humanist, screen-optimized)", weight: "700-800 headings / 400-500 body", scale: "1.25 Major Third ratio" }
style_traits: [Memphis Group 80s 현대화, 원시 도형 (원/삼각/사각/필) 장식, 하드 오프셋 섀도우(블러 없음) 스티커 컷아웃 느낌, 폴카닷/그리드/대각선 스트라이프 패턴, 혼합 반경 잎사귀+블롭 형태, confetti 다색 아이콘 시스템]
radius: { sm: "8px", md: "16px (rounded-2xl)", lg: "24px (rounded-3xl)", full: "9999px (rounded-full)", speech_bubble: "rounded-tl-2xl rounded-tr-2xl rounded-br-2xl rounded-bl-none", arch: "rounded-t-full rounded-b-none" }
shadow: "하드 섀도우 필수 — 0 blur, solid offset: 4px 4px 0px #1E293B (기본) / 6px 6px 0px (hover lift) / 2px 2px 0px (active press) / 8px 8px 0px #E2E8F0 or #F472B6 (카드)"
border: "border-2 (2px chunky) 기본 — border-[#1E293B] 다크 외곽선 + shadow 조합이 스티커 느낌 핵심"
effects:
  dot_grid: "radial-gradient(circle, #E2E8F0 1px, transparent 1px) 24px 24px bg"
  squiggles: "SVG path — 섹션 구분선 또는 헤딩 밑줄"
  confetti_shapes: "absolute positioned 소형 SVG 도형 (삼각/원) — 콘텐츠 블록 뒤 배경"
  card_icon: "floating circle div 카드 상단 테두리 걸쳐 배치 (half-in/half-out)"
  hero_deco: "massive yellow circle (#FBBF24) behind text + dot pattern behind image + blob mask on image"
  pricing_badge: "MOST POPULAR star badge rotate-[15deg] — 중앙 카드 scale-110"
  dashed_connector: "SVG dashed line between feature cards"
animation:
  easing: "cubic-bezier(0.34,1.56,0.64,1) — overshoot bounce, not ease-in-out"
  duration: "duration-300 standard"
  hover_card: "rotate-[-1deg] scale-[1.02] wiggle"
  button_hover: "translate-x-[-2px] translate-y-[-2px], shadow extends 6px 6px"
  button_active: "translate-x-[2px] translate-y-[2px], shadow shrinks 2px 2px"
  wiggle: "@keyframes wiggle { 0%,100%{rotate:0deg} 33%{rotate:3deg} 66%{rotate:-3deg} } — icon hover"
  pop_in: "scale 0 to 1 with bounce easing on entrance"
  marquee: "react-fast-marquee for logos/keywords"
layout: [max-w-6xl, py-24 96px sections, 12-col grouped 6/6 or 4/4/4, hero: text-left + deco-right split]
components:
  button_primary: "bg-[#8B5CF6] text-white font-bold rounded-full border-2 border-[#1E293B] shadow-[4px_4px_0px_#1E293B], hover:translate-x-[-2px] translate-y-[-2px] shadow-[6px_6px_0px_#1E293B], active:translate-x-[2px] translate-y-[2px] shadow-[2px_2px_0px_#1E293B] + ArrowRight in white circle inside"
  button_secondary: "bg-transparent border-2 border-[#1E293B] rounded-full, hover:bg-[#FBBF24]"
  cards: "bg-white border-2 border-[#1E293B] rounded-xl shadow-[8px_8px_0px_#E2E8F0], hover:rotate-[-1deg] hover:scale-[1.02] — floating circle icon half-in/half-out top border"
  cards_featured: "shadow-[8px_8px_0px_#F472B6] (pink shadow)"
  inputs: "bg-white border-2 border-[#CBD5E1] rounded-lg, focus: border-[#8B5CF6] shadow-[4px_4px_0px_#8B5CF6]"
  input_label: "font-bold uppercase text-sm tracking-wide"
  icons: "lucide stroke-[2.5px] rounded caps — enclosed in colored circles, never floating alone — 다색 confetti: accent/secondary/tertiary/quaternary 로테이션"
special_notes:
  - "하드 섀도우(0 blur 4px offset) 핵심 — blur shadow 사용시 스티커 느낌 소멸"
  - "border-2 (#1E293B) + hard shadow 조합 — 스티커/컷아웃 paper 느낌 필수"
  - "accent/secondary/tertiary/quaternary 4색 confetti 로테이션 — 단색 금지"
  - "Outfit 폰트 필수 — 둥근 letterform이 vibe 전달"
  - "아이콘 standalone 금지 — 항상 colored circle 안에 enclosed"
  - "bounce easing cubic-bezier(0.34,1.56,0.64,1) 필수 — ease-in-out는 죽은 느낌"
  - "mobile: shadow 2px로 축소, 복잡한 floating shapes hidden md:block"
  - "prefers-reduced-motion: bounce/wiggle 비활성화"
  - "카드 아이콘 floating circle: half-in half-out of card top border (absolute -top-6)"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**"Stable Grid, Wild Decoration."** Content lives in clean, readable areas; the world around it is alive with movement and shape. Memphis Group (80s) cleaned up for modern screens — removing chaos, keeping energy.

**Vibe:** Friendly, Tactile, Pop, Energetic. A playground or well-organized sticker book. Invites clicking. Smiles at you.

**Visual Signatures:**
- **Primitive Shapes:** Circles, triangles, squares, pills as background/mask elements
- **Hard Shadows:** 4px offset, 0 blur — sticker/cut-out paper feel
- **Pattern Fills:** Polka dots, grid lines, diagonal stripes
- **Varied Radii:** Mixed rounded + sharp creating leaf shapes and blobs

### Colors (Light Mode)
```
background:       #FFFDF5    (Warm Cream — paper feel)
foreground:       #1E293B    (Slate 800)
muted:            #F1F5F9    (Slate 100)
mutedForeground:  #64748B    (Slate 500)
accent:           #8B5CF6    (Vivid Violet — primary brand)
accentForeground: #FFFFFF
secondary:        #F472B6    (Hot Pink)
tertiary:         #FBBF24    (Amber/Yellow)
quaternary:       #34D399    (Emerald/Mint)
border:           #E2E8F0    (Slate 200)
ring:             #8B5CF6
```
**Confetti rule:** Rotate secondary/tertiary/quaternary on decorative shapes and icons — never monochromatic.

### Typography
- **Heading:** `"Outfit", system-ui, sans-serif` — rounded letterforms, 700–800
- **Body:** `"Plus Jakarta Sans", system-ui, sans-serif` — 400–500
Scale: 1.25 Major Third ratio.

### Radius & Borders
```
sm: 8px / md: 16px / lg: 24px / full: 9999px (pill — all primary buttons)
```
**Border default: `border-2` (2px chunky) — thinner loses sticker feel.**

Special: speech bubble `rounded-tl-2xl rounded-tr-2xl rounded-br-2xl rounded-bl-none`, arch `rounded-t-full rounded-b-none`

### Hard Shadows (Zero Blur — The Pop Effect)
```css
Default:     box-shadow: 4px 4px 0px 0px #1E293B;
Hover lift:  box-shadow: 6px 6px 0px 0px #1E293B;
Active press:box-shadow: 2px 2px 0px 0px #1E293B;
Card soft:   box-shadow: 8px 8px 0px 0px #E2E8F0;
Card pink:   box-shadow: 8px 8px 0px 0px #F472B6;
```
**Zero blur always. Blur kills the tactile sticker feel.**

### Textures & Patterns

**Dot grid:**
```css
background-image: radial-gradient(circle, #E2E8F0 1px, transparent 1px);
background-size: 24px 24px;
```

**Squiggle SVG divider:**
```jsx
<svg viewBox="0 0 1200 40" className="w-full" aria-hidden="true">
  <path d="M0,20 Q150,0 300,20 Q450,40 600,20 Q750,0 900,20 Q1050,40 1200,20"
    fill="none" stroke="#8B5CF6" strokeWidth="3" />
</svg>
```

**Confetti shapes:**
```jsx
<div aria-hidden="true" className="absolute top-12 right-8 h-16 w-16 rounded-full bg-[#FBBF24] opacity-60" />
<div aria-hidden="true" className="absolute bottom-20 left-12 rotate-45 h-10 w-10 bg-[#F472B6] opacity-50" />
<div aria-hidden="true" className="absolute top-1/2 right-24 h-8 w-8 bg-[#34D399] opacity-60"
  style={{clipPath: "polygon(50% 0%, 0% 100%, 100% 100%)"}} />
```

**Hero decorations:**
```jsx
{/* Massive yellow circle behind text */}
<div aria-hidden="true" className="absolute -left-20 top-0 h-[500px] w-[500px] rounded-full bg-[#FBBF24]/20 -z-10" />
{/* Dot pattern behind image */}
<div aria-hidden="true" className="absolute inset-0 -z-10"
  style={{backgroundImage: "radial-gradient(circle, #E2E8F0 1px, transparent 1px)", backgroundSize: "20px 20px"}} />
```

### Buttons

**Primary — "The Candy Button":**
```
bg-[#8B5CF6] text-white font-bold rounded-full
border-2 border-[#1E293B]
shadow-[4px_4px_0px_0px_#1E293B]
hover: -translate-x-[2px] -translate-y-[2px] shadow-[6px_6px_0px_0px_#1E293B]
active: translate-x-[2px] translate-y-[2px] shadow-[2px_2px_0px_0px_#1E293B]
transition: all 300ms cubic-bezier(0.34,1.56,0.64,1)
+ ArrowRight in rounded-full bg-white/20 circle inside button
```

**Secondary:** `bg-transparent border-2 border-[#1E293B] rounded-full`, hover: `bg-[#FBBF24]`

All: `focus-visible:ring-2 focus-visible:ring-[#8B5CF6] focus-visible:ring-offset-2`, `min-h-[48px]`

### Cards — "The Sticker Card"
```
bg-white border-2 border-[#1E293B] rounded-xl
shadow-[8px_8px_0px_0px_#E2E8F0]
hover: -rotate-[1deg] scale-[1.02]
transition: all 300ms cubic-bezier(0.34,1.56,0.64,1)
relative overflow-visible
```

**Floating circle icon (half-out of top):**
```jsx
<div className="absolute -top-6 left-6 h-12 w-12 rounded-full bg-[#8B5CF6]
  border-2 border-[#1E293B] flex items-center justify-center
  shadow-[2px_2px_0px_#1E293B]">
  <Icon className="h-5 w-5 text-white" strokeWidth={2.5} />
</div>
```

**Feature grid dashed connector:**
```jsx
<div className="relative">
  <svg className="absolute inset-0 w-full h-full pointer-events-none hidden lg:block" aria-hidden="true">
    <line x1="33%" y1="50%" x2="66%" y2="50%" stroke="#E2E8F0" strokeWidth="2" strokeDasharray="8,6" />
  </svg>
  <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">...</div>
</div>
```

**Pricing badge:**
```jsx
<div className="absolute -top-4 left-1/2 -translate-x-1/2 rotate-[15deg]
  bg-[#FBBF24] text-[#1E293B] font-bold text-xs px-4 py-1 rounded-full
  border-2 border-[#1E293B] shadow-[2px_2px_0px_#1E293B] whitespace-nowrap">
  MOST POPULAR
</div>
```
Featured card: `scale-110`, pink shadow `shadow-[8px_8px_0px_0px_#F472B6]`.

### Inputs
```
bg-white border-2 border-[#CBD5E1] rounded-lg h-12 px-4
placeholder:text-[#94A3B8]
shadow-[4px_4px_0px_0px_transparent]
focus: border-[#8B5CF6] shadow-[4px_4px_0px_0px_#8B5CF6] outline-none
transition: all 200ms ease-out
```
Label: `font-bold uppercase text-sm tracking-wide`

### Icons (lucide-react)
- `strokeWidth={2.5}` — chunky, bold, round line caps
- **Always enclosed in colored circles** — never standalone
- Rotation: `#8B5CF6` → `#F472B6` → `#FBBF24` → `#34D399`

```jsx
<div className="h-10 w-10 rounded-full bg-[#8B5CF6] flex items-center justify-center">
  <Icon className="h-5 w-5 text-white" strokeWidth={2.5} />
</div>
```

### Layout
- Container: `max-w-6xl mx-auto`
- Section: `py-24`
- Grids: `gap-8`, 12-col grouped 6/6 or 4/4/4

### Non-Negotiable Bold Choices
1. **Hard shadow on every interactive element** — 4px/0blur mandatory
2. **border-2 dark border** — thinner loses sticker feel
3. **Bounce easing** `cubic-bezier(0.34,1.56,0.64,1)`
4. **Card hover: rotate + scale wiggle**
5. **Floating circle icons** half-out of card top
6. **4-color confetti rotation** — not monochromatic
7. **MOST POPULAR star badge** rotated 15deg
8. **Squiggle SVG** section divider (not straight hr)
9. **Massive background circle** in hero
10. **Icon always enclosed** in colored shape

### Animation
```css
transition: all 300ms cubic-bezier(0.34, 1.56, 0.64, 1);

@keyframes wiggle {
  0%, 100% { transform: rotate(0deg); }
  33%       { transform: rotate(3deg); }
  66%       { transform: rotate(-3deg); }
}
@keyframes pop-in {
  0%   { transform: scale(0); opacity: 0; }
  70%  { transform: scale(1.1); opacity: 1; }
  100% { transform: scale(1); }
}
```
`prefers-reduced-motion`: disable bounce/wiggle, use `ease-out`.

### Responsive
- Mobile: stack all, shadow 2px, hide floating shapes (`hidden md:block`)
- Touch targets: `h-12` minimum
- Keep: hard shadows (reduced), bright colors, Outfit font, enclosed icons

### Accessibility
- `#1E293B` on `#FFFDF5`: AAA
- Focus: `ring-2 ring-[#8B5CF6] ring-offset-2`
- Shape + label (never color alone)
- Decorative elements: `aria-hidden="true"`

</design-system>
