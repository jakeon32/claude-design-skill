# Minimalist Dark Design System
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#0A0A0F", bg_alt: "#12121A", fg: "#FAFAFA", muted: "#1A1A24", muted_fg: "#71717A", accent: "#F59E0B", accent_fg: "#0A0A0F", accent_muted: "rgba(245,158,11,0.15)", border: "rgba(255,255,255,0.08)", border_hover: "rgba(255,255,255,0.15)", card: "rgba(26,26,36,0.6)", card_solid: "#1A1A24", ring: "#F59E0B" }
typography: { heading: "Space Grotesk (geometric, technical, distinctive)", body: "Inter (clean, highly readable)", mono: "JetBrains Mono (code/labels/metadata)", weight: "medium 500-semibold 600 headings / 400-500 body", size_hero: "text-5xl–text-7xl (56-96px)", tracking: "tracking-tight headings / tracking-normal body / tracking-wide mono labels", leading: "leading-tight headings / leading-relaxed body" }
style_traits: [대기감(Atmospheric) 다크, Premium developer tool 미학, 3단 레이어드 슬레이트 (#0A0A0F→#12121A→#1A1A24), 앰버 #F59E0B 따뜻한 단일 액센트, 글래스 카드 backdrop-blur-8px, ambient orb 배경 글로우]
radius: { sm: "6px", md: "8px (기본)", lg: "12px (cards/containers)", xl: "16px (hero elements)", xxl: "24px (special decorative)", full: "9999px (pill/avatar)" }
shadow: "ambient glow — harsh drop shadow 금지 / glow-sm: 0 0 20px rgba(245,158,11,0.15) / glow-md: 0 0 40px rgba(245,158,11,0.2) / glow-lg: 0 0 60px rgba(245,158,11,0.25) / border-glow: 0 0 0 1px rgba(245,158,11,0.3)+0 0 20px rgba(245,158,11,0.15) / btn-hover: 0 0 20px rgba(245,158,11,0.4)"
border: "1px solid rgba(255,255,255,0.08) 기본 — hover: rgba(255,255,255,0.15) — featured: rgba(245,158,11,0.2) — 두꺼운 border 절대 금지"
effects:
  glass_card: "bg: rgba(26,26,36,0.6) + backdrop-blur-[8px] + border rgba(255,255,255,0.08)"
  ambient_orbs: "large blurred circle bg-[#F59E0B] opacity-[0.02-0.04] blur-[100px-150px] — absolute positioned hero/sections"
  noise_texture: "SVG noise opacity-[0.015-0.02] fixed overlay"
  radial_ambience: "radial-gradient(ellipse at top, rgba(245,158,11,0.03) 0%, transparent 50%) — section bg"
  grid_pattern: "linear-gradient rgba(255,255,255,0.02) 1px 40px — optional for specific sections"
  pulse_dot: "animate-pulse + amber glow — hero badge live indicator"
animation:
  timing: "200ms ease-out (buttons/quick) / 300ms ease-out (cards)"
  hover_card: "scale-[1.02] + border rgba(255,255,255,0.15) + bg rgba(26,26,36,0.8) + shadow"
  hover_btn: "brightness-110 + glow 0 0 20px rgba(245,158,11,0.4)"
  active_btn: "scale-[0.98] — subtle press"
  faq: "max-h + opacity fade smooth height transition"
  no_bounce: "dramatic transforms/bounce 금지 — gentle fades + soft glows + subtle scales"
layout: [max-w-6xl, px-6 md:px-8 lg:px-12, py-24 md:py-32 lg:py-40 (very generous), gap-6 or gap-8 grids]
components:
  button_primary: "bg-[#F59E0B] text-[#0A0A0F] font-medium rounded-lg h-11 px-6, hover:brightness-110 + shadow 0 0 20px rgba(245,158,11,0.4), active:scale-[0.98], focus-visible:ring-2 ring-[#F59E0B] ring-offset-2"
  button_outline: "transparent bg, border border-white/15 text-[#FAFAFA], hover:bg-white/5 hover:border-white/25, active:scale-[0.98]"
  button_ghost: "transparent no border, hover:bg-white/5"
  cards: "bg rgba(26,26,36,0.6) backdrop-blur-[8px] border border-white/[0.08] rounded-xl, hover:scale-[1.02] hover:border-white/15 hover:bg rgba(26,26,36,0.8) 300ms ease-out"
  cards_featured: "border-[#F59E0B]/20 + box-shadow: 0 0 0 1px rgba(245,158,11,0.2)+0 0 30px rgba(245,158,11,0.15)"
  inputs: "bg rgba(26,26,36,0.6) backdrop-blur-[8px] border-white/[0.08] rounded-lg h-11 text-[#FAFAFA] placeholder:text-[#71717A], focus: border-amber-500/50 ring-2 ring-amber-500/20 shadow 0 0 20px rgba(245,158,11,0.1)"
  icons: "lucide strokeWidth={1.5}, size 20px, text-zinc-400 default / text-amber-500 accent state"
special_notes:
  - "3단 레이어드 다크 필수 — #0A0A0F/12121A/1A1A24 모두 visible"
  - "pure black #000 / cold blue 절대 금지 — warm slate + amber only"
  - "ambient glow = 이 스타일의 DNA — 없으면 generic dark theme"
  - "glass card backdrop-blur 필수 — solid bg 사용시 깊이 소멸"
  - "ambient orbs (opacity 0.02-0.04 blur 100-150px) 필수 — flat bg 금지"
  - "border는 rgba(255,255,255,0.08) 8% opacity max — harsh border 금지"
  - "btn hover glow 0.4 opacity / card hover glow 0.15 opacity 구분"
  - "active:scale-[0.98] press 필수 — bounce 금지"
  - "Space Grotesk + Inter + JetBrains Mono 3폰트 스택 필수"
  - "section py-24→py-40 generous — cramped 금지"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Atmospheric Depth.** Visual interest through carefully orchestrated layers of darkness — not color saturation or complex patterns. Warm amber accents glow like embers against cool slate. The design breathes.

**Vibe:** Atmospheric, Sophisticated, Calm, Premium, Nocturnal. Using Linear or Raycast at night. A beautifully designed app at 2am. The quiet confidence of well-crafted software.

**NOT:** Pure black, harsh contrast, vibrant colors, flat/shadowless, generic dark mode.

**DNA:** Layered slate palette + warm amber single accent + ambient glow effects + glass cards + geometric sans type + generous breathing room + very subtle borders.

### Colors (Dark Slate + Amber)
```
background:       #0A0A0F  (Deep slate — not pure black, warmer)
backgroundAlt:    #12121A  (Slightly elevated)
foreground:       #FAFAFA  (Near-white — 18.4:1 AAA)
muted:            #1A1A24  (Card bg / elevated surfaces)
mutedForeground:  #71717A  (Secondary text — 4.9:1 AA)
accent:           #F59E0B  (Amber-500 — warm, glowing, the single accent)
accentForeground: #0A0A0F  (Dark text on amber)
accentMuted:      rgba(245,158,11,0.15)
border:           rgba(255,255,255,0.08)   (8% — barely there)
borderHover:      rgba(255,255,255,0.15)
card:             rgba(26,26,36,0.6)       (semi-transparent glass)
cardSolid:        #1A1A24
ring:             #F59E0B
```
**All shadows and glows use amber tint — no cold blue glows.**

### Typography
- **Display/Headlines:** `"Space Grotesk", system-ui, sans-serif` — geometric, technical, distinctive
- **Body:** `"Inter", system-ui, sans-serif` — clean, readable
- **Mono:** `"JetBrains Mono", monospace` — code, labels, metadata

| Role | Size | Notes |
|:-----|:-----|:------|
| Hero H1 | `text-5xl md:text-6xl lg:text-7xl` | `tracking-tight font-semibold` |
| Section H2 | `text-3xl md:text-4xl md:text-5xl` | `tracking-tight` |
| H3 | `text-xl md:text-2xl` | `font-medium` |
| Body | `text-base md:text-lg` | `leading-relaxed text-[#71717A]` |
| Labels | `text-sm` | `font-mono tracking-wide` |

### Radius
```
sm:   6px          — small elements
md:   8px          — default for most
lg:   12px         — cards, containers
xl:   16px         — hero elements
2xl:  24px         — special decorative
full: 9999px       — pills, avatars
```

### Shadows & Ambient Glows
```css
/* No harsh drop shadows. Only soft ambient glows. */

/* Ambient glow tokens */
--glow-sm: 0 0 20px rgba(245,158,11,0.15);
--glow-md: 0 0 40px rgba(245,158,11,0.2);
--glow-lg: 0 0 60px rgba(245,158,11,0.25);

/* Button hover glow */
--glow-btn: 0 0 20px rgba(245,158,11,0.4);

/* Featured card border glow */
--border-glow: 0 0 0 1px rgba(245,158,11,0.2), 0 0 30px rgba(245,158,11,0.15);

/* Dark elevation (minimal) */
--shadow-card: 0 10px 15px rgba(0,0,0,0.3);
```

### Textures & Atmospheric Effects (Required)

**Ambient orbs (hero + major sections — mandatory):**
```jsx
{/* Behind hero content */}
<div aria-hidden="true"
  className="pointer-events-none fixed inset-0 overflow-hidden">
  <div className="absolute -top-40 left-1/2 -translate-x-1/2
    h-[600px] w-[600px] md:h-[800px] md:w-[800px]
    rounded-full bg-[#F59E0B] opacity-[0.03] blur-[120px]" />
  <div className="absolute bottom-0 right-0
    h-[400px] w-[400px]
    rounded-full bg-[#F59E0B] opacity-[0.02] blur-[150px]" />
</div>
```

**Noise texture overlay:**
```jsx
<div aria-hidden="true"
  className="pointer-events-none fixed inset-0 opacity-[0.015]"
  style={{backgroundImage: "url('data:image/svg+xml,...noise...')"}} />
```

**Radial ambience (section bg):**
```css
background: radial-gradient(ellipse at top, rgba(245,158,11,0.03) 0%, transparent 50%);
```

**Subtle grid (optional):**
```css
background-image:
  linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
  linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
background-size: 40px 40px;
```

### Glass Cards (The Signature)
```css
/* Standard card */
background: rgba(26, 26, 36, 0.6);
backdrop-filter: blur(8px);
border: 1px solid rgba(255, 255, 255, 0.08);
border-radius: 12px;
transition: all 300ms ease-out;

/* Hover */
border-color: rgba(255, 255, 255, 0.15);
background: rgba(26, 26, 36, 0.8);
transform: scale(1.02);
box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);

/* Featured card */
border: 1px solid rgba(245, 158, 11, 0.2);
box-shadow: 0 0 0 1px rgba(245,158,11,0.2), 0 0 30px rgba(245,158,11,0.15);
```

### Buttons

**Primary (amber):**
```
bg-[#F59E0B] text-[#0A0A0F] font-medium rounded-lg
h-11 px-6 (no uppercase, no tracking-widest)
hover: brightness-110 + shadow-[0_0_20px_rgba(245,158,11,0.4)]
active: scale-[0.98]
transition: all 200ms ease-out
focus-visible: ring-2 ring-[#F59E0B] ring-offset-2 ring-offset-[#0A0A0F]
```

**Outline:**
```
transparent bg, border border-white/15 text-[#FAFAFA] rounded-lg h-11 px-6
hover: bg-white/5 border-white/25
active: scale-[0.98]
```

**Ghost:** transparent, no border, hover: `bg-white/5`

### Inputs
```
bg: rgba(26,26,36,0.6) backdrop-blur-[8px]
border: 1px solid rgba(255,255,255,0.08) rounded-lg
h-11 px-4 text-[#FAFAFA] placeholder:text-[#71717A]
focus: border-amber-500/50 ring-2 ring-amber-500/20
      shadow-[0_0_20px_rgba(245,158,11,0.1)]
      outline-none
transition: all 200ms ease-out
```

### Icons (lucide-react)
- `strokeWidth={1.5}` — thin, elegant, not attention-grabbing
- Size: `20px` standard
- Default: `text-zinc-400` — subtle, supporting
- Accent state: `text-amber-500`

### Layout
- Container: `max-w-6xl mx-auto px-6 md:px-8 lg:px-12`
- Sections: `py-24 md:py-32 lg:py-40` — extremely generous
- Grid gaps: `gap-6` or `gap-8`
- 2-col: `lg:grid-cols-2`, 3-col: `md:grid-cols-3`

### Non-Negotiable Bold Choices
1. **3 distinct dark layers** — `#0A0A0F` / `#12121A` / `#1A1A24` all visible
2. **Amber is the ONLY accent** — no blue, no purple, no other colors
3. **Ambient glow orbs** — hero + background, fixed, blurred 100-150px
4. **Glass cards with backdrop-blur** — never solid opaque cards
5. **Ambient glow on btn hover** — 0.4 opacity (not just color change)
6. **Borders at 8% opacity** — `rgba(255,255,255,0.08)` only
7. **active:scale-[0.98]** — subtle press on all buttons
8. **Space Grotesk** for all display/headlines
9. **Noise + radial gradient** atmospheric textures mandatory
10. **py-40 maximum breathing room** — cramped layouts break the premium feel

### Animation
```css
/* Cards */
transition: all 300ms ease-out;

/* Buttons & interactions */
transition: all 200ms ease-out;

/* Never: bounce, spring, dramatic transforms */
/* Yes: gentle glow increase, subtle scale, smooth fades */
```

`@keyframes pulse` — animate-pulse for hero badge dot + amber glow.
FAQ: max-height + opacity transition for smooth accordion.

### Responsive
- Hero: `text-4xl sm:text-5xl md:text-6xl lg:text-7xl`
- Ambient orbs: `h-[400px] md:h-[600px]` (smaller on mobile for performance — but KEEP them)
- Glass effects maintained on mobile (backdrop-blur is performant)
- `py-24 md:py-32 lg:py-40` — spacing scales but stays generous
- Touch targets: `h-11` minimum (44px)
- Stack all columns on mobile

### Accessibility
- `#FAFAFA` on `#0A0A0F`: 18.4:1 AAA ✓
- `#71717A` on `#0A0A0F`: 4.9:1 AA ✓
- Focus: `ring-2 ring-[#F59E0B] ring-offset-2 ring-offset-[#0A0A0F]`
- Links nav: `focus-visible:text-[#F59E0B]`
- Decorative elements (orbs, textures): `aria-hidden="true" pointer-events-none`

</design-system>
