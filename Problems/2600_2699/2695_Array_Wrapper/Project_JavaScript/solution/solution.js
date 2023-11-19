/**
 * @param {number[]} nums
 * @return {void}
 */

// 43ms
var ArrayWrapper = function(nums) {
  this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
  return this.nums.reduce((sum, num) => sum + num, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
  return `[${this.nums.join(',')}]`;
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */
 
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

        let flds = line.replace('[[[', '').replaceAll('"', '').replace(/, /g, ',').split(']],[');

        let operation = flds[1].replace(']]', '');
        var nums;

        switch (operation) {
          case 'Add':
            nums = [];
            flds[0].split('],[').forEach(fld => {
              var row = [];
              var temp_arr = fld.split(',');
              temp_arr.forEach(temp => {
                row.push(parseInt(temp, 10));
              })
              nums.push(row);
            });
            result_contents.innerHTML += 'nums = ' + arrToString(nums) + ', operation = ' + operation + '<BR>';
            break;
          case 'String':
            nums = [];
            flds[0].split('],[').forEach(fld => {
              var row = [];
              var temp_arr = fld.split(',');
              temp_arr.forEach(temp => {
                row.push(temp);
              })
              nums.push(row);
            });
            result_contents.innerHTML += 'nums = ' + nums + ', operation = ' + operation + '<BR>';
            break;
        };

        const t_start = performance.now();

        var result;
        switch (operation) {
          case 'Add':
            result = 0;
            nums.forEach(arr => {
              const obj = new ArrayWrapper(arr);
              result += obj;
            });
            break;
          case 'String':
            result = [];
            nums.forEach(arr => {
              const obj = new ArrayWrapper(arr);
              result.push(obj);
            });
            break;
        }

        const t_end = performance.now();

        if (Array.isArray(result)) {
          // result_contents.innerHTML += 'result = ' + arrToString(result) + '<BR>';
          result_contents.innerHTML += 'result = ' + result + '<BR>';
        } else {
          result_contents.innerHTML += 'result = ' + result + '<BR>';
        }
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
