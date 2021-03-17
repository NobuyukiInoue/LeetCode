import java.util.*;

public class Solution {
    public int countArrangement(int n) {
        // 4ms
        Integer[] memo = new Integer[(1 << n) - 1];
        return dfs(memo, n, 1, 0);
    }

    private int dfs(Integer[] memo, int n, int pos, int used) {
        if (Integer.bitCount(used) == n)
            return 1;

        if (memo[used] != null)
            return memo[used];

        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (i % pos != 0 && pos % i != 0)
                continue;
            int mask = 1 << (i - 1);
            if ((used & mask) == 0) {
                res += dfs(memo, n, pos + 1, used | mask);
            }
        }

        memo[used] = res;

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = countArrangement(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
