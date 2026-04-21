# High-Fidelity Claymorphism Design System
source: designprompts.dev
category: light

```yaml
palette: { bg: "#F4F1FA", fg: "#332F3A", muted_fg: "#635F69", accent: "#7C3AED", accent_secondary: "#DB2777", tertiary: "#0EA5E9", success: "#10B981", warning: "#F59E0B", card_bg: "rgba(255,255,255,0.6-0.8)" }
typography: { heading: "Nunito (700/800/900 — rounded terminals, clay-perfect)", body: "DM Sans (400/500/700 — geometric clean)", weight: "font-black 900 (hero/stats) / font-extrabold 800 (section titles) / font-bold 700 (cards)", size_hero: "text-5xl sm:text-6xl md:text-7xl lg:text-8xl", leading: "leading-[1.1] (display) / leading-relaxed 1.625 (body)" }
style_traits: [프리미엄 디지털 클레이 물성, 4레이어 복합 섀도우 (물리 라이팅 시뮬레이션), 슈퍼-라운드 최소 20px, 캔디스토어 비비드 팔레트, animated blob 배경, 클레이 물리: 볼록/오목/부력/마이크로물리]
radius: { large_container: "48px–60px", standard_card: "32px (기본)", medium: "24px (benefits/blog)", button_input: "20px or rounded-2xl", icon_square: "rounded-2xl (16px)", icon_circle: "rounded-full", badge: "rounded-full preferred", orb: "rounded-full" }
shadow:
  clay_deep: "30px 30px 60px #cdc6d9, -30px -30px 60px #ffffff, inset 10px 10px 20px rgba(139,92,246,0.05), inset -10px -10px 20px rgba(255,255,255,0.8)"
  clay_card: "16px 16px 32px rgba(160,150,180,0.2), -10px -10px 24px rgba(255,255,255,0.9), inset 6px 6px 12px rgba(139,92,246,0.03), inset -6px -6px 12px rgba(255,255,255,1)"
  clay_button: "12px 12px 24px rgba(139,92,246,0.3), -8px -8px 16px rgba(255,255,255,0.4), inset 4px 4px 8px rgba(255,255,255,0.4), inset -4px -4px 8px rgba(0,0,0,0.1)"
  clay_pressed: "inset 10px 10px 20px #d9d4e3, inset -10px -10px 20px #ffffff"
  hover_enhanced: "clay_card + 더 큰 offset / button: hover shadow amplify"
effects:
  animated_blobs: "fixed -z-10 h-[60vh] w-[60vh] rounded-full blur-3xl — accent colors /10 opacity — clay-float 8-12s animation — 3-4개 필수"
  glass_clay: "bg-white/60–bg-white/80 + backdrop-blur-xl + shadow-clayCard"
  gradient_btn: "bg-gradient-to-br from-[#A78BFA] to-[#7C3AED] — lighter-to-darker depth"
  gradient_icon: "bg-gradient-to-br from-blue-400 to-blue-600 (각 아이콘 다른 색 조합)"
  gradient_text: "clay-text-gradient from-clay-fg 20% to-clay-accent 60% — text-5xl+ 이상만"
  clay_breathe: "@keyframes clay-breathe { 0%,100%{scale:1} 50%{scale:1.02} } 6s — stat orbs"
animation:
  clay_float: "@keyframes { 0%,100%{translateY(0) rotate(0)} 50%{translateY(-20px) rotate(2deg)} } — 8s"
  clay_float_delayed: "translateY(-15px) rotate(-2deg) — 10s alt rotation"
  clay_float_slow: "translateY(-30px) rotate(5deg) — 12s hero decorative"
  hover_lift_card: "hover:-translate-y-2 duration-500 + shadow enhance"
  hover_lift_btn: "hover:-translate-y-1 duration-200 + shadow enhance"
  active_squish: "active:scale-[0.92] active:shadow-clayPressed — 200ms — 물리 버튼 클릭"
  stagger: "animation-delay-2000 / animation-delay-4000 — blob stagger"
  breathe: "clay-breathe 6s ease-in-out infinite — stat orbs"
layout: [bento grid (col-span-2 row-span-2 mix), split 50/50 product sections, overlapping badges, negative margin decoratives, max-w-6xl or 7xl]
components:
  button_primary: "bg-gradient-to-br from-[#A78BFA] to-[#7C3AED] text-white font-bold rounded-[20px] h-14 px-8, shadow-clayButton, hover:-translate-y-1 + shadow enhance, active:scale-[0.92] active:shadow-clayPressed, focus-visible:ring-4 ring-[#7C3AED]/30"
  button_secondary: "bg-white text-[#332F3A] shadow-clayButton rounded-[20px] h-14"
  button_outline: "border-2 border-[#7C3AED]/20 text-[#7C3AED] rounded-[20px] h-14, hover:border-[#7C3AED] hover:bg-[#7C3AED]/5"
  cards: "relative overflow-hidden rounded-[32px] bg-white/60 p-8 backdrop-blur-xl shadow-clayCard, hover:-translate-y-2 duration-500"
  cards_hero: "md:col-span-2 md:row-span-2 — bento hero card"
  inputs: "rounded-2xl h-16 bg-[#EFEBF5] px-6 py-4 shadow-clayPressed border-0, focus:bg-white focus:ring-4 focus:ring-[#7C3AED]/20 transition-all duration-200"
  stat_orbs: "rounded-full shadow-clayCard clay-breathe animation, hover:scale-110"
  icon_containers: "rounded-2xl bg-gradient-to-br (varied per icon) — never flat solid"
special_notes:
  - "4레이어 섀도우 필수 — flat shadow 사용시 clay 느낌 소멸"
  - "rounded-md/rounded-lg 절대 금지 — 최소 rounded-[20px]"
  - "animated blobs 3-4개 fixed 배경 필수 — flat background 금지"
  - "active:scale-[0.92] + shadow-clayPressed squish 필수"
  - "Nunito 폰트 headings에 inline style 필수 — TW font-family 우선순위 낮음"
  - "gradient text: text-5xl+ 이상만 — 작은 사이즈 가독성 불가"
  - "muted text 최소 #635F69 — 더 밝은 gray 접근성 위반"
  - "glass-clay: bg-white/60–/80 + backdrop-blur-xl 조합 — 블롭 투과"
  - "hover:-translate-y 필수 — 모든 interactive elements"
  - "prefers-reduced-motion으로 모든 애니메이션 비활성화 처리"
  - "superdesign/hifi-claymorphism.md와 동일 컨셉이지만 designprompts.dev 버전"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**Premium digital clay.** Every element evokes holding a high-end matte-finish vinyl toy or soft silicone object. Rejects flatness in favor of volume, weight, and tactility. Complex multi-layered lighting simulation through 4-layer shadow stacks.

**Vibe:** Playful, Optimistic, Tactile, Responsive. Candy store colors. Bouncy organic motion. Zero sharp corners — subconsciously signals safety and friendliness.

**Clay Physics Engine:**
1. **Convexity (Bulge):** Buttons/cards bulge OUT with `shadow-clayButton` — captures top-left light
2. **Concavity (Press):** Inputs/active states pressed INTO surface with `shadow-clayPressed`
3. **Buoyancy (Float):** Zero-gravity environment — blobs drift (8-12s), cards hover on lift
4. **Micro-Physics:** Hover lifts up, active presses down — physical feedback every time

### Colors (Candy Shop Palette)
```
background:  #F4F1FA   (Cool lavender-white — never pure white)
foreground:  #332F3A   (Soft Charcoal — softer than black)
mutedFg:     #635F69   (Dark Lavender-Gray — MINIMUM, never lighter for accessibility)
accent:      #7C3AED   (Vivid Violet — primary CTA/links)
secondary:   #DB2777   (Hot Pink — gradients/secondary)
tertiary:    #0EA5E9   (Sky Blue — info/blobs)
success:     #10B981   (Emerald)
warning:     #F59E0B   (Amber)
cardBg:      rgba(255,255,255,0.6-0.8)
```

**Gradient formulas:**
- Primary button: `from-[#A78BFA] to-[#7C3AED]` (lighter→darker for depth)
- Icon orbs: varied `from-blue-400 to-blue-600` / `from-purple-400 to-purple-600` / `from-pink-400 to-pink-600`
- Hero text: `from-[#332F3A] 20% to-[#7C3AED] 60% to-[#DB2777]` — `text-5xl+` only

### Typography
- **Heading:** `"Nunito", sans-serif` — rounded terminals, 700/800/900. Apply via inline `style={{ fontFamily: "Nunito, sans-serif" }}`
- **Body:** `"DM Sans", sans-serif` — geometric clean, 400/500/700

| Role | Size | Notes |
|:-----|:-----|:------|
| Hero | `text-5xl sm:text-6xl md:text-7xl lg:text-8xl` | `font-black leading-[1.1] tracking-tight Nunito` |
| Section H2 | `text-3xl sm:text-4xl md:text-5xl` | `font-extrabold Nunito` |
| Card title | `text-xl–text-3xl` | `font-bold Nunito` |
| Body | `text-base–text-lg` | `leading-relaxed DM Sans` |
| Labels | `text-sm` | `font-bold uppercase tracking-wide` |

### Radius (Super-Rounded — Minimum 20px)
```
Large containers: 48px–60px
Standard cards:   32px  (default)
Medium elements:  24px
Buttons/Inputs:   20px or rounded-2xl
Icon square:      rounded-2xl (16px)
Icon circle:      rounded-full
Stat orbs:        rounded-full
Badge:            rounded-full
```
**NEVER:** `rounded-md (4px)` or `rounded-sm`. These break the clay aesthetic.

### Shadow System (4-Layer Clay Physics — CRITICAL)
```css
/* Clay Card — floating */
box-shadow:
  16px 16px 32px rgba(160,150,180,0.2),
  -10px -10px 24px rgba(255,255,255,0.9),
  inset 6px 6px 12px rgba(139,92,246,0.03),
  inset -6px -6px 12px rgba(255,255,255,1);

/* Clay Button — high convexity */
box-shadow:
  12px 12px 24px rgba(139,92,246,0.3),
  -8px -8px 16px rgba(255,255,255,0.4),
  inset 4px 4px 8px rgba(255,255,255,0.4),
  inset -4px -4px 8px rgba(0,0,0,0.1);

/* Clay Pressed — recessed (inputs, active) */
box-shadow:
  inset 10px 10px 20px #d9d4e3,
  inset -10px -10px 20px #ffffff;

/* Clay Deep — large surfaces */
box-shadow:
  30px 30px 60px #cdc6d9,
  -30px -30px 60px #ffffff,
  inset 10px 10px 20px rgba(139,92,246,0.05),
  inset -10px -10px 20px rgba(255,255,255,0.8);
```

### Animated Background Blobs (Mandatory — 3-4 blobs)
```jsx
<div className="pointer-events-none fixed inset-0 overflow-hidden -z-10" aria-hidden="true">
  <div className="absolute -top-[10%] -left-[10%] h-[60vh] w-[60vh]
    rounded-full bg-[#8B5CF6]/10 blur-3xl
    animate-[clay-float_8s_ease-in-out_infinite]" />
  <div className="absolute -right-[10%] top-[20%] h-[60vh] w-[60vh]
    rounded-full bg-[#EC4899]/10 blur-3xl
    animate-[clay-float-delayed_10s_ease-in-out_infinite]
    [animation-delay:2000ms]" />
  <div className="absolute bottom-[10%] left-[30%] h-[50vh] w-[50vh]
    rounded-full bg-[#0EA5E9]/10 blur-3xl
    animate-[clay-float_12s_ease-in-out_infinite]
    [animation-delay:4000ms]" />
</div>
```

### Buttons

**Primary (gradient + squish):**
```
bg-gradient-to-br from-[#A78BFA] to-[#7C3AED]
text-white font-bold rounded-[20px] h-14 px-8
shadow-[12px_12px_24px_rgba(139,92,246,0.3),-8px_-8px_16px_rgba(255,255,255,0.4),...]
hover:-translate-y-1 + shadow enhance
active:scale-[0.92] active:shadow-clayPressed  ← MANDATORY squish
transition-all duration-200
focus-visible:ring-4 ring-[#7C3AED]/30 ring-offset-2
```

**Secondary:** `bg-white shadow-clayButton rounded-[20px] h-14`
**Outline:** `border-2 border-[#7C3AED]/20 text-[#7C3AED]`, hover: fill to `/5`
**Ghost:** hover: `bg-[#7C3AED]/10 text-[#7C3AED]`

### Cards (Glass-Clay)
```
relative overflow-hidden rounded-[32px]
bg-white/60 backdrop-blur-xl
p-8 shadow-clayCard
hover:-translate-y-2 duration-500
transition-all
```
Inner content: `<div className="relative z-10 flex h-full flex-col">`
Decorative peeking elements: `absolute -bottom-8 -left-8 -right-8`

**Bento hero card:** `md:col-span-2 md:row-span-2` — larger padding, bigger typography.

### Inputs (Recessed Clay)
```
rounded-2xl h-16 bg-[#EFEBF5] px-6 py-4 border-0
shadow-[inset_10px_10px_20px_#d9d4e3,inset_-10px_-10px_20px_#ffffff]
text-[#332F3A] placeholder:text-[#635F69] text-lg
focus: bg-white ring-4 ring-[#7C3AED]/20 shadow-none
transition-all duration-200
```

### Stat Orbs
```
rounded-full bg-white shadow-clayCard
animate-[clay-breathe_6s_ease-in-out_infinite]
hover:scale-110 transition-all duration-300
```

### Icon Containers
```jsx
{/* Always gradient, always varied colors */}
<div className="rounded-2xl bg-gradient-to-br from-blue-400 to-blue-600 p-4 shadow-clayButton">
  <Icon className="h-6 w-6 text-white" />
</div>
```

### Layout
- Bento grid: mix `col-span-1` + `col-span-2` + `row-span-2` — never uniform grid
- 50/50 splits for product/benefits sections
- Overlapping badges: `absolute -top-4 -right-4` (bleed outside card)
- Negative margins for edge-bleeding decoratives

### Animation Keyframes
```css
@keyframes clay-float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%       { transform: translateY(-20px) rotate(2deg); }
}
@keyframes clay-float-delayed {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%       { transform: translateY(-15px) rotate(-2deg); }
}
@keyframes clay-float-slow {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50%       { transform: translateY(-30px) rotate(5deg); }
}
@keyframes clay-breathe {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.02); }
}
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; }
}
```

### Non-Negotiable Bold Choices
1. **4-layer shadow stacks** — flat/single shadow destroys clay physics
2. **active:scale-[0.92] squish** — the most important interaction
3. **Animated blobs (3-4)** — no flat backgrounds ever
4. **rounded-[20px] minimum** — never `rounded-md/lg`
5. **Glass-clay cards** — `bg-white/60 backdrop-blur-xl`
6. **Nunito inline font** for all headings
7. **Gradient icon containers** — varied colors, never flat
8. **hover:-translate-y** on every interactive element
9. **clay-breathe on stat orbs** — living, breathing UI
10. **Bento grid** not uniform — asymmetric spans

### Responsive
- Hero: `text-5xl sm:text-6xl md:text-7xl lg:text-8xl`
- Stats: `grid-cols-2 md:grid-cols-4`
- Features: single col → bento on desktop
- Primary CTA: `w-full sm:w-auto`
- Blobs: scale with `vh` units naturally
- Keep: full shadow stacks, generous radii, candy colors on mobile

### Accessibility
- `#332F3A` on `#F4F1FA`: WCAG AA ✓
- `#635F69` is the MINIMUM muted text — never lighter
- Focus: `ring-4 ring-[#7C3AED]/30 ring-offset-2`
- Decorative blobs: `aria-hidden="true"`
- `prefers-reduced-motion`: disable all clay-float animations

</design-system>
