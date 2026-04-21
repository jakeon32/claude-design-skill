# Chrome Extension Landing Page Style
source: superdesign.dev
category: light

```yaml
palette: { bg: "#f3f4f6", panel: "#ffffff", border: "#e5e7eb", border_md: "#d1d5db", cyan: "#06B6D4", traffic_red: "#ff5f57", traffic_yellow: "#febc2e", traffic_green: "#28c840", github_dark: "#0d1117" }
typography: { heading: "Inter", label: "JetBrains Mono", weight: "Inter: 500/600 / JetBrains Mono: 모든 기술 레이블·URL·단축키", size_hero: "72px leading-0.9", tracking: "normal (heading) / monospace 기본" }
style_traits: [Browser-Core Modernism, DevTools 미학, 브라우저 창 시뮬레이션, 중첩 뷰포트 구조, 기술 문서 느낌, 패턴 그리드 배경]
radius: "rounded-sm (브라우저 스타일 / GitHub README) — 전반적 미니멀"
shadow: "shadow-panel: 0 1px 3px 0 rgba(0,0,0,0.1)"
effects:
  pattern_grid: "20px linear-gradient #e5e7eb lines, 30% opacity — body 배경"
  browser_chrome: "macOS traffic lights (red/yellow/green circles), 탭 바, 주소창 (JetBrains Mono URL)"
  selection_box: "2px solid cyan (#06B6D4) border + 4px white offset, tag badge (cyan bg, white mono text)"
  cursor_demo: "시뮬레이션 커서가 카드 요소 사이 이동, dark inspector tooltip 트리거"
  inspector_tooltip: "#111827 dark bg, CSS properties cyan mono text"
  custom_scrollbar: "10px width, #d1d5db thumb"
animation:
  timing: "0.4s ease-in-out"
  cursor_sim: "cursor 이동 + 인스펙터 팝업 slide-up 애니메이션"
  version_tag: "pulse 애니메이션 'v2.0 RELEASED'"
layout: [전체 웹사이트 브라우저 창 컨테이너 내, split 히어로 (72px 기술 헤드라인 + cursor-demo / Version tag + Chrome Store CTA), 2col 변경로그 (300px left changelog + right mono feature list), 3-panel IDE 레이아웃 (256px 좌 explorer / center 패턴그리드 + cyan selection / 320px 우 property inspector), #0d1117 GitHub README block, centered FAQ <details>]
components:
  browser_frame: "tab bar (macOS traffic lights), active 탭 white bg, 주소창 (back/fwd icons + mono URL + extension cyan icon)"
  hero_left: "72px Inter leading-0.9, pulse version tag, Chrome Store 스타일 CTA (cyan bg, chrome icon)"
  cursor_demo: "시뮬레이션 UI 창 — 커서 이동 → dark inspector 팝업 (CSS cyan mono)"
  ide_explorer: "256px, vertical icons, Shortcuts footer (keybinding bordered boxes)"
  property_inspector: "320px, grid-cols-[80px_1fr] label-value, 10px mono gray 레이블, 16px color swatches"
  selection_component: "2px cyan border + 4px white offset + tag badge (element name + dimensions)"
special_notes:
  - "Inter (UI) + JetBrains Mono (기술 레이블) 조합"
  - "#06B6D4 cyan — active states + hover outlines"
  - "4px/8px 그리드 시스템"
  - "브라우저 창 시뮬레이션 전체 포함 필수"
```
