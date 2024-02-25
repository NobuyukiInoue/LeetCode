import java.util.*;

public class Solution {
    public int[] constructArray(int n, int k) {
        // 1ms
        int[] ans = new int[n];
        for (int i = 0, l = 1, r = n; l <= r; i++) {
            ans[i] = k > 1 ? (k-- % 2 != 0 ? l++ : r--) : l++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);

        System.out.println("n = " + n + ", k = " + k);

        long start = System.currentTimeMillis();

        int[] result = constructArray(n, k);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
