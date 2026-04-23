# Cyberpunk / Glitch Design System
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#0a0a0f", fg: "#e0e0e0", card: "#12121a", muted: "#1c1c2e", muted_fg: "#6b7280", accent: "#00ff88", accent_secondary: "#ff00ff", accent_tertiary: "#00d4ff", border: "#2a2a3a", ring: "#00ff88", destructive: "#ff3366" }
typography: { heading: "Orbitron / Share Tech Mono (monospace geometric futuristic)", body: "JetBrains Mono / Fira Code (terminal monospace)", labels: "Share Tech Mono (UI labels/timestamps/badges)", weight: "font-black uppercase (H1) / font-bold uppercase (H2) / font-semibold uppercase (H3) / normal body", size_hero: "text-6xl–text-8xl", tracking: "tracking-widest (H1) / tracking-wide (H2+body) / tracking-[0.2em] (labels)", leading: "leading-relaxed (body)" }
style_traits: [High-Tech Low-Life 사이버펑크 디스토피아, 80s SF 블레이드러너+아키라 미학, CRT 모니터 글리치/스캔라인, 네온 발광 텍스트+보더, 챔퍼드 코너 클립패스, PCB 회로 패턴 배경]
radius: "0px default — clip-path chamfer 대신 border-radius 사용 금지. inputs만 4px 허용"
chamfer: "clip-path: polygon(0 10px, 10px 0, calc(100%-10px) 0, 100% 10px, 100% calc(100%-10px), calc(100%-10px) 100%, 10px 100%, 0 calc(100%-10px)) — 모든 카드/버튼에 필수"
shadow:
  neon_sm: "0 0 3px #00ff88, 0 0 6px #00ff8830"
  neon: "0 0 5px #00ff88, 0 0 10px #00ff8840"
  neon_lg: "0 0 10px #00ff88, 0 0 20px #00ff8860, 0 0 40px #00ff8830"
  neon_secondary: "0 0 5px #ff00ff, 0 0 20px #ff00ff60"
  neon_tertiary: "0 0 5px #00d4ff, 0 0 20px #00d4ff60"
effects:
  scanlines: "repeating-linear-gradient(0deg, transparent 2px, rgba(0,0,0,0.3) 2px, rgba(0,0,0,0.3) 4px) — pointer-events-none 전체 페이지 오버레이 필수"
  circuit_grid: "linear-gradient(rgba(0,255,136,0.03) 1px, transparent 1px) + 90deg same — 50px 50px bg-size"
  chromatic_aberration: "::before text-shadow: -1px 0 #ff00ff / ::after text-shadow: -1px 0 #00d4ff — hero headline 필수"
  noise: "SVG noise or CSS noise filter 5-10% opacity"
  gradient_mesh: "radial-gradient accent colors 코너, very low opacity"
animation:
  timing: "150ms cubic-bezier(0.4,0,0.2,1) standard — 100ms steps(4) for digital feel"
  blink: "@keyframes blink { 50% { opacity:0; } } — 1s step-end infinite"
  glitch: "@keyframes glitch { 0%,100%{transform:translate(0)} 20%{translate(-2px,2px)} 40%{translate(2px,-2px)} 60%{translate(-1px,-1px)} 80%{translate(1px,1px)} }"
  rgb_shift: "@keyframes rgbShift { 0%,100%{text-shadow:-2px 0 #ff00ff,2px 0 #00d4ff} 50%{text-shadow:2px 0 #ff00ff,-2px 0 #00d4ff} }"
  scanline_scroll: "@keyframes scanline { 0%{transform:translateY(-100%)} 100%{transform:translateY(100vh)} }"
