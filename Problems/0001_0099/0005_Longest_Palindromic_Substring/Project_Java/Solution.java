import java.util.*;

public class Solution {
    public String longestPalindrome(String s) {
        // 23ms
        int from = 0, to = 0;
        for (int i = 0; i < s.length(); ++i) {
            int[] oddLenResult = expandFromCenter(s, i - 1, i + 1);
            if (oddLenResult[1] - oddLenResult[0] > to - from) {
                from = oddLenResult[0];
                to = oddLenResult[1];
            }
            int[] evenLenResult = expandFromCenter(s, i, i + 1);
            if (evenLenResult[1] - evenLenResult[0] > to - from) {
                from = evenLenResult[0];
                to = evenLenResult[1];
            }
        }
        return s.substring(from, to);
    }
    
    private int[] expandFromCenter(String s, int left, int right) {
        int p = left, q = right;
        while (p >= 0 && q < s.length() && s.charAt(p) == s.charAt(q)) {
            --p;
            ++q;
        }
        return new int[] {p + 1, q};
    }

    public String longestPalindrome2(String s) {
        // 198ms
        int n = s.length();
        String res = "";
        boolean[][] dp = new boolean[n][n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
                if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
                    res = s.substring(i, j + 1);
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = longestPalindrome(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
