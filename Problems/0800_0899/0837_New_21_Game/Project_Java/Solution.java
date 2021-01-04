import java.util.*;

public class Solution {
    public double new21Game(int N, int K, int W) {
        // 4ms
        if (K == 0 || N >= K + W)
            return 1;
        double dp[] = new double[N + 1], Wsum = 1, res = 0;
        dp[0] = 1;
        for (int i = 1; i <= N; ++i) {
            dp[i] = Wsum / W;
            if (i < K) {
                Wsum += dp[i];
            } else {
                res += dp[i];
            }
            if (i - W >= 0) {
                Wsum -= dp[i - W];
            }
        }
        return res;
    }

    public double new21Game_bad(int N, int K, int W) {
        if (K == 0 || N >= K + W - 1)
            return 1.0;
        List<Double> memo = new ArrayList<>();
        int i, j;
        for (i = 0; i < K + W - N; i++)
            memo.add(0.0);
        for (j = 0; j < K + W - N - 1; j++)
            memo.add(1.0);
        memo.add((double)(N - K + 1)/(double)W);
        double u = 1.0/W;
        double v = 1.0 + 1.0/W;
        for (i = 0; i < K - 1; i++)
            memo.add(v*memo.get(memo.size() - 1) - u*memo.get(memo.size() + ~W));
        return memo.get(memo.size() - 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int N = Integer.parseInt(flds[0]);
        int K = Integer.parseInt(flds[1]);
        int W = Integer.parseInt(flds[2]);
        System.out.println("N, K, W = " + Integer.toString(N) + ", " + Integer.toString(K) + ", " + Integer.toString(W));

        long start = System.currentTimeMillis();

        double result = new21Game(N, K, W);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
