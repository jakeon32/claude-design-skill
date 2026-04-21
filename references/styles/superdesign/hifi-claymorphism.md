# HiFi Claymorphism
source: superdesign.dev
category: light

```yaml
palette: { bg: "#F4F1FA", text: "#332F3A", muted: "#635F69", violet: "#7C3AED", pink: "#DB2777", blue: "#0EA5E9", green: "#10B981", amber: "#F59E0B" }
gradient:
  button: "bg-gradient-to-br from-[#A78BFA] to-[#7C3AED]"
  icon_orb: "from-[color-400] to-[color-600]"
  text: "from-#332F3A 20% to-#7C3AED 60% to-#DB2777 (text-5xl+ only)"
typography: { heading: "Nunito", body: "DM Sans", weight: "900/400-500", size_hero: "text-5xl→6xl→7xl→8xl", leading_hero: "1.1" }
style_traits: [프리미엄 디지털 클레이, 캔디스토어 컬러, 제로 샤프코너, 물리 기반 그림자, 촉각적 반응 UI]
radius: { container: "48-60px", card: "32px", medium: "24px", button: "20px", orb: "full", badge: "full" }
shadows:
  deep_clay: "30px 30px 60px #CDC6D9, -30px -30px 60px #FFFFFF, inset 10px 10px 20px rgba(139,92,246,0.05), inset -10px -10px 20px rgba(255,255,255,0.8)"
  clay_card: "16px 16px 32px rgba(160,150,180,0.2), -10px -10px 24px rgba(255,255,255,0.9), inset 6px 6px 12px rgba(139,92,246,0.03), inset -6px -6px 12px rgba(255,255,255,1)"
  clay_button: "12px 12px 24px rgba(139,92,246,0.3), -8px -8px 16px rgba(255,255,255,0.4), inset 4px 4px 8px rgba(255,255,255,0.4), inset -4px -4px 8px rgba(0,0,0,0.1)"
  clay_pressed: "inset 10px 10px 20px #D9D4E3, inset -10px -10px 20px #FFFFFF"
animation:
  float: "translateY 0→-20px + rotate 0→2deg, 8s infinite"
  breathe: "scale 1→1.02, 6s infinite (stat orbs)"
  hover_lift: "카드 -translate-y-2, 버튼 -translate-y-1"
  press: "active:scale-[0.92] + shadow-clayPressed"
layout: [#F4F1FA + 3-4 animated blobs 배경, bento/masonry 비균등 그리드, split 50/50 레이아웃]
components:
  card: "rounded-[32px], bg-white/60~80, backdrop-blur-xl, shadow-clayCard, hover:-translate-y-2"
  button: "gradient violet, rounded-[20px], h-14, active:scale-[0.92]+shadow-clayPressed"
  input: "rounded-2xl, h-16, bg-[#EFEBF5], shadow-clayPressed(recessed)"
  blob: "60vh×60vh absolute, rounded-full, blur-3xl, accent/10, clay-float animation"
special_notes:
  - "rounded-md/rounded-sm 금지 — 최소 rounded-[20px]"
  - "그림자 4레이어 스택 필수 — 단일 그림자 금지"
  - "gradient text는 text-5xl+ only"
  - "flat 배경 금지 — animated blob 필수"
```
