# Style Recommender

사용자 설명 → 스타일 자동 추천 로직.
스타일 미지정 시 DesignSystemManager가 이 파일을 참조해 top 3 후보를 제시.

---

## 0. 5개 디자인 철학 유파 (Design Philosophy Schools)

스타일 추천 시 이 분류를 먼저 참고. 같은 유파 내에서 추천하면 일관성 높음.

| 유파 | 핵심 정신 | 대표 스타일 |
|-----|---------|-----------|
| **정보 건축** (Information Architecture) | 데이터와 타이포가 구조 자체 | Swiss Minimalist, Bauhaus, Architectural Blueprint, Cyber Serif |
| **키네틱 시학** (Kinetic Poetics) | 모션·스크롤이 내러티브를 만듦 | Kinetic Typography, Neon Velocity, Synapse |
| **미니멀리즘** (Minimalism) | 제거가 표현이다, 여백이 메시지 | Minimal Dark, Neumorphism, Minimalist Beta, Dark Matte Editorial |
| **실험 전위** (Experimental Vanguard) | 규칙을 깨서 주목을 얻는다 | Neo Brutalism, Cyberpunk, Acid Graphic, Deep Red |
| **동양 철학** (Eastern Philosophy) | 비움이 콘텐츠다, 간결한 절제 | Organic, Botanical, Tectonic Stone, Cinematic Noir |

→ 사용자 키워드가 명확히 한 유파에 속하면 그 유파 내에서 3가지 추천.  
→ 유파 경계가 모호하면 서로 다른 유파에서 1개씩 교차 추천.

---

## 1. 신호 추출 규칙

사용자 설명에서 아래 차원을 추출:

| 차원 | 감지 키워드 예시 |
|------|----------------|
| **tone** | 어둡, 다크, 밝, 라이트, 모던, 깔끔 |
| **mood** | 세련, 미래적, 고급, 미니멀, 귀여운, 강렬, 편안, 빈티지, 레트로, 기술적, 개발자, 펑크, 럭셔리, 자연, 유기적 |
| **industry** | SaaS, 스타트업, 포트폴리오, 패션, 금융, 핀테크, AI, 크립토, 의료, 헬스, 교육, 이커머스, 미디어, 에이전시, 여행 |
| **audience** | B2B, 기업, 개인, 소비자, 개발자, 디자이너 |
| **complexity** | 심플, 복잡, 화려, 정보 많은, 타이포 중심 |

---

## 2. 스타일 태그 인덱스

형식: `스타일명 | 파일경로 | tone | mood[] | industry[] | audience | complexity`

### Dark Styles (superdesign)

