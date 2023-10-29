/**
 * @param {Function[]} functions
 * @return {Function}
 */

// 60ms - 71ms
var compose = function (functions = []) {
  return function (x) {
      if (!functions.length) { return x }
      for (let index = functions.length - 1; index >= 0; index--) {
          x = functions[index](x)
      }
      return x
  }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
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

      let lines = reader.result.split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        const flds = line.replace('[[', '').replace(']]', '').replace(/"/g, '').split('],[');

        var functions = eval('[' + flds[0] + ']');
        var x = parseInt(flds[1], 10);
        result_contents.innerHTML += 'functions = [' + functions + '], x = ' + x + '<BR>';

        const t_start = performance.now();

        var fn = compose(functions);
        var result = fn(x);

        const t_end = performance.now();

        result_contents.innerHTML += 'result = ' + result + '<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
