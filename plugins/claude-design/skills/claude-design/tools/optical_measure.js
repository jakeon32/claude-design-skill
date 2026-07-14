/**
 * 광학 정렬 실측 v2 — 실제 잉크의 시작점을 픽셀로 찾는다.
 *
 * v1의 measureText().actualBoundingBoxLeft 는 한글에서 대부분 0이 나왔다.
 * 한글은 네모틀에 꽉 차는 글자라 "사이드 베어링"이 거의 없기 때문이다.
 * → 그러면 Jake가 말한 "치우쳐 보임"의 원인은 베어링이 아니라 **잉크 밀도**다.
 *
 * 그래서 두 가지를 픽셀로 직접 잰다:
 *   ① 광학 좌단  = 첫 번째 잉크 픽셀의 x좌표 (기하학적 좌단 0과의 차이)
 *   ② 잉크 밀도  = 바운딩박스 대비 칠해진 픽셀 비율 (솔리드 = 1.0)
 *   ③ 좌측 여백 무게 = 좌측 20% 구간의 잉크 밀도 (여기가 낮으면 안으로 들어가 보인다)
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
    const FONT = '"Malgun Gothic","Pretendard",sans-serif';   // 실제 렌더 폰트
    const cv = document.createElement('canvas');

    function measure(text, px, weight) {
      const ctx = cv.getContext('2d', { willReadFrequently: true });
      ctx.font = `${weight} ${px}px ${FONT}`;
      const m = ctx.measureText(text);
      const w = Math.ceil(m.width) + 8;
      const h = Math.ceil(px * 1.6);
      cv.width = w; cv.height = h;

      const c = cv.getContext('2d', { willReadFrequently: true });
      c.clearRect(0, 0, w, h);
      c.font = `${weight} ${px}px ${FONT}`;
      c.fillStyle = '#000';
      c.textBaseline = 'middle';
      c.fillText(text, 0, h / 2);                 // x=0 = 기하학적 좌단

      const d = c.getImageData(0, 0, w, h).data;

      // ① 첫 잉크 픽셀의 x — 이것이 "광학 좌단"
      let firstInkX = -1;
      outer:
      for (let x = 0; x < w; x++) {
        for (let y = 0; y < h; y++) {
          if (d[(y * w + x) * 4 + 3] > 20) { firstInkX = x; break outer; }
        }
      }

      // ② 전체 잉크 밀도 (실제 글자가 차지하는 세로 범위 기준)
      let minY = h, maxY = 0, ink = 0;
      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          if (d[(y * w + x) * 4 + 3] > 20) {
            ink++;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;
          }
        }
      }
      const boxH = Math.max(1, maxY - minY + 1);
      const density = ink / (w * boxH);

      // ③ 좌측 첫 글자 폭 구간의 잉크 밀도 — 왼쪽이 얼마나 "비어" 있나
      const edgeW = Math.min(Math.ceil(px), w);
      let edgeInk = 0;
      for (let y = minY; y <= maxY; y++) {
        for (let x = 0; x < edgeW; x++) {
          if (d[(y * w + x) * 4 + 3] > 20) edgeInk++;
        }
      }
      const edgeDensity = edgeInk / (edgeW * boxH);

      return {
        firstInkX,
        firstInkEm: +(firstInkX / px).toFixed(4),
        density: +density.toFixed(4),
        edgeDensity: +edgeDensity.toFixed(4),
      };
    }

    const SAMPLES = [
      { label: '대형 타이틀(한)', text: '규격은 문서가 아니라', px: 48, weight: 800 },
      { label: '소제목(한)',     text: '검증된 역량',          px: 34, weight: 700 },
      { label: '본문(한)',       text: '국가급 정상회의 공식',  px: 28, weight: 400 },
      { label: '작은본문(한)',   text: '규모가 아닌 기술력',    px: 19, weight: 400 },
      { label: '라벨(영,대문자)', text: 'KEY FACTS',           px: 14, weight: 700 },
      { label: '대형타이틀(영)',  text: 'BRAND VISION',        px: 48, weight: 800 },
      { label: '따옴표 시작',     text: '“밀도는 죄가',    px: 40, weight: 700 },
      { label: '숫자',           text: '886',                 px: 32, weight: 800 },
    ];

    return SAMPLES.map(s => ({ ...s, ...measure(s.text, s.px, s.weight) }));
  });

  console.log('');
  console.log('광학 정렬 실측 v2 — 잉크 픽셀 직접 측정');
  console.log('='.repeat(78));
  console.log('개체              크기   광학좌단    보정(em)   잉크밀도  좌측밀도');
  console.log('-'.repeat(78));
  console.log('솔리드 도형/사진    —     0.0px      0          1.0000   1.0000');
  for (const r of out) {
    console.log(
      r.label.padEnd(17) +
      (r.px + 'px').padStart(5) + '  ' +
      (r.firstInkX + '.0px').padStart(8) + '  ' +
      ('-' + r.firstInkEm).padStart(9) + '  ' +
      r.density.toFixed(4).padStart(8) + ' ' +
      r.edgeDensity.toFixed(4).padStart(8)
    );
  }
  console.log('='.repeat(78));
  console.log('');
  console.log('해석:');
  console.log('  · 광학좌단 = 잉크가 실제로 시작되는 x. 이만큼 왼쪽으로 빼야 도형과 시각적으로 맞는다.');
  console.log('  · 잉크밀도 = 솔리드(1.0) 대비 시각 무게. 낮을수록 "가벼워" 안으로 들어가 보인다.');
  console.log('  · 좌측밀도 = 첫 글자 구간의 밀도. 낮으면 왼쪽이 비어 보여 추가 보정이 필요하다.');

  await b.close();
})();
