import java.util.*;

public class Solution {
    public String reversePrefix(String word, char ch) {
        // 0ms
    	return new StringBuilder(word.substring(0, word.indexOf(ch) + 1)).reverse().toString() + word.substring(word.indexOf(ch) + 1);
    }

    public String reversePrefix2(String word, char ch) {
        // 6ms
        int pos = word.indexOf(ch);
        if (pos >= 0) {
            StringBuilder sb = new StringBuilder(word.substring(0, pos));
            return word.charAt(pos) + sb.reverse().toString() + word.substring(pos + 1);
        } else {
            return word;
        }
    }

    public String reversePrefix3(String word, char ch) {
        // 6ms
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ch) {
                StringBuilder sb = new StringBuilder(word.substring(0, i));
                return word.charAt(i) + sb.reverse().toString() + word.substring(i + 1);
            }
        }
        return word;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String word = flds[0];
        char ch = flds[1].charAt(0);
        System.out.println("word = " + word + ", ch = " + ch);

        long start = System.currentTimeMillis();

        String result = reversePrefix(word, ch);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
