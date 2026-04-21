# Refined Grunge
source: superdesign.dev
category: grunge

```yaml
palette: { bg: "#F0EAD6", primary: "#1A1A1A", accent: "#DC143C", gold: "#C5A945", surface: "#1A1A1A" }
typography: { heading: "Cabinet Grotesk", body: "JetBrains Mono", weight: "900/400", transform: "uppercase", tracking: "-0.05em" }
style_traits: [펑크록 미니멀리즘, 모노스페이스 유틸리티, 그런지 텍스처, 기계적 지터, 종이+잉크 대비]
border: "4px solid #1A1A1A"
shadow: "8px 8px 0px #1A1A1A"
effects:
  noise_overlay: "SVG fractal noise, opacity 10%"
  halftone: "radial-gradient(#1A1A1A 1px, transparent 0), size 6px 6px"
  torn_edge: "clip-path polygon, 20+ anchor points (jagged rip)"
  image_filter: "grayscale(0.6) contrast(1.2), reverts to color on hover"
animation:
  timing: "step-end (비선형, 아날로그 느낌)"
  jitter: "translate(-1px) rotate(-0.5deg), 0.5s step-end"
  flicker: "opacity 0.98~1.0, step-end"
  glitch_text: "text-shadow #DC143C → #C5A945, 2s step-end infinite"
layout: [fixed 48px crimson header + marquee, split-grid hero, 3-col torn-card grid, scattered paper rotation (-2~2deg)]
components:
  cta_button: "#DC143C bg, 4px border, 6px block shadow → hover press simulation"
  card: "torn-edge clip-path, 2px border, 8px block shadow, grayscale image"
  headline: "Cabinet Grotesk 900, distressed glitch, step-end animation"
  header_marquee: "#DC143C 48px bar, monospaced scroll text"
  milestone_cards: "rotated -2~2deg, #F0EAD6 bg, accent border"
```
