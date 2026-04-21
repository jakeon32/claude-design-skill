# Raw Form
source: superdesign.dev
category: light

```yaml
palette: { bg: "#E4E2DD", primary: "#1E1E1E", accent: "#DB4A2B", warm: "#F8A348", soft: "#FF89A9", surface: "#D9D6D0" }
typography: { heading: "Clash Display", body: "Satoshi", weight: "700/400-500", tracking: "-0.05em", leading: "0.75", transform: "uppercase" }
style_traits: [스위스 브루탈리즘 + 웜 팔레트, 타이포 드라마, 대기감 깊이, 컨테이너 없음, 브루탈리스트 포스터]
selection: "background #DB4A2B, color #FFFFFF"
scrollbar: "8px, thumb #DB4A2B, track #E4E2DD"
effects:
  blob_gradient: "60vw×60vw absolute div, blur(140px), mix-blend-mode: multiply, opacity pulse 0.6→0.9, 10-15s"
  entrance: "slide-up, cubic-bezier(0.16,1,0.3,1) 0.8s"
  product_hover: "scale(1.05), title color→#FF89A9"
  cta_fill: "white bg slides left→right on hover, text→#DB4A2B, 0.3s ease-out"
animation:
  blobs: "#DB4A2B + #F8A348 두 개, 느린 pulse + 미세 이동, 헤딩 뒤 레이어"
  nav_mobile: "mix-blend-mode: difference"
layout: [고정 미니멀 네비, 100vh 블롭 히어로(18vw 헤딩+15vw 인덴트), 3-col 보더리스 상품 그리드, 풀와이드 12vw 카테고리 디바이더, #1E1E1E 푸터]
components:
  hero: "18vw Clash Display uppercase, 2번째 줄 15vw 들여쓰기, 400px max 서브텍스트"
  category_divider: "128px padding, 12vw 헤딩 opacity 0.9, 좌우 교번 정렬"
  campaign_block: "#D9D6D0, 12-col: 8col 헤딩 + 4col 수직 스택(thin divider+arrow 링크)"
  cta_button: "border-radius 0, #1E1E1E bg, hover 시 white fill 슬라이드 + text #DB4A2B"
  footer: "#1E1E1E, '2024' 10vw rgba(255,255,255,0.1) 배경 텍스트 우정렬"
```
