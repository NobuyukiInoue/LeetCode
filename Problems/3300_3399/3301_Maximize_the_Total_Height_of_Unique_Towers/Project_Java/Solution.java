import java.util.*;

public class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        // 50ms
        Arrays.sort(maximumHeight);
        int cur = maximumHeight[maximumHeight.length - 1];
        long ans = 0;
        for (int i = maximumHeight.length - 1; i >= 0; i--) {
            cur = Math.min(cur, maximumHeight[i]);
            if (cur <= 0) {
                return -1;
            }
            ans += cur;
            cur--;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] maximumHeight = ml.stringToIntArray(flds);
        System.out.println("maximumHeight = " + ml.intArrayToString(maximumHeight));

        long start = System.currentTimeMillis();

        long result = maximumTotalSum(maximumHeight);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
