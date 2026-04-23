# Template: SaaS Landing Page

업종: SaaS / 스타트업 / 앱 서비스
목적: 신규 사용자 획득, 회원가입 유도
권장 스타일 태그: `futuristic, professional, minimal, b2b`

---

## 섹션 구조

```
① Navbar          — Logo + 메뉴 3-4개 + CTA 버튼 (우측)
② Hero            — 헤드라인 + 서브카피 + CTA 2개 + 제품 스크린샷/목업
③ Social Proof    — 로고 스트립 ("XXX가 신뢰합니다") 또는 수치 3개
④ Problem         — 고객이 겪는 문제 (3열 pain point 카드)
⑤ Solution        — 제품 해결책 (기능 하이라이트 2열: 이미지 + 설명)
⑥ Features        — 핵심 기능 3-6개 (아이콘 + 제목 + 설명 카드 그리드)
⑦ How it Works    — 3-4단계 프로세스 (번호 + 아이콘 + 설명)
⑧ Pricing         — 2-3개 티어 카드 (추천 티어 강조)
⑨ Testimonials    — 후기 3개 (아바타 + 이름 + 직책 + 인용)
⑩ FAQ             — 아코디언 5-7개
⑪ CTA Footer      — 최종 행동 유도 + 이메일 인풋 또는 버튼
⑫ Footer          — 링크 + 저작권
```

---

## 레이아웃 패턴

### Hero
```
[Navbar: Logo ————————————— 메뉴 | CTA버튼]

[Hero 전체 너비]
  좌 60%: H1 (큰 헤드라인)
          서브카피 (1-2줄)
          [Primary CTA]  [Secondary CTA]
          수치 배지 (예: "10,000+ 팀이 사용")
  우 40%: 제품 스크린샷 (살짝 기울인 카드 or 브라우저 프레임)

배경: 그라디언트 or 패턴 or 단색 히어로
```

### Features 그리드
```
[제목 중앙 정렬]
[서브 설명]

[ 카드1 ] [ 카드2 ] [ 카드3 ]
[ 카드4 ] [ 카드5 ] [ 카드6 ]

카드: 아이콘(top) + 제목 + 설명 2줄
```

### Pricing 카드
```
[ Free        ] [ Pro ★추천  ] [ Enterprise ]
  $0/월           $29/월          문의
  기능 목록        기능 목록        기능 목록
  [시작하기]       [지금 시작]      [문의하기]

추천 카드: border accent + 배지 "가장 인기"
```

---

## 콘텐츠 가이드라인

- **Hero 헤드라인**: 10-20자, 핵심 가치 제안 1문장
- **서브카피**: 2줄 이하, 대상 고객 + 핵심 결과
- **CTA**: 동사 시작 ("지금 시작하기", "무료로 써보기")
- **섹션 간격**: 80-120px
- **컨테이너**: max-width 1280px, 좌우 패딩 24px (모바일 16px)

---

## 브레이크포인트

```css
/* Mobile */ @media (max-width: 767px)  → Hero 1열, Features 1열
/* Tablet */ @media (max-width: 1023px) → Hero 1열, Features 2열
/* Desktop */ 기본값 → Hero 2열, Features 3열
```
