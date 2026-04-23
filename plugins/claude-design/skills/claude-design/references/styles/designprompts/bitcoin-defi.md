# Bitcoin DeFi Design System
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#030304", surface: "#0F1115", fg: "#FFFFFF", muted: "#94A3B8", border: "#1E293B", accent: "#F7931A", accent_secondary: "#EA580C", accent_tertiary: "#FFD600" }
typography: { heading: "Space Grotesk (geometric grotesque, h1-h6)", body: "Inter (body/buttons/descriptions)", mono: "JetBrains Mono (stats/prices/badges/labels)", weight: "700 bold headings / 400-600 body / 400-500 mono", size_hero: "text-4xl sm:text-5xl md:text-7xl", tracking: "tracking-tight headings / tracking-wider uppercase mono labels / tracking-widest button", leading: "leading-tight headings / leading-relaxed body" }
style_traits: [비트코인/DeFi 정밀 공학 미학, True Void 우주 배경+Bitcoin Fire 에너지, 컬러드 오렌지/골드 글로우 섀도우(블랙 섀도우 금지), 글래스모피즘 플로팅 패널, 스피닝 오비탈 링 히어로, 블록체인 그리드 패턴]
radius: { cards: "rounded-2xl (16px) / rounded-xl (12px)", buttons: "rounded-full (pill 필수)", inputs: "rounded-lg (8px) or bottom-border only", small: "rounded-lg or rounded-full (badges/icons)" }
shadow: "컬러드 글로우만 — pure black shadow 절대 금지 / orange: 0 0 20px -5px rgba(234,88,12,0.5) / gold: 0 0 20px rgba(255,214,0,0.3) / card hover: 0 0 30px -10px rgba(247,147,26,0.2) / card ambient: 0 0 50px -10px rgba(247,147,26,0.1)"
border: "border-white/10 기본 → hover: border-[#F7931A]/50 → active: border-[#F7931A] full"
effects:
  grid_pattern: "linear-gradient(to right, rgba(30,41,59,0.5) 1px, transparent 1px) + to bottom same — 50px 50px + mask-image radial-gradient(circle at center, black 40%, transparent 100%)"
  radial_blur_blobs: "bg-[#F7931A] opacity-10 blur-[120px] absolute — ambient orange glow blobs"
  glass_morphism: "backdrop-blur-lg + bg-white/5 or bg-black/40 + border-white/10"
  gradient_text: "bg-gradient-to-r from-[#F7931A] to-[#FFD600] bg-clip-text text-transparent — hero headline 마지막 1-2단어"
  gradient_btn: "linear-gradient(to right, #EA580C, #F7931A) or (#F7931A, #FFD600)"
  corner_accents: "border-t border-l (top-left) + border-r border-b (bottom-right) in [#F7931A] — How It Works cards"
  icon_watermark: "opacity-20 → opacity-100 group-hover (rotated large bg icon in card)"
animation:
  float: "@keyframes float { 0%,100%{translateY(0)} 50%{translateY(-20px)} } — 8s ease-in-out infinite — hero orb"
  spin_orbital: "animate-[spin_10s_linear_infinite] outer ring + animate-[spin_15s_linear_infinite_reverse] inner — 3D depth illusion"
  bounce_cards: "animate-bounce 3s/4s delay-1s — floating stat cards around orb"
  ping_badge: "animate-ping — live network status indicators"
  timing: "duration-200–duration-300 hover/focus — snappy, precise, trading-terminal feel"
  hover_card: "hover:-translate-y-1 + border color shift + glow intensify 300ms"
  hover_btn: "hover:scale-105 + glow spread"
