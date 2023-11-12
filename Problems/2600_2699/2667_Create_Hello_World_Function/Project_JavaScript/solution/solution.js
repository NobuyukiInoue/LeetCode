/**
 * @return {Function}
 */

// 54ms - 56ms
var createHelloWorld = function() {
  return function(...args) {
    return "Hello World";
  }
};

/**
* const f = createHelloWorld();
* f(); // "Hello World"
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

        const args = line.replace('[', '').replace(']', '').replace(/"/g, '').split('],[');
        result_contents.innerHTML += 'args = ' + arrToString(args) + '<BR>';
        const t_start = performance.now();

        var result;
        const f = createHelloWorld();
        result = f();

        const t_end = performance.now();

        result_contents.innerHTML += 'result = \"' +  result + '\"<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
