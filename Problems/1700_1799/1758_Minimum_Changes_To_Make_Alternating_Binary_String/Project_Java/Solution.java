import java.util.*;

public class Solution {
    public int minOperations(String s) {
        // 2ms
        int res = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) - '0' != i % 2) {
                res++;
            }
        }
        return Math.min(res, n - res);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = minOperations(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
