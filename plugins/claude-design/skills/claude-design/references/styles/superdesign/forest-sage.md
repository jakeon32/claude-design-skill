# Forest & Sage
source: superdesign.dev
category: light

```yaml
palette: { bg: "#FEFAE0", primary: "#01472E", sage: "#CCD5AE", olive: "#E9EDC9", moss: "#A3B18A" }
typography: { heading: "Anton", body: "Inter", weight: "900/400-700", size_hero: "23vw", size_section: "15vw", leading: "0.75", tracking_heading: "-0.05em", tracking_label: "0.2em-0.4em", transform: "uppercase (labels/buttons)" }
style_traits: [어시 하이엔드 에디토리얼, 인더스트리얼 타이포 + 유기적 컬러, 플로팅 패럴랙스, 색상 블록 섹션, 아날로그 노이즈]
radius: { section: "5rem (대형 컨테이너 필수)", card: "2.5rem", floating_img: "3rem" }
shadow: "shadow-2xl + rgba(1,71,46,0.2) Forest 틴트"
effects:
  noise: "SVG fractal noise, opacity 0.04, position fixed (전체 뷰포트)"
  dark_text: "#01472E 필수 (검정 금지)"
animation:
  reveal: "translateY(100px)→0, opacity 0→1, cubic-bezier(0.16,1,0.3,1) 1.2s"
  stagger: "글자별 0.05s delay (히어로 헤딩)"
  float: "translateY(0)→(-20px), rotate(0→5deg), 50% 반전, infinite"
  parallax: "scroll depth × 0.05 추가 translateY"
layout: [고정 네비(pill backdrop-blur 20px), 100vh Sage bg 히어로(플로팅 유기적 이미지 2-3개), Olive bg 상품 그리드(5rem 상단 라운드), #01472E 푸터]
components:
  hero: "23vw Anton 글자별 stagger reveal, floating 재료 이미지 3rem radius 패럴랙스"
  nav: "logo (hyphen prefix), center pill blur, right cart+counter badge white pill"
  product_grid: "15vw Anton 헤딩 + 원형 CTA 버튼, 3-col 4/5 비율, hover blur-reveal"
  blur_reveal: "Forest 30% overlay + blur(2px), white 버튼 translateY -32px 슬라이드업"
  footer: "#01472E bg, 12-col: 6col 뉴스레터(underline-only input) + 6col 2단 링크"
special_notes:
  - "모든 곡선 5rem 이상, sharp corner 절대 금지"
  - "노이즈 오버레이 항상 유지 (analog feel)"
  - "cubic-bezier(0.16,1,0.3,1) 모든 트랜지션에 통일"
  - "어두운 텍스트 = #01472E (검정 #000000 금지)"
```
