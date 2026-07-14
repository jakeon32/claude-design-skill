/**
 * chart-scale.js — 슬라이드 차트 공통 스케일 유틸 (1280×720)
 *
 * ─ 왜 이 파일이 있는가 ─────────────────────────────────────────────
 * 2026-07-14 이전, data-layouts.md의 막대 템플릿에는 이렇게 적혀 있었다:
 *
 *     height: 240px;  /* 값에 따라 조정 * /
 *
 * 값→픽셀 환산 규칙이 없으니 AI가 **눈대중으로 막대 길이를 그렸다.**
 * 데이터와 그림이 안 맞을 수 있었다.
 *
 * 해법은 템플릿에서 픽셀을 없애고, 차트를 그리기 전에 **반드시 스케일 객체를
 * 계산하도록 강제**하는 것이다. 픽셀을 직접 쓰는 경로를 문법적으로 막는다.
 *
 * 사용 순서 (이 순서를 지킬 것):
 *   1. const s = niceScale(0, Math.max(...values));   // 축 확정
 *   2. const px = valueToPx(v, s, PLOT_W);            // 길이 환산
 *   3. assertChart(...)                                // 렌더 전 검증
 *
 * 알고리즘: Heckbert, "Nice Numbers for Graph Labels", Graphics Gems I (1990)
 * ──────────────────────────────────────────────────────────────────
 */

/* ===== 슬라이드 좌표 상수 (1280×720 고정) ===== */
const SLIDE_W = 1280, SLIDE_H = 720;
const PLOT_LEFT = 140, PLOT_TOP = 180;   // 좌: y축 라벨 공간 / 상: 제목 공간
const PLOT_W = 1000, PLOT_H = 400;       // 하단 140px = x축 라벨 + 각주
const PLOT_RIGHT = PLOT_LEFT + PLOT_W;   // 1140
const PLOT_BOTTOM = PLOT_TOP + PLOT_H;   // 580

/* ===== 1. Nice Numbers ===== */

function niceNum(x, round) {
  if (x === 0) return 0;
  const exp = Math.floor(Math.log10(x));
  const f = x / Math.pow(10, exp);                                 // 1 <= f < 10
  let nf;
  if (round) nf = f < 1.5 ? 1 : f < 3 ? 2 : f < 7 ? 5 : 10;        // 가까운 nice 수
  else       nf = f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10;       // 이상인 nice 수
  return nf * Math.pow(10, exp);
}

/**
 * 축 스케일 확정. 데이터 최댓값이 아니라 "예쁜 수"로 올림한 축 최댓값을 만든다.
 *   niceScale(0, 86)  → { min: 0, max: 100, step: 20, ticks: [0,20,40,60,80,100] }
 *
 * @param {number} dataMin
 * @param {number} dataMax
 * @param {number} maxTicks  눈금 개수 목표 (기본 5 → 눈금 4~6개)
 * @param {boolean} zeroBase 막대류는 반드시 true (0 베이스라인 강제)
 */
function niceScale(dataMin, dataMax, maxTicks = 5, zeroBase = true) {
  let lo = Math.min(dataMin, dataMax);
  let hi = Math.max(dataMin, dataMax);
  if (zeroBase) { if (lo > 0) lo = 0; if (hi < 0) hi = 0; }
  if (lo === hi) hi = lo + 1;                                      // 전부 동일값 방어
  const range = niceNum(hi - lo, false);
  const step = niceNum(range / (maxTicks - 1), true);
  const min = Math.floor(lo / step) * step;
  const max = Math.ceil(hi / step) * step;
  const decimals = Math.max(-Math.floor(Math.log10(step)), 0);
  const ticks = [];
  for (let v = min; v <= max + step * 0.5; v += step) {
    ticks.push(+v.toFixed(decimals + 2));                          // 부동소수 오차 제거
  }
  return { min, max, step, decimals, ticks };
}

/* ===== 2. 값 → 픽셀 =====
 * 🔴 정규화 기준은 "데이터 최댓값"이 아니라 "축 최댓값(scale.max)"이다.
 *    v / dataMax * H 로 하면 최대 막대가 항상 천장에 닿아 축 눈금과 어긋난다.
 */

/** 값 → 길이(px). 막대 길이·라인 높이 모두 이걸로만 구한다. */
const valueToPx = (v, s, plotPx) => (v - s.min) / (s.max - s.min) * plotPx;

/** 값 → SVG y좌표 (y축 뒤집기 포함).
 *  🔴 <g transform="scale(1,-1)">로 뒤집지 마라 — 텍스트까지 뒤집힌다. 좌표로만 뒤집는다. */