layout: [max-w-7xl, py-24–py-32 sections, 60/40 hero split, grid -skew-y-1 containers, rotate-1 asymmetric, 중간 카드 scale-up pricing]
components:
  button_default: "transparent bg, border-2 border-[#00ff88] text-[#00ff88], chamfer clip-path, uppercase tracking-wider monospace, hover: bg-[#00ff88] text-[#0a0a0f] + neon glow"
  button_secondary: "border-2 border-[#ff00ff] text-[#ff00ff], hover: bg-[#ff00ff] text-bg + neon-secondary"
  button_outline: "border border-[#2a2a3a], hover: border-[#00ff88] text-[#00ff88] + glow"
  button_glitch: "bg-[#00ff88] text-bg solid, .cyber-glitch chromatic aberration class, hover:brightness-110"
  cards_default: "bg-[#12121a] border-[#2a2a3a] chamfer clip-path, hover: translateY(-1px) border→accent + neon glow"
  cards_terminal: "bg-[#0a0a0f] border-[#2a2a3a] + auto header bar (traffic light dots red/yellow/green) + chamfer"
  cards_holographic: "bg-[#1c1c2e]/30 border-[#00ff88]/30 + neon glow + backdrop-blur + 4 corner accent brackets absolute"
  inputs: "> prefix accent color absolute-left, bg-[#12121a] border-[#2a2a3a] chamfer, text-[#00ff88] monospace, focus: border-[#00ff88] + neon glow outline-none"
  icons: "lucide stroke-[1.5px], h-5–h-6, hover:drop-shadow(0 0 4px currentColor)"
special_notes:
  - "hero H1 chromatic aberration text-shadow 필수 + glitch CSS animation 필수"
  - "scanline overlay 전체 페이지 필수 — body::after or main::after"
  - "chamfer clip-path 모든 카드+버튼 필수 — rounded corners 절대 금지"
  - "neon glow = 단순 colored border 아님 — stacked box-shadow 3개 이상"
  - "circuit/grid background 최소 1개 섹션 필수"
  - "터미널 aesthetic 최소 1섹션 (monospace + '>' prefix + 블링킹 커서)"
  - "glitch 애니메이션 subtle + 비빈번하게 — 주의 산만 금지"
  - "will-change:transform GPU 성능 주의 — 다중 box-shadow 최소화"
  - "prefers-reduced-motion — glitch 애니메이션 비활성화, static chromatic 유지"
  - "모든 텍스트 monospace 전용 — sans-serif 절대 금지"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
**"High-Tech, Low-Life."** Digital dystopia colliding with high-tech noir reality. Underground hackers, neon-drenched megacities, corrupted data streams. Every pixel rendered on a malfunctioning CRT monitor in a rain-soaked Tokyo alley.

**Vibe:** Dangerous, electric, rebellious, aggressively futuristic-retro. 80s sci-fi (Blade Runner, Akira) + hacker culture (The Matrix, Ghost in the Shell). The interface feels *alive* and volatile — buzzing with digital energy, glitching with data corruption.

**Visual Signatures:**
- **Chromatic Aberration:** RGB color splitting (red/cyan offset shadows) on hero text
- **Scanlines:** Horizontal line overlays mimicking CRT refresh rate
- **Glitch Effects:** clip-path animations, skewed transforms, flickering text
- **Neon Glow:** Multi-layered box-shadow/text-shadow stacks — physical glow, not just color
- **Corner Cuts:** Chamfered clip-path (not border-radius) on all cards and buttons
- **Circuit Patterns:** SVG/CSS PCB trace backgrounds

### Colors (Mandatory Dark Mode)
```
background:       #0a0a0f    (Deep void — slight blue undertone)
foreground:       #e0e0e0    (Primary text — not harsh pure white)
card:             #12121a    (Card bg — deep purple-black)
muted:            #1c1c2e    (UI chrome / elevated bg)
mutedForeground:  #6b7280    (Secondary text)
accent:           #00ff88    (PRIMARY — Electric green / Matrix)
accentSecondary:  #ff00ff    (SECONDARY — Hot magenta/pink)
accentTertiary:   #00d4ff    (TERTIARY — Cyan/electric blue)
border:           #2a2a3a    (Subtle borders)
ring:             #00ff88    (Focus ring = accent)
destructive:      #ff3366    (Error/danger)
```
Accent on dark bg: 7.5:1 WCAG AA ✓

