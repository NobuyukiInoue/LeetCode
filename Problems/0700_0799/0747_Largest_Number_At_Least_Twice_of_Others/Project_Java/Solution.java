import java.util.*;

public class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int [] mc = new int[cost.length + 1];
        mc[0] = cost[0];
        mc[1] = cost[1];
        
        for (int i = 2; i <= cost.length; i++) {
            int costV = (i == cost.length)? 0:cost[i];
            mc[i] = intMin(mc[i - 1] + costV, mc[i - 2] + costV);
        }

        return mc[cost.length];
    }

    public int minCostClimbingStairs2(int[] cost) {
        int a = cost[0], b = cost[1];
        int c = 0;
        for (int i = 2; i < cost.length + 1; i++) {
            if (i != cost.length) {
                c = intMin(a, b) + cost[i];
                a = b;
                b = c;
            } else {
                c = intMin(a, b);
            }
        }
        return c;
    }

    private int intMin(int a, int b) {
        if (a <= b)
            return a;
        else
            return b;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] cost = mc.str_to_int_array(flds);

        System.out.println("cost = " + mc.output_int_array(cost));

        long start = System.currentTimeMillis();
        
        int result = minCostClimbingStairs(cost);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
