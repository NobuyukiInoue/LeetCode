import java.util.*;

public class Solution {
    public String mergeAlternately(String word1, String word2) {
        // 0ms
        int minLen = Math.min(word1.length(), word2.length());
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < minLen; i++) {
            res.append(word1.charAt(i));
            res.append(word2.charAt(i));
        }
        if (word1.length() > word2.length()) {
            res.append(word1.substring(minLen));
        } else if (word2.length() > word1.length()) {
            res.append(word2.substring(minLen));
        }
        return res.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String word1 = flds[0];
        String word2 = flds[1];
        System.out.println("word1 = " + word1 + ", word2 = " + word2);

        long start = System.currentTimeMillis();

        String result = mergeAlternately(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
