# Terminal CLI Style
source: designprompts.dev
category: dark

```yaml
palette: { bg: "#0a0a0a", green: "#33ff00", amber: "#ffb000", muted_green: "#1f521f", red: "#ff3333", border: "#1f521f" }
typography: { heading: "JetBrains Mono / Fira Code / VT323", body: "JetBrains Mono", weight: "ALL CAPS headers / lowercase body acceptable", size_hero: "snap-to-grid modular scale", tracking: "monospace default" }
style_traits: [Terminal CLI Hacker, cyber-industrial phosphor monitor, monospace supremacy, blinking cursor heartbeat, shell metaphors, CRT scanlines subtle, ASCII art]
radius: "0px — 절대 rounded corners 금지"
shadow: "없음 — text-shadow: 0 0 5px rgba(51,255,0,0.5) (phosphor glow만)"
effects:
  scanlines: "pointer-events-none CRT overlay, very faint horizontal scanlines"
  phosphor_glow: "text-shadow: 0 0 5px rgba(51,255,0,0.5) on primary text"
  cursor_blink: "blinking block █ or underscore _ animate-blink"
  inverted_btn: "hover: bg fills primary green, text→black (inverted video)"
  glitch: "occasional subtle text offset on hover"
  typing: "hero text character-by-character typewriter animation"
animation:
  blink: "cursor animate-blink standard"
  typing: "typing-demo hero text"
  glitch: "subtle text offset on hover"
layout: [tmux/vim split grid of terminal windows, strict character-grid alignment, ASCII separators (--- / === / //), ASCII art logo/graphics]
components:
  buttons: "text in brackets [ INITIATE ] or solid inverted block / hover: bg fill + text invert / active: 1px shift or rapid blink"
  cards: "black box 1px green border, title bar '+--- SYSTEM STATUS ---+' or solid inverted bar, padded mono content"
  inputs: "no box, prompt 'user@acme:~$' + field, blinking █ cursor, no focus ring"
  nav: "monospaced links, shell metaphors ($, >, ~), status codes [OK] [ERR]"
  progress: "[||||||||||.....] ASCII bar instead of charts"
  ascii_art: "logo or key graphic in ASCII art"
  data_viz: "raw ASCII progress bars, no pie charts"
special_notes:
  - "모든 텍스트 monospace 필수 — sans-serif/serif 금지"
  - "rounded corners 0px 절대 원칙"
  - "drop shadow 금지 — phosphor glow text-shadow만"
  - "green/amber 팔레트만 — 다른 색상 금지"
  - "shell metaphors ($, >, ~, --flag, [OK]) 반드시 포함"
  - "ASCII 구분선 사용: --- / === / //"
```

---

## Full Design System Prompt

<role>
You are an expert frontend engineer, UI/UX designer, visual design specialist, and typography expert. Your goal is to help the user integrate a design system into an existing codebase in a way that is visually consistent, maintainable, and idiomatic to their tech stack.

Before proposing or writing any code, first build a clear mental model of the current system: Identify the tech stack, understand existing design tokens, review component architecture, and note constraints. Always preserve accessibility, maintain visual consistency, ensure responsive layouts, and make deliberate creative design choices that express the design system's personality instead of producing generic UI.
</role>

<design-system>

### Design Philosophy
The **Terminal CLI** aesthetic pays homage to the raw power of the command line. It strips away UI layers to reveal the system underneath. **Brutally functional, high-contrast, authentically retro** — like configuring a server or hacking into a mainframe.

**Vibe:** Cyber-Industrial, Hacker, System-Level. NOT Matrix rain (too cliché) — a clean, usable ZSH/BASH shell environment.

**Key Signatures:**
- **Monospace Supremacy:** Every single character — from headline to footer link — is monospaced
- **The Cursor:** Blinking block `█` or underscore `_` is the heartbeat
- **Shell Metaphors:** Prompt characters (`>`, `$`, `~`), command flags (`--help`), status codes (`[OK]`, `[ERR]`)
- **Scanlines:** Faint CRT overlay adds depth without ruining readability

