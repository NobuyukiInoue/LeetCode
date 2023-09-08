import java.util.*;

public class Solution {
    public int stoneGameII(int[] piles) {
        // 2ms
        if (piles.length == 0) {
            return 0;
        }
        int[][] dp = new int[piles.length][];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = new int[piles.length];
        }
        int[] suffixSum = new int[piles.length];
        suffixSum[suffixSum.length - 1] = piles[piles.length -1];
        for (int i = piles.length - 2; i >= 0; i--) {
            suffixSum[i] = piles[i] + suffixSum[i + 1];
        }
        return helper(piles, dp, suffixSum, 0, 1);
    }

    private int helper(int[] piles, int[][]dp, int[] suffixSum, int i, int M) {
        if (i == piles.length) {
            return 0;
        }
        if (i + 2*M >= piles.length) {
            return suffixSum[i];
        }
        if (dp[i][M] != 0) {
            return dp[i][M];
        }
        int result = 0;
        for (int x = 1; x <= 2*M; x++) {
            result = Math.max(result, suffixSum[i] - helper(piles, dp, suffixSum, i + x, Math.max(M, x)));
        }
        dp[i][M] = result;
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] piles = ml.stringToIntArray(flds);
        System.out.println("piles = " + ml.intArrayToString(piles));

        long start = System.currentTimeMillis();

        int result = stoneGameII(piles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
