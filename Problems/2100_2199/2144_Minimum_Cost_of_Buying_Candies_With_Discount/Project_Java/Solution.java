import java.util.*;

public class Solution {
    public int minimumCost(int[] cost) {
        // 1ms
        Arrays.sort(cost);
        int res = 0;
        for (int i = 0; i < cost.length; i++) {
            if (i % 3 != cost.length % 3) {
                res += cost[i];
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] cost = ml.stringToIntArray(flds);
        System.out.println("cost = " + ml.intArrayToString(cost));

        long start = System.currentTimeMillis();

        int result = minimumCost(cost);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
