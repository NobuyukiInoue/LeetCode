import java.util.*;

public class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        // 0ms
        int max_len = -1;
        for ( char ch : s.toCharArray()){
            max_len = Math.max(max_len, s.lastIndexOf(ch) - s.indexOf(ch) - 1);
        }
        return(max_len);
    }

    public int maxLengthBetweenEqualCharacters2(String s) {
        // 0ms
        int[] width = new int[26];
        for (int i = 0; i < 26; i++)
            width[i] = -1;

        int max_len = -1;
        for (int i = 0; i < s.length(); i++) {
            int ch = (int)s.charAt(i) - (int)'a';
            if (width[ch] != -1)
                max_len = Math.max(max_len, i - width[ch] - 1);
            if (width[ch] == -1)
                width[ch] = i;
        }
        return max_len;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = maxLengthBetweenEqualCharacters(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