| 스타일 | 파일 | tone | mood | industry | audience | complexity |
|--------|------|------|------|----------|----------|------------|
| Futuristic SaaS | superdesign/futuristic-saas.md | dark | futuristic, professional | saas, ai, startup | b2b | moderate |
| Neural Noir | superdesign/neural-noir.md | dark | luxurious, futuristic, ai | ai, brand, startup | b2b | moderate |
| Synapse | superdesign/synapse.md | dark | futuristic, energetic | ai, saas, startup | b2b | moderate |
| Linear / Modern | designprompts/linear-modern.md | dark | futuristic, professional, minimal | saas, startup | b2b | minimal |
| Midnight Editorial | superdesign/midnight-editorial.md | dark | editorial, professional, minimal | brand, media | creative | moderate |
| Cinematic Dark | superdesign/cinematic-dark.md | dark | cinematic, futuristic, editorial | portfolio, brand | creative | maximal |
| Cinematic Noir | superdesign/cinematic-noir.md | dark | cinematic, minimal, luxurious | gallery, portfolio | creative | minimal |
| Digital Luxury Editorial | superdesign/digital-luxury-editorial.md | dark | luxurious, editorial, brutalist | fashion, brand | b2c | maximal |
| Dark Matte Editorial | superdesign/dark-matte-editorial.md | dark | editorial, minimal, professional | brand, consulting | b2b | minimal |
| Tectonic Stone | superdesign/tectonic-stone.md | dark | minimal, futuristic, architectural | brand, portfolio | creative | minimal |
| Architectural Blueprint | superdesign/architectural-blueprint.md | dark | technical, minimal | architecture, engineering | b2b | minimal |
| Red Noir | superdesign/red-noir.md | dark | technical, edgy, futuristic | startup, saas, tech | b2b | moderate |
| Neon Velocity | superdesign/neon-velocity.md | dark | futuristic, edgy, energetic | startup, gaming, tech | b2c | moderate |
| Minimalist Beta | superdesign/minimalist-beta.md | dark | minimal, professional | saas, startup | b2b | minimal |
| Disruptor Beta | superdesign/disruptor-beta.md | dark | brutalist, edgy | startup, tech | b2c | moderate |
| Deep Red | superdesign/deep-red.md | dark | surreal, edgy | creative, brand | creative | maximal |
| Dark Avant-Garde | superdesign/dark-avant-garde.md | dark | edgy, editorial, brutalist | creative, brand | creative | moderate |
| Cyber Serif | superdesign/cyber-serif.md | dark | technical, minimal, editorial | developer, saas | developer | minimal |
| Acid Graphic | superdesign/acid-graphic.md | dark | edgy, surreal, technical | music, creative, tech | creative | maximal |
| Hyper-Saturated Fluid | superdesign/hyper-saturated-fluid.md | dark | futuristic, professional | fintech, startup | b2b | moderate |
| Editorial Poster Dark | superdesign/editorial-poster-dark.md | dark | editorial, typographic | brand, creative | creative | moderate |
| Vaporwave Dark | superdesign/vaporwave-dark.md | dark | retro, playful | gaming, creative | b2c | maximal |
| Grunge Collage Motion | superdesign/grunge-collage-motion.md | dark | edgy, retro, playful | creative, music, brand | creative | maximal |
| Refined Grunge | superdesign/refined-grunge.md | dark | edgy, technical, minimal | music, creative, developer | creative | minimal |
| Terminal CLI | designprompts/terminal-cli.md | dark | technical, edgy | developer, saas | developer | minimal |
| Minimalist Dark | designprompts/minimalist-dark.md | dark | minimal, professional | saas, app | b2b | minimal |
| Bold Typography | designprompts/bold-typography.md | dark | editorial, typographic, minimal | brand, creative | creative | minimal |
| Kinetic Typography | designprompts/kinetic-typography.md | dark | edgy, typographic, editorial | brand, creative | creative | moderate |
| Art Deco | designprompts/art-deco.md | dark | luxurious, retro, editorial | luxury, finance, brand | b2c | moderate |
| Cyberpunk / Glitch | designprompts/cyberpunk-glitch.md | dark | futuristic, edgy, technical | gaming, tech, creative | b2c | maximal |
| Bitcoin DeFi | designprompts/bitcoin-defi.md | dark | futuristic, technical | finance, crypto, saas | b2b | moderate |
| Vaporwave / Outrun | designprompts/vaporwave-outrun.md | dark | retro, edgy, futuristic | gaming, creative, music | b2c | maximal |
| Maximalism / Dopamine | designprompts/maximalism-dopamine.md | dark | maximalist, playful, edgy | entertainment, creative | b2c | maximal |

### Light / Neutral Styles (superdesign)

