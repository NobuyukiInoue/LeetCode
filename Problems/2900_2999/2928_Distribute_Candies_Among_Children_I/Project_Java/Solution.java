import java.util.*;

public class Solution {
    public int distributeCandies(int n, int limit) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < Math.min(n, limit) + 1; i++) {
            ans += helper(n - i, limit);
        }
        return ans;
    }

    private int helper(int n, int limit) {
        int min_v = Math.max(0, n - limit);
        int max_v = Math.min(n, limit);
        return Math.max(0, max_v - min_v + 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int limit = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", limit = " + limit);
 
        long start = System.currentTimeMillis();

        int result = distributeCandies(n, limit);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
