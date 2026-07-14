/**
 * slide-lint.js — 슬라이드 빌드 게이트 (Puppeteer)
 *
 * ─ 왜 이 파일이 있는가 ─────────────────────────────────────────────
 * 2026-07-14 이전, 모든 .slide 에 `overflow:hidden` 이 걸려 있었다.
 * 내용이 넘치면 **에러도 경고도 없이 그냥 잘려 나갔다.** 무증상 정보 손실.
 *
 * 규격은 문서가 아니라 코드에 둔다. 이 린터가 세 가지를 강제한다:
 *   ① 넘침 (scrollHeight)
 *   ② 안전영역 이탈 (getBoundingClientRect) — absolute/음수마진은 ①로 안 잡힌다
 *   ③ 폰트 하한 (밀도 등급별) — 축소로 오버플로를 "해결"한 흔적 적발
 *
 * 넘치면 exit 1. 자동으로 폰트를 줄여 해결하지 않는다.
 * 대응은 density-rules.md §5 결정 트리:
 *   삭제 → 분할 → 부록 → 열/등급 → 폰트(1단계) → 실패
 *
 * 사용: node slide_lint.js <deck.html>
 * ──────────────────────────────────────────────────────────────────
 */

const path = require('path');
const fs = require('fs');

/** 밀도 등급별 본문 폰트 절대 하한 (px). density-rules.md §4 */
const FLOOR = { D1: 32, D2: 24, D3: 16 };

/** 안전영역 (1280×720 기준). density-rules.md §1
 *  bottom(680)  = 본문 하한. 출처·각주는 이 아래 밴드(672~700)에 놓인다.
 *  hardBottom(704) = 캔버스 절대 경계 — 무엇도 이걸 넘으면 잘린다. */
const SAFE = { top: 40, right: 1216, bottom: 680, left: 64, hardBottom: 704 };

/** 각주·출처는 하한 예외 (본문이 아니므로) */
const NOTE_SELECTOR = '.source, .footnote, .note, figcaption';

/** 시스템 Chrome 후보 (puppeteer-core 사용 시 executablePath 필수) */
const CHROME_PATHS = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
];

/** puppeteer(번들 Chromium) 우선, 없으면 puppeteer-core + 시스템 Chrome */
function loadPuppeteer() {
  try {
    return { pptr: require('puppeteer'), execPath: null };
  } catch (_) { /* fall through */ }
  const pptr = require('puppeteer-core');       // x-scraping 등에 이미 설치돼 있음
  const execPath = CHROME_PATHS.find(p => fs.existsSync(p));
  if (!execPath) {
    throw new Error(
      'puppeteer 미설치 + 시스템 Chrome도 못 찾음.\n' +
      '  npm i puppeteer   또는  Chrome 설치 후 재시도'
    );
  }
  return { pptr, execPath };
}

