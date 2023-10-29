/**
 * @return {null|boolean|number|string|Array|Object}
 */

// 46ms
Array.prototype.last = function() {
    if (this.length === 0) {
        return -1;
      } else {
        return this[this.length - 1];
      }
  };
  
  /**
  * const arr = [1, 2, 3];
  * arr.last(); // 3
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
  
          const flds = line.replace('[', '').replace(']', '').replace(/, /g, ',').split(',');
          result_contents.innerHTML += 'flds = [' + flds + ']<BR>';

          const t_start = performance.now();

          result_contents.innerHTML += 'result = ' + flds.last() + '<BR>';

          const t_end = performance.now();

          result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
        });
      };
  
      reader.readAsText(file);
    });
  });
  