layout: [max-w-7xl 1280px, py-24 96px sections, gap-8–gap-12 grids, single-col mobile → md:grid-cols-3 desktop, no hr dividers — alternating bg + spacing only]
components:
  button_primary: "bg-gradient-to-r from-[#EA580C] to-[#F7931A] text-white font-bold uppercase tracking-wider rounded-full h-11+ px-6, shadow: 0 0 20px -5px rgba(234,88,12,0.5), hover:scale-105 + intensified glow"
  button_outline: "transparent bg, border-2 border-white/20 text-white, hover: border-white + bg-white/10"
  button_ghost: "transparent no border, hover: bg-white/10 text-[#F7931A]"
  button_link: "text-[#F7931A] hover:underline"
  cards_standard: "bg-[#0F1115] border-white/10 rounded-2xl p-8, hover:-translate-y-1 border-[#F7931A]/50 + orange glow"
  cards_glass: "bg-black/40 or bg-white/5, backdrop-blur-lg, border-white/10"
  cards_pricing: "featured: scale-105 border-[#F7931A] z-10 shadow-[0_0_40px_-10px_rgba(247,147,26,0.15)] / others: opacity-80 hover:scale-105"
  inputs: "bg-black/50, border-b-2 border-white/20 (bottom only), h-12 px-4, text-white text-sm, placeholder:text-white/30, focus:border-[#F7931A] + bottom glow shadow"
  icons: "lucide default stroke, text-[#F7931A]/[#EA580C]/[#FFD600]/white, container: bg-[#EA580C]/20 border-[#EA580C]/50 rounded-lg p-3 + hover:glow"
  stat_ticker: "border-y border-white/10, font-mono, live ping badge"
special_notes:
  - "gradient text bg-clip-text 히어로 헤드라인 마지막 단어 필수"
  - "spinning orbital rings 히어로 필수 — 10s + 15s reverse"
  - "컬러드 글로우 섀도우만 — 모든 shadow에 orange/gold tint 필수"
  - "그리드 패턴 히어로 배경 + mask-image vignette 필수"
  - "radial blur blobs 앰비언트 라이팅 — absolute positioned 다수"
  - "rounded-full 버튼 필수 — 어떤 버튼도 sharp/squared 없음"
  - "border: 기본 white/10 → hover orange/50 → active orange 100% 패턴"
  - "pure black shadow 절대 금지 — orange/gold tint only"
  - "font-mono JetBrains Mono — stats/prices/labels/badges 전용"
  - "animate-ping live badge 필수 — blockchain network activity 표현"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Bitcoin/DeFi precision engineering meets digital gold.** True Void darkness where Bitcoin orange and digital gold illuminate data structures. Not generic dark mode — a cosmic void where light emanates from interactive elements themselves.

**5 Core Principles:**
1. **Luminescent Energy:** Colored glows (orange/gold) — shadows are never black, they're warm tinted light
2. **Mathematical Precision:** Ultra-thin 1px borders, monospace data fonts, strict grid structure
3. **Layered Depth:** Glass morphism + colored glow shadows + backdrop blur — digital Z-space
4. **Textured Void:** Grid patterns, radial blur blobs, noise — backgrounds breathe
5. **Trust Through Design:** High contrast, technical precision — "your assets are safe here"

**Vibe:** Secure, Technical, Valuable. Bitcoin mining rigs humming in darkness, glowing with orange heat.

### Colors
```
background:  #030304   (True Void — deepest space)
surface:     #0F1115   (Dark Matter — cards/panels)
foreground:  #FFFFFF   (Pure Light — 21:1 on bg AAA)
muted:       #94A3B8   (Stardust — secondary text)
border:      #1E293B   (Dim Boundary — often at white/10 opacity)
accent:      #F7931A   (Bitcoin Orange — primary CTA/links/active)
secondary:   #EA580C   (Burnt Orange — gradients/depth)
tertiary:    #FFD600   (Digital Gold — value/highlights/success)
```
**Gradient formula:** `from-[#EA580C] to-[#F7931A]` or `from-[#F7931A] to-[#FFD600]`

### Typography
- **Heading:** `"Space Grotesk"` — geometric grotesque with quirky technical character
- **Body:** `"Inter"` — screen-optimized legibility
- **Mono/Data:** `"JetBrains Mono"` — stats, prices, badges, labels (technical precision)

