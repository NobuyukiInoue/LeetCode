import java.util.*;

public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // 10ms
        int len1 = text1.length();
        int len2 = text2.length();
        int[][] matrix = new int[len1 + 1][len2 + 1];

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if(text1.charAt(i) == text2.charAt(j)) {
                    matrix[i + 1][j + 1] = matrix[i][j] + 1;
                } else {
                    matrix[i + 1][j + 1] = Math.max(matrix[i + 1][j], matrix[i][j + 1]);
                }
            }
        }

        return matrix[len1][len2];
    }

    public int longestCommonSubsequence2(String text1, String text2) {
        // 9ms
        int len1 = text1.length();
        int len2 = text2.length();
        int[][] dp = new int[len1 + 1][len2 + 1];

        if (text1.charAt(0) == text2.charAt(0)) {
            dp[0][0] = 1;
        } else {
            dp[0][0] = 0;
        }

        for (int i = 1; i < len1; i++) {
            if (text1.charAt(i) == text2.charAt(0)) {
                dp[i][0] = 1;
            } else {
                dp[i][0] = dp[i - 1][0];
            }
        }

        for (int j = 1; j < len2; j++) {
            if (text1.charAt(0) == text2.charAt(j)) {
                dp[0][j] = 1;
            } else {
                dp[0][j] = dp[0][j - 1];
            }
        }

        for (int i = 1; i < len1; i++) {
            for (int j = 1; j < len2; j++) {
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[len1 - 1][len2 - 1];
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String temp) {
        String[] flds  = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String text1 = flds[0];
        String text2 = flds[1];
        System.out.println("text1 = " + text1 + ", text2 = " + text2);

        long start = System.currentTimeMillis();
        
        int result = longestCommonSubsequence(text1, text2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
