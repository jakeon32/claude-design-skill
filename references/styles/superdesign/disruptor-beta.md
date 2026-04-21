# Disruptor Beta Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#121212", volt: "#CCFF00", fg: "#FFFFFF", black: "#000000", muted: "#475569" }
typography: { heading: "Ranchers", label: "Space Mono", body: "Plus Jakarta Sans", weight: "Ranchers: all-caps leading-0.85 up to 180px / Space Mono: uppercase 0.1em bold / Plus Jakarta Sans: 400–700", size_hero: "150px–180px", tracking: "0.1em (mono) / tight (Ranchers)" }
style_traits: [Neo-Brutalist Industrial, 볼트 그린 고에너지, 4px/8px hard borders, solid neo-shadows no-blur, sticker-bar, vertical sidebar strips, blueprint aesthetic]
radius: "8px max — 날카로운 모서리 유지"
effects:
  neo_shadow: "solid 8px 8px offset (no blur) in #000000 or #FFFFFF"
  sticker: "rotated -2 to +5deg, 4px border, white bg, mono all-caps text"
  vertical_sidebar: "64px strips, 4px black separators, writing-mode: vertical-rl, Space Mono text"
  comparison_row: "left half #000000 muted text (Old Way) / right half #CCFF00 black text (Better Way)"
  watermark: "giant Ranchers step number 3% opacity behind card"
  brutalist_form: "4px black border + 8px solid shadow container, no-border input, hover: translate(4px,4px) fills shadow"
animation:
  button_hover: "translate(4px 4px) → fills neo-shadow gap 150ms"
  form_submit: "black↔white bg flip"
layout: [sticky white nav (4px bottom border, rotated logo mark, mono badge, 'Join Beta' 8px-radius), massive Ranchers hero (sticker badge + 150–180px headline + 6–8px drop shadow + italic subheadline + brutalist form), full-width sticker testimonial bar (4px borders), comparison grid (Black/Volt rows Ranchers 80px), 3col blueprint process cards (white bg 8px border, white neo-shadow, volt step tag, watermark), 200px fixed vertical sidebar (64px strips)]
components:
  nav: "sticky white 4px-border-bottom, rotated logo-square, mono badge neo-shadow, 'Join Beta' 8px-radius"
  hero: "Ranchers 180px 6–8px drop shadow, sticker badge -2deg, italic PJS subheadline, brutalist form"
  sticker_bar: "full-width white 4px borders, rotated testimonial sticker cards, mono all-caps"
  comparison: "horizontal rows split 50/50 black/volt, Ranchers 80px, Space Mono labels"
  process_cards: "3col white 8px border white neo-shadow, volt 'STEP 01' tag rotated, Ranchers watermark 3%"
  sidebar: "fixed 200px right, vertical 64px strips w/ 4px dividers, vertical-rl Space Mono labels"
special_notes:
  - "solid shadow only — blur/spread 금지"
  - "모든 기술 레이블 all-caps 필수"
  - "최소 4px border — 얇은 선 금지"
  - "black/white/volt 고대비 유지"
  - "rounded corners 8px 초과 금지"
  - "그라디언트·투명 효과 금지 (bg watermark 3% 제외)"
```
