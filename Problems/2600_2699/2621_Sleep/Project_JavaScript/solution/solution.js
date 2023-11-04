/**
 * @param {number} millis
 * @return {Promise}
 */

// 52ms
async function sleep(millis) {
  await new Promise(resolve => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
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
      let lines = reader.result.trim().split('\n');
      lines.forEach(line => {
        result_contents.innerHTML += 'args = ' + line + '<BR>';

        let flds = line.replace('[', '').replace(']', '');
        let millis = parseInt(flds, 10);

        result_contents.innerHTML += 'millis = ' + millis + '<BR>';

        const t_start = performance.now();

        let t = Date.now();

        sleep(millis).then(() => console.log(Date.now() - t));

        const t_end = performance.now();

        result_contents.innerHTML += 'result = ' + (t_end - t_start)*1000 + '[ms]<BR>';
        result_contents.innerHTML += 'Execute time ... ' + (t_end - t_start).toFixed(3) + '[s]<BR><BR>';
      });
    };

    reader.readAsText(file);
  });
});
