import java.util.*;

public class Solution {
    public int minDeletionSize2(String[] strs) {
        // 2ms
        int res = 0;
        boolean[] check = new boolean[strs.length];
        Arrays.fill(check, true);
        for (int col = 0; col < strs[0].length(); col++) {
            int prev_res = res;
            for (int i = 0; i < strs.length - 1; i++) {
                if (check[i] && strs[i].charAt(col) > strs[i + 1].charAt(col)) {
                    res++;
                    break;
                }
            }
            if (res == prev_res) {
                for (int i = 0; i < strs.length - 1; i++) {
                    if (strs[i].charAt(col) < strs[i + 1].charAt(col)) {
                        check[i] = false;
                    }
                }
            }
        }
        return res;
    }

    public int minDeletionSize(String[] strs) {
        // 0ms
        int m = strs[0].length();
        int n = strs.length;
        int[] check = new int[n];
        Arrays.fill(check, -1);
        boolean[] del = new boolean[m];
        int res = 0;
        for (int col = 0; col < m; col++) {
            for (int i = 1; i < n; i++) {
                if (check[i] != -1 && !del[check[i]]) {
                    continue;
                }
                if (strs[i].charAt(col) > strs[i - 1].charAt(col)) {
                    check[i] = col;
                } else if (strs[i].charAt(col) < strs[i - 1].charAt(col)) {
                    del[col] = true;
                    res++;
                    break;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] strs = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("strs = " + ml.stringArrayToString(strs));

        long start = System.currentTimeMillis();

        int result = minDeletionSize(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
