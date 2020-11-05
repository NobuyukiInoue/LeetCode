import java.util.*;

public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        // 5ms
        if (s1.length() == 0 && s2.length() == 0 && s3.length() == 0)
            return true;
        if (s3.length() != s1.length() + s2.length())
            return false;
        
        boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
        dp[0][0] = true;
        for (int i = 1; i <= s1.length(); i++) {
            if (s3.charAt(i - 1) == s1.charAt(i - 1))
                dp[i][0] = true;
            else
                break;
        }
        for (int j = 1; j <= s2.length(); j++) {
            if (s3.charAt(j - 1) == s2.charAt(j - 1))
                dp[0][j] = true;
            else
                break;
        }
        for (int i = 1; i <= s1.length(); i++) {
            for (int j = 1; j <= s2.length(); j++) {
                if (s3.charAt(i + j - 1) == s1.charAt(i - 1))
                    dp[i][j] = dp[i - 1][j] || dp[i][j];
                if (s3.charAt(i + j - 1) == s2.charAt(j - 1))
                    dp[i][j] = dp[i][j - 1] || dp[i][j];
            }
        }

        return dp[s1.length()][s2.length()];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        String s1 = flds[0];
        String s2 = flds[1];
        String s3 = flds[2];
        System.out.println("s1 = " + s1 + ", s2 = " + s2 + ", s3 = " + s3);

        long start = System.currentTimeMillis();

        Boolean result = isInterleave(s1, s2, s3);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
