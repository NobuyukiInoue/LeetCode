import java.util.*;

public class Solution {
    // 223ms - 373ms
    private int[] cookies_p;
    private int[] counts;
    private int total = Integer.MAX_VALUE;

    public int distributeCookies(int[] cookies, int k) {
        cookies_p = cookies;
        counts = new int[k];
        dfs(k, 0);
        return total;
    }

    private void dfs(int children, int pos) {
        if (pos >= cookies_p.length) {
            int max = 0;
            for (int count : counts) {
                max = Math.max(max, count);
            }
            total = Math.min(total, max);
            return;
        }
        for (int i = 0; i < children; i++) {
            counts[i] += cookies_p[pos];
            dfs(children, pos + 1);
            counts[i] -= cookies_p[pos];
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] cookies = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("cookies = " + ml.intArrayToString(cookies) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = distributeCookies(cookies, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