| 스타일 | 파일 | tone | mood | industry | audience | complexity |
|--------|------|------|------|----------|----------|------------|
| Bold Editorial Design | superdesign/bold-editorial-design.md | light | editorial, professional, brutalist | agency, portfolio | creative | moderate |
| Super Travel | superdesign/super-travel.md | light | luxurious, editorial | travel, lifestyle | b2c | moderate |
| Poster Modernist | superdesign/poster-modernist.md | light | editorial, minimal | brand, creative | creative | minimal |
| Season 04 | superdesign/season-04.md | light | luxurious, brutalist, editorial | fashion, brand | b2c | maximal |
| Forest & Sage | superdesign/forest-sage.md | light | organic, editorial, minimal | lifestyle, wellness | b2c | minimal |
| Raw Form | superdesign/raw-form.md | light | brutalist, minimal, editorial | brand, architecture | creative | minimal |
| Material You (MD3) | superdesign/material-you-md3.md | light | professional, playful | app, consumer | b2c | moderate |
| Sophisticated Playful | superdesign/sophisticated-playful.md | light | playful, professional | wellness, education, family | b2c | moderate |
| HiFi Claymorphism | superdesign/hifi-claymorphism.md | light | playful, modern, luxurious | app, consumer, saas | b2c | moderate |
| Bold Editorial Studio | superdesign/bold-editorial-studio.md | light | editorial, minimal, typographic | brand, portfolio | creative | minimal |
| Echo Minimalist | superdesign/echo-minimalist.md | light | minimal, luxurious | brand, portfolio | creative | minimal |
| Neo-Brutalist SaaS | superdesign/neo-brutalist-saas.md | light | brutalist, playful | saas, startup | b2b | moderate |
| Architectural Type System | superdesign/architectural-type-system.md | light | technical, minimal, brutalist | saas, developer | developer | minimal |
| Obsidian & Lime | superdesign/obsidian-lime.md | light | technical, modern | saas, tech | b2b | moderate |
| Warm Industrial Gray | superdesign/warm-industrial-gray.md | light | industrial, editorial, minimal | brand, portfolio | creative | minimal |
| Mosaic Grid | superdesign/mosaic-grid.md | light | playful, modern | brand, startup | b2c | moderate |
| Neo-Brutalism Acid | superdesign/neo-brutalism-acid.md | light | brutalist, edgy, playful | startup, creative | b2c | moderate |
| Softly Digital Wellness | superdesign/softly-wellness.md | light | organic, playful, minimal | wellness, health | b2c | minimal |
| Chrome Extension Landing | superdesign/chrome-extension.md | light | technical, minimal | developer, saas | developer | minimal |
| Organic Editorial | superdesign/organic-editorial.md | light | organic, editorial, minimal | brand, lifestyle | creative | minimal |
| Red Sun | superdesign/red-sun.md | light | editorial, energetic | brand, startup | b2c | moderate |
| Clean Fluid Organic | superdesign/clean-fluid.md | light | modern, minimal, organic | saas, startup, brand | b2b | moderate |
| Tech Editorial | superdesign/tech-editorial.md | light | technical, editorial, minimal | media, saas | b2b | minimal |
| Bold Retro-Modernism | superdesign/bold-retro-modernism.md | light | retro, editorial, playful | brand, creative | creative | moderate |
| Kinetic Orange | superdesign/kinetic-orange.md | light | brutalist, energetic, edgy | startup, creative, tech | b2c | maximal |
| Glassmorphism Card | superdesign/glassmorphism-card.md | neutral | modern, professional | saas, app | b2b | moderate |

### designprompts Styles

