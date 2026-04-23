# Hyper-Saturated Fluid
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#0A0A0A", surface: "#171717", primary: "#FFFFFF", accent: "#FDE047", ui: "#262626" }
typography: { heading: "Inter / General Sans", body: "Inter", weight: "700/400", size_hero: "text-6xl~8xl", tracking_hero: "tight", size_label: "10px uppercase tracking-widest" }
style_traits: [프리미엄 핀테크, 사이버 옐로우 지배색(60% 뷰포트), 유기적 리퀴드 섹셔닝, 글래스모피즘 데이터 카드, Dark Void 대비]
radius: { section: "rounded-[100px] 또는 clip-path 웨이브", glass: "rounded-[32px]", button: "rounded-full (pill)" }
glass: "bg-white/10, backdrop-blur-2xl, border 1px rgba(255,255,255,0.2), shadow-2xl"
effects:
  hero_cut: "rounded-b-[120px] (우하단) + rounded-bl-[40px] (좌하단) → 비대칭 웨이브"
  shout_color: "#FDE047 flat (그라데이션 금지), 히어로 60% 차지"
  void: "검정 섹션에 파트너 로고 흑백 처리 (모노크로매틱)"
  trust_badge: "pill shape + gold/yellow 아이콘, 전환 구간에 배치"
animation:
  entrance: "slide-up, cubic-bezier(0.22,1,0.36,1) (elastic liquid ease)"
  glass_float: "slow subtle float animation on glassmorphic cards"
  button_hover: "scale(1.05) + shadow-lg"
  button_click: "active:scale(0.95) (squish)"
layout: [비대칭 리퀴드 섹셔닝(Yellow→Black 유기적 bleeding), 좌정렬 매시브 타이포 히어로, 글래스 데이터 카드 영역, Dark Void 로고 티커, pill CTA]
components:
  hero: "#FDE047 bg, 대형 헤딩 black text 좌정렬, 비대칭 하단 컷아웃"
  glass_card: "bg-white/10 + backdrop-blur-2xl + white border 20%, 우상단 Cyber Yellow pill badge"
  cta_button: "pill형, solid(bg-black/text-white 또는 bg-#FDE047/text-black), outline(border-black/20)"
  logo_ticker: "Dark Void 섹션, 파트너 로고 흑백/회색 처리"
special_notes:
  - "지배색 #FDE047은 flat 유지 — 그라데이션 절대 금지"
  - "border-radius 최소 극단값 사용 (pill 또는 100px+, 8~12px 금지)"
  - "고채도 영역은 타이포+컬러만 — 시각 잡음 금지"
```
