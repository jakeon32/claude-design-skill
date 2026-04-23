# Obsidian & Lime
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#000000", surface: "#0c0c0c", surface2: "#0a0a0a", lime: "#ccff00", emerald: "#10b981", fg: "#ebebeb", fg_60: "rgba(235,235,235,0.6)", fg_30: "rgba(235,235,235,0.3)" }
typography: { heading: "Space Grotesk", body: "Space Grotesk", mono: "JetBrains Mono", heading_spec: { weight: "300~700", tracking: "-0.06em" }, mono_spec: { transform: "uppercase", tracking: "tracked-out" } }
style_traits: [Obsidian + Lime 글래스모피즘, 테크-인더스트리얼, 플로팅 쉘 아키텍처, 벤토 그리드, 다크모드 퍼스트]
glass: "background: rgba(255,255,255,0.03), backdrop-filter: blur(16px), border: 1px solid rgba(255,255,255,0.1), border-radius: 1.5rem"
texture:
  grid: "60×60px linear-gradient 그리드 패턴, opacity 15%"
  noise: "SVG noise overlay, opacity 15%"
  glow_sphere: "radial-gradient, blur(120px), lime/emerald 컬러, 대형 장식 요소"
radius:
  shell: "2.5rem (전체 사이트 컨테이너)"
  card: "2.5rem"
  nav_pill: "rounded-full"
  button: "9999px (pill)"
  contrast_section: "4rem (상단 코너만)"
effects:
  accent_rule: "#ccff00 — 주요 액션/하이라이트 전용"
  bento_hover: "border-color → #ccff00/40"
  footer_btn_hover: "white bg slide-up transition"
animation:
  float: "translateY 0→-10px, 6s infinite ease-in-out"
  pulse_dot: "lime 6px dot, 2s infinite"
  transition: "cubic-bezier(0.4,0,0.2,1)"
layout: [max-w-1600px 플로팅 쉘(#0c0c0c, rounded-[2.5rem], ring-1 ring-white/10), fixed 네비, 12-col 스플릿 히어로(7+5), 4-col 벤토 그리드, 라이트 섹션(#e5e5e5 대비), #000000 푸터]
components:
  shell: "max-w-1600px, rounded-[2.5rem], ring-1 ring-white/10, shadow-2xl, bg #0c0c0c"
  nav: "좌: rounded-xl lime 박스 + black 이니셜 로고 / 중: pill 네비(rgba(255,255,255,0.05) + backdrop-blur + rounded-full, links white/70) / 우: mono 시스템 상태(lime pulse dot) + rounded-full white 버튼"
  hero: "좌(7col): AI mono 레이블 + 7.5rem leading-0.85 헤딩(italic gradient span #ccff00→white) / 우(5col): 글래스 목업 쉘 + float 카드들 + #ccff00 AI Cursor 플로팅 레이블"
  bento_card: "rounded-[2.5rem], border-white/10, hover: border-#ccff00/40 / 2×2 대형(데이터 시각화 수직 바) / 1×2 tall(컬러 토큰 스와치) / accent(solid #ccff00 bg + black text + noise)"
  contrast_section: "#e5e5e5 bg, black text, rounded-t-[4rem], 번호 리스트(01/02/03 mono circle) + 그레이스케일 초상+글래스 testimonial 오버레이"
  footer: "#000000 bg, 'SUPER' 10rem watermark opacity 5%, 대형 #ccff00 CTA 버튼(hover white slide-up), 3-col(정책링크/소셜hollow circles/mono 저작권)"
  glass_float_card: "rgba(255,255,255,0.03) bg, backdrop-blur(16px), 1px solid rgba(255,255,255,0.1), border-radius 1.5rem, float-anim 6s"
  neon_pulse_btn: "#ccff00 bg, black text, font-weight 700, rounded-full, px-8 py-4, box-shadow 0 0 30px rgba(204,255,0,0.3), hover scale(1.05)"
  system_status_tag: "JetBrains Mono, uppercase, tracking-[0.2em], 10px / lime 6px dot pulse 2s"
special_notes:
  - "#ccff00 반드시 primary accent — 대체 불가"
  - "Space Grotesk + JetBrains Mono 외 시스템 폰트 금지"
  - "glass 요소 blur 최소 16px 유지"
  - "그리드 패턴 + 노이즈 오버레이 필수 — flat dark 방지"
  - "모든 컨테이너 코너 최소 2rem radius"
```
