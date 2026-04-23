# Deep Red Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", accent: "#FF4500", card: "#111111", fg: "#FFFFFF", fg_muted: "#ffe0e0", fg_dim: "rgba(255,255,255,0.4)" }
typography: { heading: "Playfair Display", body: "Inter", weight: "Playfair Display: italic medium / Inter: 300–600", size_hero: "text-5xl–text-7xl", tracking: "tight (serif) / widest uppercase (utility mono)" }
style_traits: [Surrealist Dark Editorial, floating hands mix-blend-hard-light, noise overlay 5%, coral radial cards 4:5, scroll parallax stagger, mix-blend-overlay hero text]
radius: "rounded-full (CTA pill) / rounded-3xl (cards) / rounded-full (icons)"
effects:
  noise: "fixed noise.svg overlay 5% opacity mix-blend-mode: overlay"
  floating_hands: "mix-blend-hard-light 80% opacity, animate-float-left 12s / animate-float-right 14s ease-in-out infinite"
  hero_text: "mix-blend-overlay, text-shadow: 0 0 12px rgba(255,255,255,0.71)"
  hero_bg: "atmospheric image 60% opacity mix-blend-screen + gradient-to-b transparent→#050505"
  cta_glow: "#FF4500/20 blur-xl rounded-full on hover"
  coral_card: "#FF4500 bg rounded-3xl shadow-2xl, hover: shadow 0 20px 50px rgba(255,69,0,0.3)"
  parallax: "parallax-card-up / parallax-card-down translateY(--scroll-offset)"
  dot_bg: "radial-gradient circle #333 1px transparent, 40px bg-size, 10% opacity"
animation:
  timing: "cubic-bezier(0.22, 1, 0.36, 1) 0.8s"
  reveal: "translateY(30px)→0 + opacity 0→1, stagger 200ms"
  hand_float_l: "translateY(-20px) rotate(2deg) 12s ease-in-out infinite"
  hand_float_r: "translateY(20px) rotate(-2deg) 14s ease-in-out infinite"
layout: [fixed serif nav (logo 'Superdesign.' + gray-400 sm links + white rounded-full CTA), 100vh surrealist hero (atmospheric bg + floating hands hard-light + centered PD italic heading + glass pill CTA + mono time/location), mission section (5xl–6xl serif centered + grayscale logo grid), 2col staggered 4:5 coral/dark cards (parallax), dark footer (10vw ghost brand text 10% opacity)]
components:
  nav: "fixed transparent, 'Superdesign.' 2xl bold tracking-tighter serif, gray-400 sm links, white rounded-full pill CTA"
  hero: "atmospheric img 60% mix-blend-screen + gradient overlay, floating hands hard-light, PD italic 5xl–7xl mix-blend-overlay text-shadow, glass pill 'Enter the Void' + mono time"
  logo_grid: "4col 40% grayscale hover:grayscale-0 transition-500, uppercase tracking-widest font-bold"
  cards: "2col — coral #FF4500 rounded-3xl p-8–p-12 4:5 (black serif title) + dark #111 border-white/10 (hover border-FF4500/50), parallel scroll offset"
  footer: "#050505 border-t white/5, 10vw tracking-tighter text-white/10 ghost brand, right: social links gray-400 hover:white"
special_notes:
  - "mix-blend-overlay 히어로 텍스트 + text-shadow 필수"
  - "floating hands mix-blend-hard-light 80% — z-index 10 hero bg z-0"
  - "noise overlay 5% mix-blend-overlay fixed 전체 필수"
  - "#FF4500 strictly — 다른 accent 색상 금지"
```
