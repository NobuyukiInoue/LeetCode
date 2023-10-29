/**
 * @param {number} n
 * @return {Function} counter
 */

// 39ms
var createCounter = function(n) {
  let count = n, i = -1
  return () => count + ++i;
};

/** 
* const counter = createCounter(10)
* counter() // 10
* counter() // 11
* counter() // 12
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
      let lines = reader.result.split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        let flds = line.replace('[[', '').replace(']]', '').replace(/, /g, ',').split('],[');
        let n = parseInt(flds[0], 10);
        let cmds = flds[1].replace(/\"/g, '').split(',');

        result_contents.innerHTML += 'n = ' + n + ', cmds = [' + cmds + ']<BR>';

        const t_start = performance.now();

        const counter = createCounter(n);

        let result = [];
        cmds.forEach(cmd => {
          if (cmd === "call") {
            result.push(counter());
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
