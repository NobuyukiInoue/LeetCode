import java.util.*;

public class Solution {
    public int countVowelStrings(int n) {
        // 0ms
        int[] dp = new int[5];
        Arrays.fill(dp, 1);
        for (int i = 2; i < n + 1; i++) {
            for (int j = 1; j < 5; j++) {
                dp[j] = dp[j] + dp[j - 1];
            }
        }
        int ans = 0;
        for (int i = 0; i < 5; i++) {
            ans += dp[i];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = countVowelStrings(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