const valueToY = (v, s, plotTop, plotH) =>
  plotTop + plotH * (s.max - v) / (s.max - s.min);

/** 값 → 폭 비율(%). HTML/CSS 가로 막대용 — 컨테이너 크기와 무관하게 정확하다. */
const valueToPct = (v, s) => (v - s.min) / (s.max - s.min) * 100;

/* ===== 3. 숫자 포맷 ===== */

const fmt = (v, s) =>
  Math.abs(v) >= 1e9 ? (v / 1e9).toFixed(1) + 'B' :
  Math.abs(v) >= 1e6 ? (v / 1e6).toFixed(1) + 'M' :
  Math.abs(v) >= 1e4 ? (v / 1e3).toFixed(0) + 'K' :
  v.toFixed(s ? s.decimals : 0).replace(/\B(?=(\d{3})+(?!\d))/g, ',');

/* ===== 4. 막대 두께 / 간격 =====
 * 간격은 막대 폭보다 좁아야 한다. 권장 비율 0.3 (범위 0.2~0.4).
 */
function barGeometry(plotW, n, gapRatio = 0.3) {
  const slot = plotW / n;
  const barW = Math.round(slot / (1 + gapRatio));
  return { slot, barW, gap: slot - barW };
}

/* ===== 5. 렌더 전 자가 검증 =====
 * 눈대중 렌더를 여기서 잡는다. 값 비율과 픽셀 비율이 어긋나면 실패.
 */
function assertChart(data, s, rendered) {
  const errs = [];

  if (!s || typeof s.max !== 'number') {
    errs.push('niceScale() 없이 렌더 금지 — 픽셀을 직접 쓰지 마라');
    return errs;
  }
  // 막대류는 0 베이스라인
  if (!(s.min <= 0 && s.max >= 0)) {
    errs.push(`막대 축은 0을 포함해야 함 (min=${s.min}, max=${s.max})`);
  }
  // ★ 핵심: 값 비율 = 픽셀 비율
  if (data.length >= 2 && rendered && rendered.length >= 2) {
    const [a, b] = data;
    if (b.value !== 0) {
      const vRatio = a.value / b.value;
      const pxRatio = rendered[0].px / rendered[1].px;
      if (Math.abs(vRatio - pxRatio) > 0.02) {
        errs.push(
          `값 비율(${vRatio.toFixed(3)}) ≠ 픽셀 비율(${pxRatio.toFixed(3)}) — 눈대중 렌더 감지`
        );
      }
    }
  }
  // 데이터가 축을 넘지 않는가
  const dmax = Math.max(...data.map(d => d.value));
  if (dmax > s.max) errs.push(`데이터(${dmax})가 축 최댓값(${s.max})을 넘음`);

  return errs;
}

/* ===== 6. 색 상수 ===== */

/** 계열 색 — Okabe-Ito (색맹 대응). 이 순서대로 배정한다. */
const SERIES = [
  '#0072B2', // Blue
  '#E69F00', // Orange
  '#009E73', // Bluish Green
  '#CC79A7', // Reddish Purple
  '#56B4E9', // Sky Blue
  '#D55E00', // Vermillion
  '#F0E442', // Yellow ← 흰 배경 대비 낮음. 선·텍스트 금지, 큰 면적만 + 외곽선
  '#000000', // Black
];

/** IBCS 시나리오 — 색이 아니라 채우기 패턴으로 구분한다 */
const SCENARIO = {
  AC: { fill: '#404040' },                                   // 실적: 진한 단색
  PY: { fill: '#BFBFBF' },                                   // 전년: 연한 회색
  PL: { fill: 'none', stroke: '#404040', strokeWidth: 1.5 }, // 계획: 테두리만
  FC: { fill: 'url(#fcHatch)' },                             // 예측: 빗금
};

/** 편차 전용 색 (다른 용도 금지). 적록색맹 대응해 순수 red/green 회피 */
const VAR_GOOD = '#009E73';
const VAR_BAD  = '#D55E00';

/* ===== exports ===== */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    SLIDE_W, SLIDE_H, PLOT_LEFT, PLOT_TOP, PLOT_W, PLOT_H, PLOT_RIGHT, PLOT_BOTTOM,
    niceNum, niceScale, valueToPx, valueToY, valueToPct, fmt,
    barGeometry, assertChart, SERIES, SCENARIO, VAR_GOOD, VAR_BAD,
  };
}
