import java.util.*;

public class Solution {
    public int maxTurbulenceSize(int[] arr) {
        // 6ms - 7ms
        int ans = 0, clen = 0;
        for (int i = 0; i < arr.length; i++) {
            if (i >= 2 && ((arr[i-2] > arr[i-1] && arr[i-1] < arr[i]) ||
                          (arr[i-2] < arr[i-1] && arr[i-1] > arr[i]))) {
                clen++;
            } else if(i >= 1 && arr[i-1] != arr[i]) {
                clen = 2;
            } else {
                clen = 1;
            }
            ans = Math.max(ans, clen);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = maxTurbulenceSize(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
