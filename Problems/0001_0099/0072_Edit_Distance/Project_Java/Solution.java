import java.util.*;

public class Solution {
    public int minDistance(String word1, String word2) {
        // 4ms
        int m = word1.length();
        int n = word2.length();
        int[][] table = new int[m + 1][n + 1];

        for (int i = 0; i < m + 1; i++)
            table[i][0] = i;
        for (int j = 0; j < n + 1; j++)
            table[0][j] = j;

        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    table[i][j] = table[i - 1][j - 1];
                } else {
                    table[i][j] = 1 + Math.min(Math.min(table[i - 1][j], table[i][j - 1]), table[i - 1][j - 1]);
                }
            }
        }

        return table[m][n];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String word1 = flds[0];
        String word2 = flds[1];
        System.out.println("word1 = " + word1 + ", word2 = " + word2);

        long start = System.currentTimeMillis();

        int result = minDistance(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
