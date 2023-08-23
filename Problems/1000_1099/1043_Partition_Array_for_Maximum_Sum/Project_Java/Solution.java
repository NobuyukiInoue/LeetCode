import java.util.*;

public class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        // 5ms - 6ms
        int n = arr.length;
        int dp[] = new int[n];
        dp[0] = arr[0];
        int max_val = arr[0];
        for (int i = 1; i < k; i++) {
            max_val = Math.max(max_val, arr[i]);
            dp[i] = max_val*(i + 1);
        }
        for (int i = k; i < n; i++) {
            max_val = arr[i];
            for (int j = 1; j < k + 1; j++) {
                max_val = Math.max(max_val, arr[i - j + 1]);
                dp[i] = Math.max(dp[i], dp[i - j] + max_val*j);
            }
        }
        return dp[n - 1];
    }

    public int maxSumAfterPartitioning1(int[] arr, int k) {
        // 5ms - 6ms
        int n = arr.length;
        int dp[] = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = arr[i];
        }
        int max_val = arr[0];
        for (int i = 1; i < k; i++) {
            max_val = Math.max(max_val, arr[i]);
            dp[i] = max_val*(i + 1);
        }
        int[][] maxs = new int[n][k + 1];
        for (int i = n - 1; i > k - 2; i--) {
            max_val = arr[i];
            for (int j = 0; j < k + 1; j++) {
                if (i - j >= 0) {
                    max_val = Math.max(max_val, arr[i - j]);
                } else {
                    max_val = Math.max(max_val, arr[n + (i - j)]);
                }
                maxs[i][j] = max_val*(j + 1);
            }
        }
        for (int i = k; i < n; i++) {
            max_val = 0;
            for (int j = 1; j < k + 1; j++) {
                max_val = Math.max(max_val, maxs[i][j - 1] + dp[i - j]);
            }
            dp[i] = max_val;
        }
        return dp[n - 1];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = maxSumAfterPartitioning(arr, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
