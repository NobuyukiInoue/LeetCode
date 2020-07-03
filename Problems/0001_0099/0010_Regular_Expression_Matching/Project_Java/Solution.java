import java.util.*;

public class Solution {
    public boolean isMatch(String s, String p) {
        // 2ms
        int[][] memo = new int[s.length() + 1][p.length()];
        return isMatch2(s, 0, p, 0, memo);
    }
    
    private boolean isMatch2(String s, int matchedLengthS, String p, int matchedLengthP, int[][] memo) {
        if (matchedLengthS == s.length() && matchedLengthP == p.length()) {
            return true;
        }

        if (matchedLengthP == p.length()) {
            return false;
        }

        if (memo[matchedLengthS][matchedLengthP] != 0) {
            return memo[matchedLengthS][matchedLengthP] == 1;
        }

        if (matchedLengthP + 1 < p.length() && p.charAt(matchedLengthP + 1) == '*') {
            if (matchedLengthS < s.length() && (p.charAt(matchedLengthP) == s.charAt(matchedLengthS) || p.charAt(matchedLengthP) == '.')) {
                if (isMatch2(s, matchedLengthS + 1, p, matchedLengthP, memo) || isMatch2(s, matchedLengthS + 1, p, matchedLengthP + 2, memo) || isMatch2(s, matchedLengthS, p, matchedLengthP + 2, memo)) {
                    memo[matchedLengthS][matchedLengthP] = 1;
                }
            } else {
                if (isMatch2(s, matchedLengthS, p, matchedLengthP + 2, memo)) {
                    memo[matchedLengthS][matchedLengthP] = 1;
                }
            }
        } else {
            if (matchedLengthS < s.length() && (p.charAt(matchedLengthP) == s.charAt(matchedLengthS) || p.charAt(matchedLengthP) == '.')) {
                if (isMatch2(s, matchedLengthS + 1, p, matchedLengthP + 1, memo)) {
                    memo[matchedLengthS][matchedLengthP] = 1;
                }
            }
        }

        if(memo[matchedLengthS][matchedLengthP] == 0) {
            memo[matchedLengthS][matchedLengthP] = -1;
        }

        return memo[matchedLengthS][matchedLengthP] == 1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s = flds[0], p = flds[1];
        System.out.println("s = \"" + s + "\", p = \"" + p + "\"");

        long start = System.currentTimeMillis();

        boolean result = isMatch(s, p);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
