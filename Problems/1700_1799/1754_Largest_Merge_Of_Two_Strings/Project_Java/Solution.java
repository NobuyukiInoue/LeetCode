import java.util.*;

public class Solution {
    public String largestMerge(String word1, String word2) {
        // 47ms - 48ms
        int i = 0, j = 0;
        StringBuilder sb = new StringBuilder();
        while (i < word1.length() && j < word2.length()) {
            if (word1.charAt(i) > word2.charAt(j)) {
                sb.append(word1.charAt(i++));
            } else if (word1.charAt(i) < word2.charAt(j)) {
                sb.append(word2.charAt(j++));
            } else {
                if (word1.substring(i, word1.length()).compareTo(word2.substring(j, word2.length())) > 0) {
					sb.append(word1.charAt(i++));
				} else  {
					sb.append(word2.charAt(j++));
				} 
            }
        }
        while(i < word1.length()) {
             sb.append(word1.charAt(i++));
        }
        while(j < word2.length()) {
             sb.append(word2.charAt(j++));
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String word1 = flds[0];
        String word2 = flds[1];

        System.out.println("word1 = \"" + word1 + "\", word2 = \"" + word2 + "\"");
        long start = System.currentTimeMillis();

        String result = largestMerge(word1, word2);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