### Typography
- **Headings:** `"Orbitron", "Share Tech Mono", monospace` — geometric, futuristic, robotic
- **Body:** `"JetBrains Mono", "Fira Code", monospace` — terminal aesthetic
- **Labels/Badges:** `"Share Tech Mono", monospace` — UI chrome, timestamps

| Role | Size | Notes |
|:-----|:-----|:------|
| H1 | `text-5xl md:text-7xl lg:text-8xl` | `font-black uppercase tracking-widest` |
| H2 | `text-4xl md:text-5xl` | `font-bold uppercase tracking-wide` |
| H3 | `text-xl md:text-2xl` | `font-semibold uppercase` |
| Body | `text-base` | `tracking-wide leading-relaxed` |
| Labels | `text-sm` | `font-mono uppercase tracking-[0.2em]` |

**All text: monospace only. Sans-serif forbidden.**

### Radius & Chamfered Corners
```
Default: 0px — border-radius forbidden on cards/buttons
Inputs: 4px max only
```

**Chamfer pattern (MANDATORY on all cards + buttons):**
```css
clip-path: polygon(
  0 10px, 10px 0,
  calc(100% - 10px) 0, 100% 10px,
  100% calc(100% - 10px), calc(100% - 10px) 100%,
  10px 100%, 0 calc(100% - 10px)
);
/* Small variant: 6px cuts for buttons */
```

### Neon Glow System
```css
/* Not just colored borders — real stacked glow */
--neon-sm:        0 0 3px #00ff88, 0 0 6px #00ff8830;
--neon:           0 0 5px #00ff88, 0 0 10px #00ff8840;
--neon-lg:        0 0 10px #00ff88, 0 0 20px #00ff8860, 0 0 40px #00ff8830;
--neon-secondary: 0 0 5px #ff00ff, 0 0 20px #ff00ff60;
--neon-tertiary:  0 0 5px #00d4ff, 0 0 20px #00d4ff60;
```

### Textures & Patterns (All Required)

**Scanlines overlay (entire page — mandatory):**
```css
.scanlines::after {
  content: "";
  position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  background: repeating-linear-gradient(
    0deg,
    transparent, transparent 2px,
    rgba(0,0,0,0.3) 2px, rgba(0,0,0,0.3) 4px
  );
}
```

**Circuit grid background (min 1 section):**
```css
background-image:
  linear-gradient(rgba(0,255,136,0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(0,255,136,0.03) 1px, transparent 1px);
background-size: 50px 50px;
```

**Chromatic aberration (hero headline — mandatory):**
```css
.cyber-glitch::before {
  content: attr(data-text);
  position: absolute; inset: 0;
  text-shadow: -1px 0 #ff00ff;
  clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
  animation: glitch 3s infinite;
}
.cyber-glitch::after {
  text-shadow: -1px 0 #00d4ff;
  clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
  animation: glitch 3s infinite reverse;
}
```

**Gradient mesh (corners, low opacity):**
```css
background: radial-gradient(circle at top-right, rgba(0,255,136,0.05) 0%, transparent 60%),
            radial-gradient(circle at bottom-left, rgba(255,0,255,0.05) 0%, transparent 60%);
```

### Buttons

**Default (green neon):**
```
bg-transparent border-2 border-[#00ff88] text-[#00ff88]
font-mono uppercase tracking-wider chamfer-sm clip-path
hover: bg-[#00ff88] text-[#0a0a0f] + box-shadow var(--neon)
active: brightness-90
transition: all 150ms cubic-bezier(0.4,0,0.2,1)
```

**Secondary (magenta):**
```
border-2 border-[#ff00ff] text-[#ff00ff]
hover: bg-[#ff00ff] text-[#0a0a0f] + neon-secondary
```

**Outline:**
```
border border-[#2a2a3a] text-[#e0e0e0]
hover: border-[#00ff88] text-[#00ff88] + neon-sm
```

**Glitch (solid CTA):**
```
bg-[#00ff88] text-[#0a0a0f] .cyber-glitch class
hover: filter brightness-110
```

