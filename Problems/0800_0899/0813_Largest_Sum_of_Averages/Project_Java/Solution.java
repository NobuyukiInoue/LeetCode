import java.util.*;

public class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        // 7ms
        int N = A.length;
        double[][] memo = new double[N + 1][N + 1];
        double cur = 0;
        for (int i = 0; i < N; ++i) {
            cur += A[i];
            memo[i + 1][1] = cur/(i + 1);
        }
        return search(N, K, A, memo);
    }

    public double search(int n, int k, int[] A, double[][] memo) {
        if (memo[n][k] > 0) {
            return memo[n][k];
        }
        if (n < k) {
            return 0;
        }

        double cur = 0;
        for (int i = n - 1; i > 0; --i) {
            cur += A[i];
            memo[n][k] = Math.max(memo[n][k], search(i, k - 1, A, memo) + cur/(n - i));
        }
        return memo[n][k];
    }

/*
    // Time Limit Exceeded.

    HashMap<Integer[], Double> cache;
    public double largestSumOfAverages(int[] A, int K) {
        cache = new HashMap<>();
        return rec(0, A, K);
    }

    private double rec(int st, int[] A, int k) {
        Integer[] st_k = new Integer[] {st, k}; 
        if (cache.containsKey(st_k)) {
            return cache.get(st_k);
        }
        if (k == 1) {
            int temp = 0;
            for (int i = st; i < A.length; i++) {
                temp += A[i];
            }
            cache.put(st_k, (double)temp/(A.length - st));
            return cache.get(st_k);
        }
        double total = 0.0;
        double res = -Double.MAX_VALUE;
        for (int i = st; i < A.length - k + 1; i++) {
            total += A[i];
            res = Math.max(res, (total/(i - st + 1)) + rec(i + 1, A, k - 1));
        }
        cache.put(st_k, res);
        return cache.get(st_k);
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds[0]);
        int K = Integer.parseInt(flds[1]);
        System.out.println("A = " + ml.intArrayToString(A) + ", K = " + Integer.toString(K));

        long start = System.currentTimeMillis();

        double result = largestSumOfAverages(A, K);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
