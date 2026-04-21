# Dark Matte Editorial
source: superdesign.dev
category: dark

```yaml
palette: { bg: "#181818", primary: "#EBDCC4", secondary: "#B6A596", accent: "#DC9F85", border: "#66473B", divider: "#35211A" }
typography: { heading: "Clash Grotesk", body: "General Sans", weight: "700/300-400", size_hero: "11.5vw (desktop) / 16vw (mobile)", leading: "0.85", tracking: "tight", transform: "uppercase" }
style_traits: [조용한 자신감, 다크 매트 에디토리얼, 어시 웜 톤, 배타성 표현, 아이콘/소프트쉐도우/그라데이션 없음]
radius: "4px max (pill 형태 절대 금지)"
border: "1px solid #66473B 또는 #35211A"
shadow: "없음 — 텍스트 레이어링으로만 깊이 표현"
effects:
  noise: "SVG fractal noise, opacity 0.03, position fixed 전체 뷰포트"
  text_depth: "레이어 1(뒤): -webkit-text-stroke 1px #66473B, color transparent, offset 4px 4px / 레이어 2(앞): color #EBDCC4 — 동일 font 완벽 정렬 필수"
animation:
  badge_rotate: "SVG text path 'WAITING LIST •' 무한 회전, 12s linear"
  status_pulse: "8px circle #DC9F85 pulse (배치 003 표시)"
layout: [absolute 미니멀 네비(좌: 브랜드ID + 중: 1px 라인 스페이서 + 우: INVITE ONLY), 엣지투엣지 히어로(11.5vw 레이어드 텍스트), 수평 #35211A 구분선, 12-col 하단 그리드]
components:
  nav: "absolute 포지션, 좌: 'SD—PROTOCOL 01' #B6A596 uppercase wide-tracking / 우: 'INVITE ONLY' 10-12px #35211A"
  hero: "11.5vw Clash Grotesk uppercase leading-0.85, 아웃라인 레이어(offset 4px) + 솔리드 레이어 이중 구조"
  early_access_label: "24px horizontal line #DC9F85 + uppercase #B6A596 텍스트"
  bottom_grid: "12-col: col1-5(exclusivity 문구 + 8px dot status) / col7-12(이메일 폼)"
  email_form: "투명 input(1px #66473B border, 4px 좌측 radius) + solid #DC9F85 버튼(4px 우측 radius) — 연결된 단일 블록"
  waitlist_badge: "64×64px circle, 1px #35211A border, SVG text path 회전 12s, 우하단 fixed"
special_notes:
  - "그라데이션/박스쉐도우/pill 버튼 절대 금지"
  - "헤딩 line-height 0.85 엄격 유지"
  - "팔레트 어시 웜 톤만 — 일반 테크 컬러 금지"
  - "노이즈 오버레이 fixed 전체 뷰포트 필수"
```