| Role | Size | Notes |
|:-----|:-----|:------|
| Hero H1 | `text-4xl sm:text-5xl md:text-7xl` | `font-bold leading-tight` |
| Section H2 | `text-2xl md:text-4xl md:text-5xl` | `font-semibold` |
| Body | `text-base md:text-lg` | `leading-relaxed` |
| Data labels | `text-sm` | `font-mono uppercase tracking-wider` |
| Button | any | `font-semibold uppercase tracking-widest` |

**Gradient text (hero — mandatory):**
```
bg-gradient-to-r from-[#F7931A] to-[#FFD600] bg-clip-text text-transparent
— apply to last 1-2 words of hero headline only
```

### Radius & Borders
```
Cards:    rounded-2xl (16px) or rounded-xl (12px)
Buttons:  rounded-full — pill shape, ALL buttons, no exceptions
Inputs:   rounded-lg (8px) or bottom-border only (minimalist)
Badges:   rounded-full or rounded-lg
```

**Border state system:**
```
Rest:   border border-white/10    (barely visible)
Hover:  border-[#F7931A]/50       (orange at 50%)
Active: border-[#F7931A]          (full intensity)
```

### Colored Glow Shadows (No Black Shadows)
```css
/* Orange glow — primary */
shadow-[0_0_20px_-5px_rgba(234,88,12,0.5)]
hover: shadow-[0_0_30px_-5px_rgba(247,147,26,0.6)]

/* Gold glow — highlights */
shadow-[0_0_20px_rgba(255,214,0,0.3)]

/* Card ambient */
shadow-[0_0_50px_-10px_rgba(247,147,26,0.1)]

/* Card hover */
shadow-[0_0_30px_-10px_rgba(247,147,26,0.2)]
```
**NEVER use pure black box-shadow. All shadows carry orange or gold tint.**

### Textures & Patterns (Required)

**Grid pattern (hero — mandatory):**
```css
.bg-grid-pattern {
  background-size: 50px 50px;
  background-image:
    linear-gradient(to right, rgba(30,41,59,0.5) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(30,41,59,0.5) 1px, transparent 1px);
  mask-image: radial-gradient(circle at center, black 40%, transparent 100%);
}
```

**Radial blur blobs (ambient glow — multiple per section):**
```jsx
<div className="absolute top-1/4 right-0 w-96 h-96 bg-[#F7931A] opacity-10 blur-[120px] rounded-full pointer-events-none" />
<div className="absolute bottom-0 left-1/4 w-64 h-64 bg-[#EA580C] opacity-10 blur-[150px] rounded-full pointer-events-none" />
```

**Glass morphism:**
```
bg-black/40 or bg-white/5
backdrop-blur-lg or backdrop-blur-sm
border border-white/10
```

### Buttons

**Primary (Bitcoin orange gradient):**
```
bg-gradient-to-r from-[#EA580C] to-[#F7931A]
text-white font-semibold uppercase tracking-widest
rounded-full h-11 px-6 md:px-8
shadow-[0_0_20px_-5px_rgba(234,88,12,0.5)]
hover:scale-105 hover:shadow-[0_0_30px_-5px_rgba(247,147,26,0.6)]
transition-all duration-300
```

**Outline:** `border-2 border-white/20 text-white`, hover: `border-white bg-white/10`

**Ghost:** no border, hover: `bg-white/10 text-[#F7931A]`

**Link:** `text-[#F7931A]` hover: underline

All: `focus-visible:ring-2 focus-visible:ring-[#F7931A] focus-visible:ring-offset-2 focus-visible:ring-offset-[#030304]`

### Cards

**Standard:**
```
bg-[#0F1115] border border-white/10 rounded-2xl p-8
hover:-translate-y-1 hover:border-[#F7931A]/50
hover:shadow-[0_0_30px_-10px_rgba(247,147,26,0.2)]
transition-all duration-300
```

**Glass:**
```
bg-black/40 backdrop-blur-lg border border-white/10 rounded-2xl
```

