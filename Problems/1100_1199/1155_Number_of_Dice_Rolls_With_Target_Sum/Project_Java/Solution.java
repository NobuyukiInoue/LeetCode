public class Solution {
    public int numRollsToTarget(int d, int f, int target) {
        // 5ms
        if (f*d < target)
            return 0;
        if (d == 1)
            return 1;
        
        int[][] dp = new int[d + 1][target + 1];

        for (int i = 1; i <= f && i <= target; i++)
            dp[1][i] = 1;

        for (int k = 2; k <= d; k++) {
            for (int i = 1; i <= f && i <= target; i++) {
                for (int j = 1; j <= target - i; j++) {
                    if (j + i <= target) {
                        dp[k][j + i] = (dp[k][j + i] + dp[k - 1][j]) % (1000000007);
                    }
                }
            }
        }

        return dp[d][target];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int d = Integer.parseInt(flds[0]);
        int f = Integer.parseInt(flds[1]);
        int target = Integer.parseInt(flds[2]);
        System.out.println(String.format("d = %d, f = %d, target = %d", d, f, target));

        long start = System.currentTimeMillis();

        int result = numRollsToTarget(d, f, target);

        long end = System.currentTimeMillis();

        System.out.println(String.format("result = %d", result));
        System.out.println((end - start)  + "ms\n");
    }
}
