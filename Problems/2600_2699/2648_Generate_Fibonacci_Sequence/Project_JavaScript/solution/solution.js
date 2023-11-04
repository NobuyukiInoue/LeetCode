/**
 * @return {Generator<number>}
 */

// 50ms
var fibGenerator = function*() {
  let current = 0;
  let next = 1;

  while (true) {
    yield current;
    [current, next] = [next, current + next];
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

window.addEventListener('load', () => {
  const f = document.getElementById('selct_file_button');
  f.addEventListener('change', evt => {
    let input = evt.target;
    if (input.files.length == 0) {
      console.log('No file selected');
      return;
    }
    const file = input.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      const result_contents = document.getElementById('result_contents');
      result_contents.innerHTML = '';

      let lines = reader.result.trim().split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        const flds = line.replace('[', '').replace(']', '');

        var callCount = parseInt(flds, 10);

        result_contents.innerHTML += 'callCount = ' + callCount + '<BR>';

        const t_start = performance.now();

        var result = 0;
        const gen = fibGenerator();
        for (let i = 0; i <= callCount; i++) {
          result = gen.next().value;
        }

        const t_end = performance.now();

        result_contents.innerHTML += 'result = [' + result + ']<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
