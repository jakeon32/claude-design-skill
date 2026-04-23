# Kinetic Orange
source: superdesign.dev
category: grunge

```yaml
palette: { bg: "#FF4D00", primary: "#000000", white: "#FFFFFF" }
typography: { heading: "Archivo Black", body: "Inter", mono: "Space Mono", weight: "900/400", transform: "uppercase (Archivo Black 전용)", tracking_heading: "-0.04em", tracking_mono: "-0.02em", leading: "0.85-0.9", size_hero: "16vw", size_service: "7vw", size_cta: "14vw" }
style_traits: [디지털 브루탈리즘, 키네틱 오렌지, 3색 시스템(오렌지/블랙/화이트), 급박한 에너지, 기하학적 레이아웃]
border: "2px solid #000000"
selection: "background #000000, color #FF4D00"
radius: "0px (pill 네비게이션 + 라운드 버튼 제외)"
shadow: "네비게이션 depth 전용 — 그 외 drop shadow 금지"
effects:
  skew: "마키 섹션 -2deg 기울기"
  hover: "translate-x-4(16px) + scale-110"
  arrow_reveal: "opacity 0→1 + rotate(45deg) on hover"
animation:
  marquee_row1: "#FF4D00 Archivo Black 10vw, linear infinite"
  marquee_row2: "white 80% opacity, 역방향 스크롤"
  spin: "SVG textPath 360deg, 12s linear infinite"
layout: [고정 플로팅 pill 네비(black bg), 100vh 16vw 타이포 히어로(2px 구분선+메타 row), -2deg 스큐 마키(black bg), 수직 서비스 리스트, 14vw CTA, 2px top border 풋터]
components:
  nav: "pill rounded-full black bg, Space Mono 12px white links(hover→black text white bg)"
  hero: "16vw Archivo Black 중앙, 하단 메타 row: 좌(Based in) + 중(회전 Scroll Down SVG) + 우(타이틀)"
  skew_marquee: "bg-black -2deg skew, row1: #FF4D00 10vw / row2: white/80 역방향"
  service_item: "top border white/20, [#FF4D00 인덱스] [타이틀+태그] [오렌지 화살표], hover: bg white/5 + +16px + 45deg 화살표"
  scroll_indicator: "144px circle, SVG textPath 'Scroll Down •' ×3-4, 중앙 arrow-down, 12s 회전"
  cta_button: "rounded-full black bg white text"
special_notes:
  - "3색(오렌지/블랙/화이트) 외 색상 절대 금지"
  - "그라데이션/드롭쉐도우(네비 제외) 금지"
  - "Archivo Black 헤딩 uppercase 필수"
  - "버튼/네비 pill 제외 모든 코너 sharp"
```