| 스타일 | 파일 | tone | mood | industry | audience | complexity |
|--------|------|------|------|----------|----------|------------|
| Flat Design | designprompts/flat-design.md | light | minimal, playful, modern | app, saas, startup | b2c | minimal |
| Swiss Style | designprompts/swiss-style.md | light | editorial, minimal, technical | brand, corporate | b2b | minimal |
| Minimalist Monochrome | designprompts/minimalist-monochrome.md | light | minimal, editorial, luxurious | brand, portfolio | creative | minimal |
| Sketch Hand-Drawn | designprompts/sketch-hand-drawn.md | light | playful, organic | education, creative, startup | b2c | minimal |
| Playful Geometric | designprompts/playful-geometric.md | light | playful, maximalist | education, app, startup | b2c | moderate |
| Bauhaus | designprompts/bauhaus.md | light | editorial, minimal, technical | brand, design, creative | creative | minimal |
| Luxury Editorial | designprompts/luxury-editorial.md | light | luxurious, editorial | fashion, brand, lifestyle | b2c | moderate |
| Win98 Retro | designprompts/win98-retro.md | light | retro, playful, technical | creative, developer | creative | maximal |
| Neumorphism | designprompts/neumorphism.md | light | minimal, modern, soft | app, dashboard | b2b | minimal |
| Newsprint | designprompts/newsprint.md | light | editorial, minimal, retro | media, news, brand | b2b | minimal |
| Minimalist Modern | designprompts/minimalist-modern.md | light | modern, minimal, professional | saas, startup | b2b | minimal |
| Neo-Brutalism | designprompts/neo-brutalism.md | light | brutalist, playful, edgy | startup, creative | b2c | moderate |
| Academia / Classical | designprompts/academia-classical.md | light | luxurious, editorial, minimal | education, brand, publishing | b2b | moderate |
| HiFi Claymorphism (DP) | designprompts/hifi-claymorphism-dp.md | light | playful, modern | app, consumer | b2c | moderate |
| Serif | designprompts/serif.md | light | minimal, luxurious, editorial | brand, portfolio, luxury | b2c | minimal |
| Botanical / Organic Serif | designprompts/botanical-organic.md | light | organic, minimal, luxurious | wellness, lifestyle, brand | b2c | minimal |
| Corporate Trust | designprompts/corporate-trust.md | light | professional, modern | enterprise, saas, finance | b2b | moderate |
| Hand-Drawn | designprompts/hand-drawn.md | light | playful, organic | education, personal, creative | b2c | minimal |
| Industrial Skeuomorphism | designprompts/industrial-skeuomorphism.md | light | technical, retro, edgy | developer, industrial | developer | moderate |
| Organic / Natural | designprompts/organic-natural.md | light | organic, minimal | wellness, food, lifestyle | b2c | minimal |
| Retro / 90s Nostalgia | designprompts/retro-90s-nostalgia.md | light | retro, playful, technical | creative, gaming, startup | b2c | maximal |

---

## 3. 추천 알고리즘

```
1. 사용자 설명에서 신호 추출 (섹션 1 기준)
2. 아래 우선순위로 태그 매칭:
   a. industry 일치 (가중치 3)
   b. mood 일치 (가중치 2)
   c. tone 일치 (가중치 2)
   d. audience 일치 (가중치 1)
   e. complexity 일치 (가중치 1)
3. 점수 합산 → 상위 3개 선정
4. 동점 시: superdesign 스타일 우선
5. 단, 같은 mood 그룹에서 3개 다 나오지 않도록 다양성 확보
   (e.g. dark futuristic 3개 → 2개로 제한, 나머지 1개는 차순위 다른 mood)
```

---

## 4. 출력 형식

```
💡 설명을 바탕으로 스타일 3가지를 추천합니다:

① [스타일명]
   [한 줄 무드 설명]
   주색: [primary hex] + [accent hex] / 배경: [bg hex]
   → 이 설명에 맞는 이유: [1문장]

② [스타일명]
   ...

③ [스타일명]
   ...

번호로 선택하거나, "직접 고를게요"라고 말씀해주세요.
(선택 후 바로 DESIGN_SYSTEM 설정으로 진행합니다)
```

---

## 5. 엣지 케이스

| 상황 | 처리 |
|------|------|
| 신호가 너무 적음 ("디자인 만들어줘"만) | tone/mood/industry를 직접 한 줄 질문 후 추천 |
| 상충하는 신호 ("미니멀하면서 화려하게") | 두 신호 모두 반영한 moderate complexity 스타일 우선 |
| 한국 시장 명시 | korean-typography.md 병합 조건 추가 |
| 이미 스타일 명시 | 이 파일 참조 불필요, 기존 B 분기로 직접 로드 |