**Featured pricing:**
```
scale-105 border-[#F7931A] z-10
shadow-[0_0_40px_-10px_rgba(247,147,26,0.15)]
```
Other tiers: `opacity-80`, `hover:scale-105 hover:opacity-100`

**Corner accent pattern (How It Works):**
```jsx
{/* Top-left */}
<div className="absolute top-0 left-0 w-6 h-6 border-t border-l border-[#F7931A]" />
{/* Bottom-right */}
<div className="absolute bottom-0 right-0 w-6 h-6 border-b border-r border-[#F7931A]" />
```

**Icon watermark (feature cards):**
```jsx
<div className="absolute bottom-4 right-4 opacity-20 group-hover:opacity-100 transition-opacity duration-300">
  <Icon className="h-16 w-16 text-[#F7931A] rotate-12" />
</div>
```

### Inputs
```
bg-black/50 border-b-2 border-white/20 (bottom border only)
h-12 px-4 py-2 text-white text-sm placeholder:text-white/30
focus-visible:border-[#F7931A]
focus-visible:shadow-[0_10px_20px_-10px_rgba(247,147,26,0.3)]
focus-visible:outline-none
transition-all duration-200
```

### Icons (lucide-react)
- Orange: `text-[#F7931A]` / Gold: `text-[#FFD600]` / Muted: `text-[#94A3B8]`
- Container: `bg-[#EA580C]/20 border border-[#EA580C]/50 rounded-lg p-3`
- Hover: `hover:shadow-[0_0_20px_rgba(234,88,12,0.4)]`
- Watermark in cards: large, rotated, `opacity-20 group-hover:opacity-100`

### Layout
- Container: `max-w-7xl mx-auto`
- Sections: `py-24` (96px) — generous breathing room
- Grids: `gap-8` to `gap-12`, single-col → `md:grid-cols-2` → `md:grid-cols-3`
- **No `<hr>` dividers** — section separation via spacing + alternating `bg-[#030304]` ↔ `bg-[#0F1115]`
- Stats ticker: `border-y border-white/10` with monospace data + `animate-ping` dots

### Non-Negotiable Bold Choices
1. **Gradient text** on hero headline final words — `from-[#F7931A] to-[#FFD600] bg-clip-text`
2. **Spinning orbital rings** in hero — 10s spin + 15s reverse inner ring
3. **Floating bounce cards** around hero orb — staggered `animate-bounce` 3s/4s
4. **All shadows orange/gold tinted** — never black
5. **Corner border accents** on How It Works cards
6. **Background icon watermarks** — reveal on group-hover
7. **Pulsing `animate-ping` badges** — live network status
8. **Asymmetric pricing scale** — featured `scale-105`, others `opacity-80`
9. **Grid pattern + mask-image vignette** on hero
10. **Radial blur blobs** multiple per major section

### Animation
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
/* Hero orb: animation: float 8s ease-in-out infinite */

/* Outer ring */ animation: spin 10s linear infinite;
/* Inner ring */ animation: spin 15s linear infinite reverse;

/* Stat cards */ animate-bounce (custom 3s, 4s duration + delay-1s stagger)
/* Live badge */ animate-ping
```

Interaction speed: `duration-200`–`duration-300`. Snappy, no spring, trading-terminal precision.

### Responsive
- Hero: `text-4xl sm:text-5xl md:text-7xl` — dramatic scaling
- Orb graphic: `h-[300px] md:h-[450px]`
- Grids: single-col → `md:grid-cols-2/3`
- Pricing: stack on mobile, 3-col + scale on md+
- Touch targets: `h-10` minimum (40px), `h-11` preferred
- Grid patterns + glows persist on mobile — don't strip personality

### Accessibility
- `#FFFFFF` on `#030304`: 21:1 AAA ✓
- `#F7931A` on dark: AA for large text ✓
- Focus: `ring-2 ring-[#F7931A] ring-offset-2 ring-offset-[#030304]`
- `prefers-reduced-motion`: disable float/spin/bounce animations
- Decorative blobs/patterns: `aria-hidden="true" pointer-events-none`

</design-system>
