import java.util.*;

public class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        // 4ms
        int ans = 0, prev = values[0];
        for (int i = 1; i < values.length; i++) {
            ans = Math.max(ans, values[i] - i + prev);
            prev = Math.max(prev, values[i] + i);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] values = ml.stringToIntArray(flds);
        System.out.println("values = " + ml.intArrayToString(values));

        long start = System.currentTimeMillis();

        int result = maxScoreSightseeingPair(values);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
