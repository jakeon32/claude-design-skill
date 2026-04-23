# Bold Editorial Design Style
source: superdesign.dev
category: dark

```yaml
palette: { navy: "#171e19", sage: "#b7c6c2", white: "#ffffff", taupe: "#9f8d8b", beige: "#d7c5b2", cyan: "#d5f4f9", soft_blue: "#bbe2f5", charcoal: "#302b2f" }
typography: { heading: "Anton", body: "Plus Jakarta Sans", weight: "Anton: 400(display) / Jakarta: 300~600", tracking: "tighter (heading) / widest (label, 12px uppercase)", size_hero: "18vw", size_section: "9xl / 7xl / 5xl" }
style_traits: [브루탈리스트 타이포 + 럭셔리 미니멀리즘, 다크 네이비 베이스, 에디토리얼 시네마틱, 에이전시 포트폴리오, 비대칭 마소리 그리드]
cursor: "crosshair"
effects:
  text_outline: "-webkit-text-stroke: 1px sage, color: transparent (2번째 헤드라인 라인)"
  nav_blend: "mix-blend-mode: difference, fixed, white 텍스트 (배경색 반전)"
  ambient_orbs: "384px div, blur(120px), opacity 20%, float 0→-20px 6s ease-in-out infinite"
  image_hover: "scale(1.1) + navy/60 overlay opacity 0→100, circular 'VIEW' badge 96px white"
  arrow_hover: "+8px translateX (링크 화살표)"
  line_hover: "가로선 40px→64px 연장 transition"
  scroll_reveal: "translateY(10px)→0 + opacity 0→1, 1000ms"
animation:
  timing: "cubic-bezier(0.16,1,0.3,1) 0.5s"
  float: "translateY 0→-20px, 6s ease-in-out infinite"
  nav_btn_hover: "white bg 슬라이드인"
border: "1px solid (white/sage 계열)"
layout: [fixed mix-blend-difference 네비, 100vh Navy 히어로(18vw Anton + 앰비언트 orbs), white 2-col 마소리 포트폴리오 그리드, Navy 비대칭 피처 섹션, light-gray 역량 12-col 그리드, charcoal 테스티모니얼 캐러셀, Navy 대형 푸터]
components:
  nav: "Anton 2xl tracking-widest 로고 / 12px uppercase 링크 / 1px white border 버튼(hover white bg)"
  hero: "18vw Anton uppercase leading-0.85 / 2행 text-outline(sage stroke) / 하단: 좌-Taupe 캡션 + 우-원형 border 바운싱 arrow"
  portfolio_grid: "2-col masonry, 짝수 아이템 4rem top margin, 3:4~4:5 이미지, hover: scale 1.1 + navy/60 + 원형 VIEW 배지"
  featured: "좌: 흑백 이미지 + cyan 20% 장식 정사각(-48px offset) / 우: sage Anton 레이블 + 7xl 헤딩 + taupe 본문"
  capabilities: "12-col split — 1-4col: taupe 레이블 + 수평선 프리픽스 리스트(40→64px) / 5-12col: 6xl light 헤딩(이탤릭 taupe 강조어)"
  testimonial: "charcoal bg, navy 30rem 따옴표 30% opacity 배경, Anton 5xl uppercase 인용, 64px 원형 아바타"
  footer: "Navy, Anton 9xl 'Let's Create', sage 4xl email(underline 8px offset), 1px white/10 border, 12px uppercase 저작권"
  view_badge: "absolute inset overlay navy/60 opacity-0→1 / 중앙 96px white circle / Anton 14px tracking-widest 'VIEW'"
special_notes:
  - "Anton + Plus Jakarta Sans — 다른 폰트 혼용 금지"
  - "mix-blend-mode: difference 네비 — 흰 배경 위 검정 전환 필수"
  - "앰비언트 orbs: sage + soft-blue 2개, blur 120px, float 애니메이션"
  - "마소리 그리드 짝수 카드 64px top offset — 비대칭 리듬 필수"
  - "crosshair 커서 전역 적용"
  - "배경 교차: Navy → White → Navy → Light Gray → Charcoal → Navy"
```