async function lint(htmlPath) {
  const { pptr, execPath } = loadPuppeteer();
  const browser = await pptr.launch({
    headless: 'new',
    ...(execPath ? { executablePath: execPath } : {}),
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'networkidle0' });

  const errors = await page.evaluate((FLOOR, SAFE, NOTE_SELECTOR) => {
    const errs = [];
    const slides = document.querySelectorAll('.slide');

    slides.forEach((s, i) => {
      const n = i + 1;
      const tier = s.dataset.density || 'D2';
      const floor = FLOOR[tier];
      if (!floor) { errs.push(`slide ${n}: 알 수 없는 density "${tier}" (D1/D2/D3)`); return; }

      // ─── ① 넘침 (스크롤 오버플로) ───────────────────────────────
      // [data-fit] 을 단 컨테이너만 검사한다. 없으면 .body 를 본다.
      const fitEls = s.querySelectorAll('[data-fit], .body');
      fitEls.forEach(el => {
        const dy = el.scrollHeight - el.clientHeight;
        const dx = el.scrollWidth - el.clientWidth;
        if (dy > 1) {
          errs.push(
            `slide ${n}: 세로 넘침 ${dy}px @${tier} (floor ${floor}px) ` +
            `— density-rules.md §5 결정트리: 삭제 → 분할 → 부록 → 열/등급 → 폰트`
          );
        }
        if (dx > 1) errs.push(`slide ${n}: 가로 넘침 ${dx}px`);
      });

      // ─── ② 안전영역 이탈 ──────────────────────────────────────
      // absolute 배치·음수 마진·transform 은 scrollHeight 에 안 잡힌다. 반드시 병행 검사.
      // 출처·각주는 하단 별도 밴드(y 672~700)에 놓이는 게 정상 → 본문 안전영역 검사 제외,
      // 대신 캔버스 절대 경계(SAFE.hardBottom)만 확인한다.
      const sb = s.getBoundingClientRect();
      s.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (!r.width || !r.height) return;
        const x1 = r.left - sb.left, y1 = r.top - sb.top;
        const x2 = r.right - sb.left, y2 = r.bottom - sb.top;
        const isNote = el.closest(NOTE_SELECTOR);
        const bottomLimit = isNote ? SAFE.hardBottom : SAFE.bottom;

        if (x1 < SAFE.left - 1 || x2 > SAFE.right + 1 ||
            y1 < SAFE.top - 1  || y2 > bottomLimit + 1) {
          const tag = el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).split(' ')[0] : '');
          errs.push(
            `slide ${n}: 안전영역 이탈 <${tag}> ` +
            `(${Math.round(x1)},${Math.round(y1)})-(${Math.round(x2)},${Math.round(y2)}) ` +
            `/ safe ${SAFE.left},${SAFE.top}-${SAFE.right},${bottomLimit}`
          );
        }
      });

      // ─── ③ 폰트 하한 ─────────────────────────────────────────
      // 축소로 오버플로를 "해결"한 흔적을 잡는다.
      s.querySelectorAll('p, li, td, th, span, div').forEach(el => {
        if (!el.textContent.trim()) return;
        if (el.children.length > 0) return;           // 리프 노드만
        if (el.closest(NOTE_SELECTOR)) return;        // 각주 예외
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (fs < floor) {
          errs.push(
            `slide ${n}: 폰트 ${fs}px < ${tier} 하한 ${floor}px ` +
            `— 폰트를 줄여 넘침을 해결하지 마라 (density-rules.md §5 STEP 5)`
          );
        }
      });

      // ─── ④ Action Title 검사 ─────────────────────────────────
      const title = s.querySelector('.title, h1, h2');
      if (title) {
        const t = title.textContent.trim();
        if (t.length > 45) {
          errs.push(`slide ${n}: 제목 ${t.length}자 > 40자 권장 (density-rules.md §8)`);
        }
        const lh = parseFloat(getComputedStyle(title).lineHeight);
        const h = title.getBoundingClientRect().height;
        if (lh && h / lh > 2.3) {
          errs.push(`slide ${n}: 제목이 3줄 이상 — 2줄 초과는 하드 실패 (§8)`);
        }
      }

      // ─── ⑤ 차트 정크 ────────────────────────────────────────
      s.querySelectorAll('svg, .chart, .bar').forEach(el => {
        const cs = getComputedStyle(el);
        if (cs.boxShadow !== 'none') errs.push(`slide ${n}: 차트에 그림자 (차트 정크 금지)`);
        if (cs.backgroundImage.includes('gradient'))
          errs.push(`slide ${n}: 차트에 그라디언트 (차트 정크 금지)`);
      });
    });

    return { errs, slideCount: slides.length };
  }, FLOOR, SAFE, NOTE_SELECTOR);

  await browser.close();
  return errors;
}

/* ===== CLI ===== */
if (require.main === module) {
  const target = process.argv[2];
  if (!target) {
    console.error('사용법: node slide_lint.js <deck.html>');
    process.exit(2);
  }
  lint(target).then(({ errs, slideCount }) => {
    if (errs.length) {
      console.error(`\n❌ slide-lint 실패 — ${slideCount}장 중 ${errs.length}건\n`);
      errs.forEach(e => console.error('  ' + e));
      console.error('\n넘침은 빌드 실패다. 폰트를 줄여 덮지 말고 구조로 해결할 것.');
      console.error('대응 순서: 삭제 → 분할 → 부록 → 열/등급 → 폰트(1단계) → 실패\n');
      process.exit(1);
    }
    console.log(`✅ slide-lint 통과 — ${slideCount}장, 위반 0건`);
  }).catch(e => {
    console.error('slide-lint 실행 오류:', e.message);
    process.exit(2);
  });
}

module.exports = { lint, FLOOR, SAFE };
