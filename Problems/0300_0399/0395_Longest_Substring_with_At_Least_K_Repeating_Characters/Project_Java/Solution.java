import java.util.*;

public class Solution {
    public int longestSubstring(String s, int k) {
        // 0ms
        return longest(s, 0, s.length() - 1, k);
    }

    private int longest(String s, int start, int end, int k) {
        if (start > end) {
            return 0;
        }

        int len = end - start + 1;
        if (len == 0 || k > len) {
            return 0;
        }
        if (k <= 1) {
            return len;
        }
        
        int[] alcount = new int['z' - 'a' + 1];
        for (int i = start; i <= end; i++) {
            alcount[s.charAt(i) - 'a']++;
        }

        int i = start;
        while (i <= end && alcount[s.charAt(i) - 'a'] >= k) {
            i++;
        }

        if (i >= end) {
            return i - start;
        }

        int ls1 = longest(s, start, i - 1, k);
        while (i <= end && alcount[s.charAt(i) - 'a'] < k) {
            i++;
        }

        int ls2;
        if (i <= end) {
            ls2 = longest(s, i, end, k);
        } else {
            ls2 = 0;
        }
        return Math.max(ls1, ls2);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = longestSubstring(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
