/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */

// 41ms
var reduce = function(nums, fn, init) {
  let val = init;
  for (let i = 0; i < nums.length; i++) {
    val = fn(val, nums[i]);
  }
  return val;
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

      let lines = reader.result.split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        const flds = line.replace('[[', '').replace(']]', '').replace(/, /g, ',').replace(/"/g, '').split('],[');

        var nums = [];
        flds[0].split(',').forEach(temp => {
          nums.push(parseInt(temp, 10));
        });

        let fn = flds[1];
        let init = parseInt(flds[2], 10);
        result_contents.innerHTML += 'nums = [' + nums + '], fn = ' + fn + ', init = ' + init + '<BR>';

        fn = fn.replace(/.*{/, '').replace(' return ', '').replace('; }', '');

        const t_start = performance.now();

        var result;

        if (fn === '0') {
          result = reduce(nums, (accum, _val) => accum + eval(fn), init);
        } else {
          result = reduce(nums, (accum, curr) => eval(fn), init);
        }

        result_contents.innerHTML += 'result = ' + result + '<BR>';

        const t_end = performance.now();

        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
