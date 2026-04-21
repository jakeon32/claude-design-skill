# Super Travel
source: superdesign.dev
category: light

```yaml
palette: { bg: "#FDF8F3", surface: "#F5F0EB", primary: "#262626", accent: "#E4A4BD" }
typography: { heading: "League Spartan", body: "League Spartan", weight: "700-900/400", size_hero: "15vw", leading: "0.8", tracking_heading: "tighter", label: "10px bold uppercase tracking-[0.4em]" }
style_traits: [럭셔리 여행 에디토리얼, 더스티 로즈 시그니처, 기하학 타이포, 그레이스케일→컬러 reveal, 스태거드 포트폴리오]
radius: { card: "24px", portfolio: "16px", badge: "9999px (circle)" }
effects:
  glass_nav: "background rgba(253,248,243,0.8), backdrop-blur(12px), border 1px rgba(255,255,255,0.05)"
  image_hover: "grayscale(1)→grayscale(0), scale(1.08), 1s cubic-bezier(0.16,1,0.3,1)"
  card_hover: "bg #FDF8F3→#E4A4BD, icon color #E4A4BD→#262626"
animation:
  reveal_up: "opacity 0 + translateY(40px)→opacity 1 + translateY(0), 1s cubic-bezier(0.16,1,0.3,1), intersection observer threshold 0.15"
  badge_bounce: "translateY -5%→5%, 4s ease-in-out infinite"
  easing: "cubic-bezier(0.16,1,0.3,1) 전용 — 모든 reveal/hover 통일"
layout: [fixed 80px glass 네비(로고+중앙 10px uppercase 메뉴+pill CTA), 100vh 스플릿 히어로(좌: 15vw heading + 우: grayscale 카드), #F5F0EB 3-col 서비스 그리드, 2-col 스태거드 포트폴리오(짝수 +100px), 12-col 푸터]
components:
  hero: "15vw League Spartan, 특정 단어 lowercase italic #E4A4BD, 우: grayscale image card 24px radius, 플로팅 배지"
  concierge_badge: "160px circle #E4A4BD bg, 3xl italic '01' + 8px uppercase 텍스트, 4s bounce"
  service_card: "40px padding, 4xl 아이콘, h3 bold uppercase + p small, hover bg→#E4A4BD"
  portfolio_item: "3:4 이미지 16px radius, 짝수 아이템 +100px 하단 오프셋, hover 96px 블랙 원('View Case' 10px white)"
  portfolio_meta: "10px #E4A4BD bold label + 3xl 타이틀 + bullet 구분 태그"
  footer: "#F5F0EB, 12-col: 5col 브랜드+미션 + 7col 3서브컬(네비/소셜/지역), #E4A4BD 헤더 8px 오프셋 밑줄"
special_notes:
  - "League Spartan 단일 폰트 — 헤딩+바디 동일 패밀리"
  - "그라데이션 금지 — solid 뮤트 컬러만"
  - "이미지 기본 grayscale, 인터랙션에서만 컬러 reveal"
```
