/**
 * @param {Function} fn
 * @return {Function}
 */

// 57ms - 61ms
var once = function(fn) {
  let hasBeenCalled = false;
  let result;

  return function(...args) {
    if (!hasBeenCalled) {
      result = fn(...args);
      hasBeenCalled = true;
      return result;
    } else {
      return undefined;
    }
  }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */


function arrToString(flds) {
  var resultStr = '';
  flds.forEach(fld => {
    if (resultStr === '') {
      resultStr += fld;
    } else {
      resultStr += ', ' + fld;
    }
  });
  return '[' + resultStr + ']';
}

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

        const flds = line.replace('[[', '').replace(']]', '').replace(/"/g, '').split('],[[');

        var fn_str = flds[0];

        var calls = [];
        flds[1].split('],[').forEach(row => {
          var data = []
          row.split(',').forEach(col => {
            data.push(parseInt(col, 10));
          });
          calls.push(data);
        });

        result_contents.innerHTML += 'fn = ' + fn_str + ', calls = [';
        var workStr = '';
        calls.forEach(call => {
          if (workStr === '') {
            workStr += '[' + call + ']';
          } else {
            workStr += ',[' + call + ']';
          }
        });
        result_contents.innerHTML +=  workStr + ']<BR>';

        const t_start = performance.now();

        var result;

        let fn = eval(fn_str);
        let onceFn = once(fn);

        var resultArr = [];

        calls.forEach(call => {
          resultArr.push(onceFn(call[0], call[1], call[2]));
        });

        const t_end = performance.now();

        result_contents.innerHTML += 'result = ' +  arrToString(resultArr) + '<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