All: `focus-visible:ring-2 focus-visible:ring-[#00ff88] focus-visible:ring-offset-2 focus-visible:ring-offset-[#0a0a0f]`

### Cards

**Default:**
```
bg-[#12121a] border border-[#2a2a3a] chamfer clip-path p-6
hover: translateY(-1px) border-[#00ff88] box-shadow var(--neon-sm)
transition: all 300ms
```

**Terminal variant:**
```
bg-[#0a0a0f] border-[#2a2a3a] chamfer
+ header bar: bg-[#1c1c2e] px-4 py-2
  - dots: h-3 w-3 rounded-full bg-[#ff3366] / bg-[#ffcc00] / bg-[#00ff88]
  - title: monospace text-xs text-[#6b7280]
Content: pt adjusted for header
```

**Holographic variant:**
```
bg-[#1c1c2e]/30 border border-[#00ff88]/30 backdrop-blur-sm
box-shadow: var(--neon-sm)
+ 4 corner accent brackets (absolute, 12px × 12px, 1px solid accent)
```

### Inputs
```
Prefix: ">" text-[#00ff88] absolute left-3
bg-[#12121a] border border-[#2a2a3a] chamfer-sm
h-12 px-8 (to accommodate ">") font-mono text-[#00ff88]
placeholder: text-[#6b7280] font-mono ("> ENTER_COMMAND_")
focus: border-[#00ff88] box-shadow var(--neon-sm) outline-none
transition: all 200ms
```

### Layout
- Container: `max-w-7xl mx-auto`
- Sections: `py-24 md:py-32`
- Hero: 60/40 asymmetric split minimum
- Feature grid: `grid -skew-y-1` on container, cards self-compensate with `skew-y-1`
- Pricing: middle card `scale-105 md:scale-110`
- Stats: `flex divide-x divide-[#2a2a3a]`
- At least one section: overlapping elements with negative margins or `rotate-1`

### Non-Negotiable Bold Choices
1. **Glitched hero H1** — chromatic aberration + occasional glitch animation mandatory
2. **Scanline overlay** — full page, always-on
3. **Terminal section** — at least one with `>` prefix + blinking cursor
4. **Real neon glow** — 3-layer stacked box-shadow, not just colored borders
5. **Chamfered corners** — clip-path on ALL cards + buttons
6. **Circuit grid background** — min 1 section
7. **Blinking cursors** — `@keyframes blink { 50% { opacity:0; } }` 1s step-end
8. **RGB shift animation** — on hero or key headline

### Animation
```css
@keyframes blink { 50% { opacity: 0; } }
@keyframes glitch {
  0%, 100% { transform: translate(0); }
  20% { transform: translate(-2px, 2px); }
  40% { transform: translate(2px, -2px); }
  60% { transform: translate(-1px, -1px); }
  80% { transform: translate(1px, 1px); }
}
@keyframes rgbShift {
  0%, 100% { text-shadow: -2px 0 #ff00ff, 2px 0 #00d4ff; }
  50% { text-shadow: 2px 0 #ff00ff, -2px 0 #00d4ff; }
}
@keyframes scanline {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(100vh); }
}
```
Glitch: subtle + infrequent (3s interval). Not constant distraction.

### Responsive
- Hero H1: `text-5xl md:text-7xl lg:text-8xl`
- Hero HUD panel: `hidden lg:block`
- All grids: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- Stats: 2×2 mobile → 4-column desktop
- Maintain: scanlines, chamfer, neon glow, monospace, dark scheme at all sizes
- Touch targets: `h-11` minimum (44px)
- Reduce glow intensity on mobile for performance

### Accessibility
- `#00ff88` on `#0a0a0f`: 7.5:1 AA ✓
- Focus: `ring-2 ring-[#00ff88] ring-offset-2 ring-offset-[#0a0a0f]` + neon glow
- `prefers-reduced-motion`: disable glitch/rgb-shift animations, keep static chromatic aberration
- Decorative scanlines: `aria-hidden="true" pointer-events-none`
- Blinking cursor decorations: `aria-hidden="true"`

</design-system>
