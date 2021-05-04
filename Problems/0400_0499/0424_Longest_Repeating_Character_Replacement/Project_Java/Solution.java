import java.util.*;

public class Solution {
    public int characterReplacement(String s, int k) {
        // 4ms
        int maxf = 0, i = 0, n = s.length(), count[] = new int[26];
        for (int j = 0; j < n; ++j) {
            maxf = Math.max(maxf, ++count[s.charAt(j) - 'A']);
            if (j - i + 1 > maxf + k)
                --count[s.charAt(i++) - 'A'];
        }
        return n - i;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = characterReplacement(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
