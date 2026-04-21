# Dark Avant-Garde Style
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#0C0A09", surface: "#1C1917", fg: "#E7E5E4", lime: "#D4F268", border: "rgba(255,255,255,0.1)" }
typography: { heading: "Newsreader", body: "Instrument Sans", mono: "system monospace", weight: "Newsreader: 200–400 italic 자유 / Instrument Sans: 400–600", size_hero: "light weight large serif", tracking: "-0.02em (heading) / normal (body)" }
style_traits: [Digital Naturalism + Brutalist Technicality, 딥 차콜 베이스, 라임 #D4F268 surgical accent, 노이즈 overlay 4% opacity, serrated 섹션 구분선, 폴더형 탭 UI]
radius: "24px (large cards) / rounded-full (buttons) / 10rem radius top-arch (hero image)"
effects:
  noise_overlay: "fixed SVG fractalNoise 0.04 opacity, mix-blend-mode: overlay"
  serrated_edge: "radial-gradient mask — circle at 10px 0, transparent 0-5px, black 5px; mask-size: 20px 10px; 섹션 경계 분리"
  sticky_note: "#D4F268 카드, rotate(2deg), hover: rotate(0deg) scale(1.02)"
  catalog_label: "이미지 absolute badge — #000/40 backdrop-blur, 10px mono 'Fig. No' + #D4F268 dot"
  grayscale_hover: "카드 이미지 grayscale(100%)→full color on hover"
animation:
  timing: "300ms cubic-bezier(0.4, 0, 0.2, 1)"
  tab_active: "#D4F268 활성 탭, 약간 회전 (-2~-1deg), serrated top edge"
  card_hover: "showcase 카드 3:4 비율, grayscale→color + vertical offset 카드 1개 Y translation"
layout: [fixed pill nav (center링크 backdrop-blur 8px, #D4F268 CTA), 2col hero (5:7 — serif 라이트 헤드라인 italic 강조 / top-arch 이미지 + #D4F268 스티키노트 6deg), folder 탭 UI (serrated top edge, 40px grid 3% opacity, #1C1917), 3:4 showcase 그리드]
components:
  nav: "fixed top, 로고+원형 아이콘, pill nav #E7E5E4/5 + backdrop-blur, #D4F268 CTA rounded-full"
  hero: "5col: Newsreader 300 light serif, italic 강조어, 70% grayscale 아바타 / 7col: top-arch 컨테이너(10rem radius) + #D4F268 sticky note 6deg rotate"
  folder_tab: "-2~-1deg 약간 회전, overlap, 활성 탭 크고 #D4F268, content area #1C1917 serrated top"
  showcase: "3:4 비율, #292524 bg, grayscale→color hover, serif italic 제목, 1카드 Y-offset"
  sticky_note: "#D4F268 bg, #1C1917 text, rotate(2deg), 24px radius, serif heading + bottom border"
special_notes:
  - "Newsreader 200–400 light weights 필수 — italic 빈번 사용"
  - "순수 검정(#000000) 사용 금지 — stone-tinted #0C0A09"
  - "노이즈 overlay 필수 — 어두운 색 flat 방지"
  - "#D4F268 surgical 사용 — 큰 배경 블록 사용 금지"
```
