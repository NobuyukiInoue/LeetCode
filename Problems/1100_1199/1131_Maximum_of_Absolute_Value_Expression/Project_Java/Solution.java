import java.util.*;

public class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        // 3ms
        int res = 0, n = arr1.length, P[] = {-1, 1};
        for (int p : P) {
            for (int q : P) {
                int closest = p*arr1[0] + q*arr2[0] + 0;
                for (int i = 1; i < n; ++i) {
                    int cur = p*arr1[i] + q*arr2[i] + i;
                    res = Math.max(res, cur - closest);
                    closest = Math.min(closest, cur);
                }
            }
        }
        return res;
    }

    public int maxAbsValExpr2(int[] arr1, int[] arr2) {
        // Time Limit Exceeded
        int max = 0;
        for (int i = 0; i < arr1.length; i++) {
            for (int j = i + 1; j < arr1.length; j++) {
                int res = Math.abs(arr1[i] - arr1[j]) + Math.abs(arr2[i] - arr2[j]) + Math.abs(i - j);
                if (res > max)
                    max = res;
            }
        }
        return max;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr1 = ml.stringTointArray(flds[0]);
        int[] arr2 = ml.stringTointArray(flds[1]);

        System.out.println("arr1 = " + ml.intArrayToString(arr1) + ", arr2 = " + ml.intArrayToString(arr2));

        long t_start = System.currentTimeMillis();

        int result = maxAbsValExpr(arr1, arr2);

        long t_end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((t_end - t_start)  + "ms\n");
    }
}
