/**
 * hangul_complexity.js — 한글 텍스트의 복잡도를 세어 폰트 웨이트 상한을 산출한다.
 *
 * ─ 왜 필요한가 ────────────────────────────────────────────────
 * "한글은 영문보다 웨이트를 덜 써야 한다"는 맞지만, **한글 안에서도 편차가 크다.**
 * Pretendard 실측(tools/weight_measure.js):
 *
 *   19px, 카운터(속공간) 생존율
 *     영문                     400: 7개 → 900: 7개  (손실 0%)
 *     한글 단순 "이 수가 나아"  400: 2개 → 900: 2개  (손실 0%)
 *     한글 복잡 "뚫렸던 확률"   400: 6개 → 700: 4개(−33%) → 900: 1개(−83%)
 *
 * 즉 **겹받침·복모음이 많은 글자에서만 막힌다.** 그러므로 웨이트 상한은
 * 텍스트의 복잡도에 따라 달라져야 한다. 이 도구가 그걸 계산한다.
 * ─────────────────────────────────────────────────────────────
 */

/** 한글 음절을 초성/중성/종성으로 분해 */
function decompose(ch) {
  const code = ch.charCodeAt(0) - 0xac00;
  if (code < 0 || code > 11171) return null;          // 한글 음절 아님
  return {
    cho: Math.floor(code / 588),
    jung: Math.floor((code % 588) / 28),
    jong: code % 28,                                   // 0 = 받침 없음
  };
}

/** 겹받침 (두 자음) — 획이 가장 많이 몰린다 */
const DOUBLE_JONG = new Set([3, 5, 6, 9, 10, 11, 12, 13, 14, 15, 18, 20]);
//  ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ ...

/** 복모음 (두 모음 결합) — 중성이 넓게 퍼져 공간을 먹는다 */
const COMPLEX_JUNG = new Set([9, 10, 11, 14, 15, 16, 19, 20]);
//  ㅘ ㅙ ㅚ ㅝ ㅞ ㅟ ㅢ ...

/** 획이 많은 초성 (ㄲ ㄸ ㅃ ㅆ ㅉ ㅎ) */
const HEAVY_CHO = new Set([1, 4, 8, 10, 13, 18]);

/**
 * 텍스트 복잡도 (0~1). 높을수록 획이 많고 속공간이 좁다.
 * @returns {{ complexity:number, syllables:number, detail:object }}
 */
function complexity(text) {
  let n = 0, score = 0;
  const detail = { doubleJong: 0, complexJung: 0, heavyCho: 0, hasJong: 0 };

  for (const ch of text) {
    const d = decompose(ch);
    if (!d) continue;
    n++;
    let s = 0;
    if (d.jong > 0) { s += 0.30; detail.hasJong++; }             // 받침 있음
    if (DOUBLE_JONG.has(d.jong)) { s += 0.45; detail.doubleJong++; }   // 겹받침 (가중)
    if (COMPLEX_JUNG.has(d.jung)) { s += 0.25; detail.complexJung++; } // 복모음
    if (HEAVY_CHO.has(d.cho)) { s += 0.15; detail.heavyCho++; }        // 된소리·ㅎ
    score += Math.min(1, s);
  }
  if (!n) return { complexity: 0, syllables: 0, detail };
  return { complexity: +(score / n).toFixed(3), syllables: n, detail };
}

/**
 * 복잡도 + 크기 → 안전한 폰트 웨이트 상한.
 * 실측 기준: 복잡 글자 19px 는 700 에서 카운터 33% 손실, 800 에서 50% 손실.
 */
function maxWeight(text, px) {
  const { complexity: c, syllables } = complexity(text);
  if (!syllables) return 900;                          // 한글 아님 → 영문 기준

  // 기본 상한 (크기별) — 작을수록 낮다
  let base;
  if (px >= 40)      base = 700;
  else if (px >= 24) base = 700;
  else if (px >= 19) base = 600;
  else               base = 500;

  // 복잡도 보정 — 겹받침·복모음이 많으면 한 단계 낮춘다
  if (c >= 0.55)      base -= 100;                     // 매우 복잡
  else if (c >= 0.40) base -= 100;                     // 복잡
  // c < 0.40 은 보정 없음

  return Math.max(400, base);
}

/** 검사 — 위반이면 메시지 반환, 통과면 null */
function check(text, px, weight) {
  const max = maxWeight(text, px);
  const { complexity: c } = complexity(text);
  if (weight > max) {
    return `한글 ${px}px, 복잡도 ${c} → 웨이트 상한 ${max} (현재 ${weight}). ` +
           `겹받침·복모음이 많아 속공간이 막힌다.`;
  }
  return null;
}

/* ===== CLI ===== */
if (require.main === module) {
  const SAMPLES = [
    ['이 수가 나아', 44],
    ['규격은 코드에 둔다', 44],
    ['뚫렸던 확률과 넓혔다', 44],
    ['훑짧옳쫓뚫', 44],
    ['규모가 아닌 기술력으로', 19],
    ['뚫렸던 확률과 넓혔다', 19],
    ['검증된 역량', 24],
  ];
  console.log('\n한글 복잡도 → 웨이트 상한');
  console.log('='.repeat(70));
  console.log('텍스트'.padEnd(26) + 'px'.padStart(4) + '  복잡도  상한   구성');
  console.log('-'.repeat(70));
  for (const [t, px] of SAMPLES) {
    const { complexity: c, detail } = complexity(t);
    const mw = maxWeight(t, px);
    const parts = [];
    if (detail.doubleJong)  parts.push(`겹받침${detail.doubleJong}`);
    if (detail.complexJung) parts.push(`복모음${detail.complexJung}`);
    if (detail.heavyCho)    parts.push(`된소리${detail.heavyCho}`);
    console.log(
      t.padEnd(24) + String(px).padStart(4) + '  ' +
      c.toFixed(3).padStart(6) + '   ' + String(mw).padStart(3) + '   ' +
      (parts.join(' · ') || '—')
    );
  }
  console.log('='.repeat(70));
}

module.exports = { complexity, maxWeight, check, decompose };
