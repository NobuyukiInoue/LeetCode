/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
  // 53ms - 55ms
  var res = [];
  for (var i = 0; i < arr.length; i += size) {
    res.push(arr.slice(i, i + size));
  }
  return res;
};

function arrToString(flds) {
  var resultStr = '';
  flds.forEach(fld => {
    if (resultStr === '') {
      resultStr += getIsArrayToString(fld);
    } else {
      resultStr += ', ' + getIsArrayToString(fld);
    }
  });
  return '[' + resultStr + ']';
}

function getIsArrayToString(fld) {
  if (Array.isArray(fld)) {
    return arrToString(fld);
  }
  return fld;
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
      let lines = reader.result.trim().split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        let flds = line.replace('[[', '').replace(']]', '').replace(/, /g, ',').split('],[');

        var arr = [];
        flds[0].split(',').forEach(fld => {
          arr.push(parseInt(fld, 10));
        });

        let size = parseInt(flds[1], 10);

        result_contents.innerHTML += 'arr = ' + arrToString(arr) + ', size = ' + size + '<BR>';

        const t_start = performance.now();

        var result = chunk(arr, size);

        const t_end = performance.now();

        result_contents.innerHTML += 'result = ' + arrToString(result) + '<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
