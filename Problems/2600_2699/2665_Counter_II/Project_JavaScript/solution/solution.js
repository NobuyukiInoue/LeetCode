/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

// 46ms
var createCounter = function(init) {
  let presentCount = init;

  function increment() {
    return ++presentCount;
  }

  function decrement() {
      return --presentCount;
  }

  function reset() {
      return (presentCount = init);
  }

  return { increment, decrement, reset };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
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
      let lines = reader.result.trim().split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        let flds = line.replace('[[', '').replace(']]', '').replace(/, /g, ',').split('],[');
        let init = parseInt(flds[0], 10);
        let calls = flds[1].replace(/\"/g, '').split(',');

        result_contents.innerHTML += 'init = ' + init + ', calls = [' + calls + ']<BR>';

        const t_start = performance.now();

        var result = [];
        const counter = createCounter(init);

        calls.forEach(cmd => {
          switch (cmd) {
            case 'increment':
              result.push(counter.increment());
              break;
            case 'decrement':
              result.push(counter.decrement());
              break;
            case 'reset':
              result.push(counter.reset());
              break;
          }
        });

        const t_end = performance.now();

        result_contents.innerHTML += 'result = [' + result + ']<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
