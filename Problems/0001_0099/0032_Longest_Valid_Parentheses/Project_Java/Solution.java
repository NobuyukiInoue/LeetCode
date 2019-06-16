import java.util.*;

public class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        int[] f = new int[n + 1];
        char[] c = s.toCharArray();
        int max = 0;
        for (int i = 2; i <= n; ++i) {
            if (c[i - 1] == ')') {
                if (c[i - 2] == '(') {
                    f[i] = f[i - 2] + 2;
                } else if (i - f[i - 1] - 2 >= 0 && c[i - f[i - 1] - 2] == '(') {
                    f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2;
                }
            }
            max = Math.max(max, f[i]);
        }
        return max;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("S = " + s);

        long start = System.currentTimeMillis();
        
        int result = longestValidParentheses(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
