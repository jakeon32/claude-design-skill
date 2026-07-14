/**
 * 한글 폰트 웨이트 실측 — "한글은 영어보다 웨이트를 덜 써야 한다"를 수치로.
 *
 * 한글은 자음+모음 조합이라 획이 많고, 글자 안에 닫힌 속공간(카운터)이 많다.
 * 웨이트를 올리면 획이 두꺼워지면서 속공간이 먼저 막힌다 → 글자가 뭉개진다.
 * 영문은 획이 적고 카운터가 커서 900까지 견딘다.
 *
 * 측정:
 *   ① 잉크 밀도      — 웨이트를 올릴 때 얼마나 빨리 차오르나
 *   ② 카운터 생존율  — 글자 안 "빈 구멍"이 몇 개나 남아 있나 (막히면 0으로 수렴)
 */
const pptr = require('puppeteer-core');

(async () => {
  const b = await pptr.launch({
    headless: 'new',
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  });
  const p = await b.newPage();
  await p.setContent('<html><body></body></html>');

  const out = await p.evaluate(() => {
    const FONT = "'Pretendard',sans-serif";
    const cv = document.createElement('canvas');

    function measure(text, px, weight) {
      const ctx = cv.getContext('2d', { willReadFrequently: true });
      ctx.font = `${weight} ${px}px ${FONT}`;
      const m = ctx.measureText(text);
      const w = Math.ceil(m.width) + 6;
      const h = Math.ceil(px * 1.5);
      cv.width = w; cv.height = h;

      const c = cv.getContext('2d', { willReadFrequently: true });
      c.clearRect(0, 0, w, h);
      c.font = `${weight} ${px}px ${FONT}`;
      c.fillStyle = '#000';
      c.textBaseline = 'middle';
      c.fillText(text, 2, h / 2);

      const d = c.getImageData(0, 0, w, h).data;
      const ink = new Uint8Array(w * h);
      let inkCount = 0, minY = h, maxY = 0;
      for (let i = 0; i < w * h; i++) {
        if (d[i * 4 + 3] > 128) {
          ink[i] = 1; inkCount++;
          const y = Math.floor(i / w);
          if (y < minY) minY = y;
          if (y > maxY) maxY = y;
        }
      }
      const boxH = Math.max(1, maxY - minY + 1);
      const density = inkCount / (w * boxH);

      // 카운터(속공간) 개수 — 잉크로 완전히 둘러싸인 빈 영역.
      // 바깥 배경에서 flood fill 한 뒤, 남은 빈 픽셀 덩어리가 카운터다.
      const outside = new Uint8Array(w * h);
      const stack = [];
      for (let x = 0; x < w; x++) { stack.push(x); stack.push((h - 1) * w + x); }
      for (let y = 0; y < h; y++) { stack.push(y * w); stack.push(y * w + w - 1); }
      while (stack.length) {
        const i = stack.pop();
        if (i < 0 || i >= w * h || outside[i] || ink[i]) continue;
        outside[i] = 1;
        const x = i % w, y = Math.floor(i / w);
        if (x > 0)     stack.push(i - 1);
        if (x < w - 1) stack.push(i + 1);
        if (y > 0)     stack.push(i - w);
        if (y < h - 1) stack.push(i + w);
      }
      // 남은 빈 픽셀 = 카운터. 덩어리 수와 총 면적을 센다.
      const visited = new Uint8Array(w * h);
      let counters = 0, counterArea = 0;
      for (let i = 0; i < w * h; i++) {
        if (ink[i] || outside[i] || visited[i]) continue;
        let size = 0;
        const st = [i];
        while (st.length) {
          const j = st.pop();
          if (j < 0 || j >= w * h || visited[j] || ink[j] || outside[j]) continue;
          visited[j] = 1; size++;
          const x = j % w, y = Math.floor(j / w);
          if (x > 0)     st.push(j - 1);
          if (x < w - 1) st.push(j + 1);
          if (y > 0)     st.push(j - w);
          if (y < h - 1) st.push(j + w);
        }
        if (size >= 3) { counters++; counterArea += size; }   // 3px 미만은 노이즈
      }

      return {
        density: +density.toFixed(3),
        counters,
        counterArea: +(counterArea / (w * boxH)).toFixed(4),
      };
    }

    const WEIGHTS = [400, 500, 600, 700, 800, 900];
    // 한글은 복잡도 편차가 크다. 상한은 "최악의 글자" 기준으로 잡아야 안전하다.
    //   단순 = 무받침·홑받침 (가·나·이·수)
    //   보통 = 일반 받침    (격·은·코·드)
    //   복잡 = 겹받침·복모음 (뚫·짧·옳·쫓·웠·훑·흙)
    const CASES = [
      { label: '한글 단순 44', text: '이 수가 나아', px: 44 },
      { label: '한글 보통 44', text: '규격은 코드에', px: 44 },
      { label: '한글 복잡 44', text: '뚫렸던 확률', px: 44 },
      { label: '한글 극단 44', text: '훑짧옳쫓뚫', px: 44 },
      { label: '한글 단순 19', text: '이 수가 나아', px: 19 },
      { label: '한글 보통 19', text: '규모가 아닌 기술력', px: 19 },
      { label: '한글 복잡 19', text: '뚫렸던 확률과 넓혔다', px: 19 },
      { label: '한글 극단 19', text: '훑짧옳쫓뚫', px: 19 },
      { label: '영문 44px',   text: 'BRAND VISION', px: 44 },
      { label: '영문 19px',   text: 'Verified Capability', px: 19 },
    ];

    return CASES.map(c => ({
      label: c.label,
      px: c.px,
      rows: WEIGHTS.map(w => ({ w, ...measure(c.text, c.px, w) })),
    }));
  });

  console.log('\n한글 vs 영문 — 웨이트별 잉크 밀도 / 카운터(속공간) 생존');
  console.log('='.repeat(72));
  for (const c of out) {
    console.log(`\n■ ${c.label}`);
    console.log('   weight   잉크밀도   카운터수   카운터면적');
    const base = c.rows[0];
    for (const r of c.rows) {
      const dGain = ((r.density / base.density - 1) * 100).toFixed(0);
      const cLoss = base.counters ? ((1 - r.counters / base.counters) * 100).toFixed(0) : '0';
      console.log(
        `   ${String(r.w).padStart(4)}    ${r.density.toFixed(3)}  (+${dGain.padStart(3)}%)` +
        `   ${String(r.counters).padStart(3)} (−${cLoss.padStart(3)}%)` +
        `   ${r.counterArea.toFixed(4)}`
      );
    }
  }
  console.log('\n' + '='.repeat(72));
  console.log('카운터 = 글자 안의 닫힌 빈 공간. 이게 막히면 글자가 "뭉친다".');

  await b.close();
})();
