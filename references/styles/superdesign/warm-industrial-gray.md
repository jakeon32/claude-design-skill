# Warm Industrial Gray Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#EBEBE8", fg: "#18181B", accent_blue: "#0066FF", border: "#D4D4D8", footer_bg: "#18181B", footer_fg: "#EBEBE8" }
typography: { heading: "Playfair Display", body: "Inter", label_mono: "monospace", weight: "Inter: 400/700/900 / Playfair: italic 400", tracking: "0.2em–0.3em (labels 10px bold uppercase)", size_hero: "8xl–10xl (128–160px)", tracking_hero: "-0.05em" }
style_traits: [Warm Industrial 인더스트리얼, 12컬럼 구조적 그리드, 스트로크 텍스트(-webkit-text-stroke), 클립패스 리빌 애니메이션, 노이즈 텍스처 0.04 opacity, 날카로운 직사각 형태]
cursor: "default"
effects:
  noise_overlay: "SVG fractalNoise 0.04 opacity, fixed 전역"
  grid_bg: "fixed 12 vertical lines #18181B at 0.1 opacity, 1600px max-width 내 균등 배치"
  stroke_text: "-webkit-text-stroke: 1px #18181B; color: transparent — 대형 헤드라인용"
  clip_path_reveal: "project 이미지 hover — clip-path: inset(0 0 0 100%)→inset(0 0 0 0), 0.6s cubic-bezier(0.16,1,0.3,1)"
  status_pulse: "6px circle bg-green-500, box-shadow 펄스 애니메이션"
  marquee_ticker: "7xl 교차 bold sans stroke + italic serif, 120px height, electric blue #0066FF star separators"
animation:
  timing: "cubic-bezier(0.16, 1, 0.3, 1)"
  project_hover: "clip-path reveal + grayscale image + #0066FF/20 mix-blend-multiply overlay"
  hero_arrow: "hover rotate on CTA button"
layout: [80px sticky header (backdrop-blur 10px), split hero (7:5) — stroke 헤드라인 + 사각 'Start' 버튼 / 글래스모피즘 UI 카드, 120px marquee ticker ribbon, 300px height project list rows (clip-path 리빌 hover), 철학적 parallax 섹션, technical journal, #18181B 대형 footer (20vw 배경 마퀴)]
components:
  nav: "80px height, logo: serif italic 'SUPER' + bold sans 'DESIGN' absolute centered, tiny caps 링크, rounded-full CTA"
  hero_left: "7cols — 'Available' status dot, 3-line stroke+serif 헤드라인, 10px mono 레이블, 사각 'Start' 버튼"
  hero_right: "5cols — grayscale 이미지 + 20px internal frame + glassmorphism system status 카드"
  project_row: "300px, 1px border-bottom, hover: italic 텍스트 + clip-path 이미지 리빌 오른쪽, 'View' 원형 badge"
  footer: "#18181B, 4xl 콘택트 링크, 20vw 배경 마퀴 0.1 opacity, 녹색 pulse 'System Operational'"
special_notes:
  - "배경 #EBEBE8 유지 필수 — Warm Industrial 느낌"
  - "12컬럼 배경 그리드 라인 전 섹션에 고정 노출"
  - "CTA 버튼과 status badge 제외 rounded corners 금지"
  - "노이즈 텍스처 미묘하게 유지 — 더럽게 보이지 않게"
```
