/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */

// 50ms
var argumentsLength = function(...args) {
	return args.length;
};

/**
 * argumentsLength(1, 2, 3); // 3
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

        let lines = reader.result.trim().split('\n');
        lines.forEach(line => {
          result_contents.innerHTML += 'args = ' + line + '<BR>';
  
//        const args = line.replace('[', '').replace(']', '').replace('"', '').replace(/, /g, ',').split(',');
          const args = line;
//        result_contents.innerHTML += 'n_args = ' + args + '<BR>';

          const t_start = performance.now();

          var result = argumentsLength(eval(args));
          result_contents.innerHTML += 'result = ' + result + '<BR>';

          const t_end = performance.now();

          result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
        });
      };
  
      reader.readAsText(file);
    });
  });
  
