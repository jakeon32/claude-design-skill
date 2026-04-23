# Digital Luxury Editorial
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#050505", footer_bg: "#0A0A0A", primary: "#FFFFFF", muted: "rgba(255,255,255,0.4)", border: "rgba(255,255,255,0.05)" }
glow_accents: { orange: "#F97316 blur(120px) opacity 5-10%, mix-blend-mode: screen", blue: "#1E3A8A blur(120px) opacity 5-10%, mix-blend-mode: screen" }
typography: { heading: "Clash Display", body: "Inter", weight: "700/300-400", size_hero: "15vw", tracking: "-0.05em (tracking-tighter)", label: "10px uppercase bold tracking-[0.2em]" }
style_traits: [디지털 럭셔리, 브루탈리스트 타이포 + 하이엔드 패션, 인지적 명료함, 대기 라이트 리크, 고대비 흑백 기반]
radius: "2px (sharp near-square, 4px 초과 금지)"
border: "rgba(255,255,255,0.05) — ultra-subtle"
effects:
  light_leaks: "절대위치 pill div, blur(120px), orange 우상단 + blue 좌하단 (히어로/푸터 각도 배치)"
  nav_blend: "mix-blend-mode: difference, text #FFFFFF — 밝은 이미지 위 자동 반전 흑색"
  image_hover: "scale 5-10%, 2s ease-out"
  gallery_overlay: "black overlay → opacity 0 on hover, caption 좌하단 hover-only"
animation:
  reveal_up: "translateY(40px)→0, opacity 0→1, cubic-bezier(0.22,1,0.36,1) 1s"
  stats_stagger: "셀별 0.1s delay 증분"
  explore_arrow: "border-bottom + arrow icon hover translate"
layout: [fixed 100px mix-blend-difference 네비(pill border contact 버튼), 100vh 히어로(4:5 이미지 + 15vw 타이포 이미지 하단 좌측 오버랩), 4-col 스탯 밴드, 12-col 에디토리얼 블록(1-3 sticky + 5-12 narrative), 21:9 패럴랙스 갤러리, #0A0A0A 중앙정렬 푸터]
components:
  hero: "15vw Clash Display 이미지 하단-좌 오버랩, 우: float 64px 1-2 문장 low-opacity"
  stats_band: "border-t rgba(255,255,255,0.05), 4-col, 10px label + 2xl 수치, stagger reveal"
  editorial_block: "12-col: 1-3 sticky 01/02 인덱스 + 5-12 xl+ 본문, 80px+ 거터"
  contact_btn: "pill border-white/20 → solid white bg on hover"
  ghost_brand: "opacity 0.1, 극대형, 푸터 하단 부분 컷오프"
special_notes:
  - "화이트 on 블랙 고대비 유지 필수"
  - "고품질 고대비 사진 (흑백/뮤트 컬러 권장)"
  - "코너 4px 초과 금지"
  - "narrative 블록 60-80자 line length 유지"
```
