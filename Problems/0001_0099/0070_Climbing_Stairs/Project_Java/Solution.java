import java.util.*;

public class Solution {
    public int climbStairs(int n) {
        // 0ms
        int[] results = new int[n + 1];
        results[0] = 0;
        if (n > 0)
            results[1] = 1;
        if (n > 1)
            results[2] = 2;
        for (int i = 3; i <= n; ++i) {
            results[i] = results[i - 1] + results[i - 2];
        }
        return results[n];
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int result = climbStairs(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
