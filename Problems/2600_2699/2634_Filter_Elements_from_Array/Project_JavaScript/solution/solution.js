/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

// 46ms
var filter = function(arr, fn) {
  var filteredArr = [];
  for (var i = 0; i < arr.length; i++) {
      if (fn(arr[i], i)) {
          filteredArr.push(arr[i]);
      }
  }
  return filteredArr;
};
 
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

        const flds = line.replace('[[', '').replace(']]', '').replace(/"/g, '').split('],[');

        var arr = [];
        flds[0].split(',').forEach(temp => {
          arr.push(parseInt(temp, 10));
        });

        var fn = flds[1];

        result_contents.innerHTML += 'arr = ' + arr + ', functions = ' + fn + '<BR>';

        const t_start = performance.now();

        fn = fn.replace(/.*{/, '').replace(' return ', '').replace(' }', '');

        result_contents.innerHTML += 'fn = "' + fn + '"<BR>';

        var result;
        if (fn.indexOf("i ") === 0) {
          result = filter(arr, (n, i) => eval(fn));
        } else {
          result = filter(arr, n => eval(fn));
        }

        const t_end = performance.now();

        result_contents.innerHTML += 'result = [' + result + ']<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