### Colors (Dark Mode Only)
Phosphor monitor palette. High contrast is non-negotiable.
```
background: #0a0a0a  (Deep black — not pure OLED to allow scanline visibility)
primary:    #33ff00  (Bright Neon Green — main text/interactive)
secondary:  #ffb000  (Amber — warnings, secondary accents)
muted:      #1f521f  (Dimmed green — borders, inactive text)
error:      #ff3333  (Bright Red)
border:     #1f521f  (Dimmed green)
```
Green is primary. Amber for warnings/contrast. No other colors.

### Typography
- **Font:** `"JetBrains Mono"`, `"Fira Code"`, or `"VT323"` — monospace only
- **Headers:** ALL CAPS. Snap to grid sizes, not smooth scale.
- **Body:** Lowercase acceptable, but consistent
- **Rule:** Every single text element — headings, body, labels, nav, footer — must be monospaced. No exceptions.

### Radius & Borders
- **Radius: 0px. Absolutely no rounded corners.**
- Borders: `1px` solid or dashed `#1f521f`
- Borders define "windows" and "panes" — essential structural element

### Shadows
- No drop shadows
- **Phosphor glow only:** `text-shadow: 0 0 5px rgba(51, 255, 0, 0.5)` on primary green text

### Effects (Required)
```css
/* CRT Scanlines overlay */
.scanlines::after {
  content: '';
  position: fixed; inset: 0; pointer-events: none; z-index: 9999;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px, rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px
  );
}

/* Cursor blink */
@keyframes blink { 0%,49% { opacity: 1; } 50%,100% { opacity: 0; } }
.animate-blink { animation: blink 1s step-end infinite; }

/* Typewriter */
@keyframes typing { from { width: 0; } to { width: 100%; } }
.typing-demo { overflow: hidden; white-space: nowrap; animation: typing 3s steps(40); }
```

### Buttons
- **Structure:** Text in brackets: `[ EXECUTE ]` or `[ --HELP ]`
- **Default:** green text + green border on black bg
- **Hover:** bg fills `#33ff00`, text → black (inverted video)
- **Active:** text shifts 1px down, or brief rapid blink
- Shape: 0px radius, `px-4 py-2`, uppercase monospace

### Cards (Terminal Windows/Panes)
- Black box with 1px `#1f521f` border
- **Title bar:** `+--- WINDOW TITLE ---+` or solid inverted `bg-[#33ff00] text-black`
- Content: padded monospaced text inside
- Use `|` and `+` ASCII corners for decorative borders

### Inputs
- No box styling — just prompt followed by field:
  `user@system:~$` `[input text here]█`
- Blinking `█` cursor at caret
- Focus: no ring — cursor presence indicates focus
- No border-radius, no outer border

### Layout
- Grid of terminal windows (tmux/vim splits)
- Strict character-grid alignment
- ASCII dividers: `────────────────`, `================`, `// SECTION //`
- Content aligned in columns like terminal output

### Non-Negotiable Bold Choices
1. **ASCII Art:** Logo or hero graphic rendered in ASCII
2. **Typewriter Effect:** Hero headline appears character-by-character
3. **ASCII Progress Bars:** Stats → `[██████████░░░░░]  68%` not charts
4. **Shell Prompts:** Inputs prefixed with `$` or `user@host:~$`
5. **Status Codes:** Navigation and states use `[OK]`, `[ERR]`, `[--]`, `[??]`
6. **Window Title Bars:** Cards use `+--- TITLE ---+` ASCII framing
7. **Phosphor Glow:** `text-shadow: 0 0 5px rgba(51,255,0,0.5)` on primary text
8. **Glitch Hover:** Subtle `translateX(1–2px)` text offset on hover

### Animation
```css
/* All animations: snappy, instant, or blink-based */
blink:   1s step-end infinite (cursor)
typing:  3s steps(40) (hero text reveal)
glitch:  hover: translateX(1px) or skewX(1deg) momentarily
inverted:instant bg-fill on hover (no transition — snap to state)
```
No smooth easing — terminal interactions are instantaneous.

### Responsive
- Mobile: terminal windows stack vertically
- Long lines wrap with `\` continuation indicator
- Reduce font size slightly but maintain monospace
- Preserve all shell metaphors and ASCII elements on mobile

### Accessibility
- `#33ff00` on `#0a0a0a`: >7:1 AAA ✓
- `#ffb000` on `#0a0a0a`: >7:1 AAA ✓
- Focus: inherent — inverted colors on focus/hover are highly visible
- Scanlines: kept subtle (opacity 0.05) to not impair readability

</design-system>
