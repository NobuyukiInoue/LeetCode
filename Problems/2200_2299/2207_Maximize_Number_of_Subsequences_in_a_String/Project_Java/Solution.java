import java.util.*;

public class Solution {
    public long maximumSubsequenceCount(String text, String pattern) {
        // 23ms
        long res = 0, cnt1 = 0, cnt2 = 0;
        for (int i = 0; i < text.length(); ++i) {   
            if (text.charAt(i) == pattern.charAt(1)) {   
                res += cnt1; 
                cnt2++;
            }
            if (text.charAt(i) == pattern.charAt(0)) {   
                cnt1++;
            }
        }
        return res + Math.max(cnt1, cnt2);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String text = flds[0];
        String pattern = flds[1];

        System.out.println("text = \"" + text + "\", pattern = \"" + pattern + "\"");
        long start = System.currentTimeMillis();

        long result = maximumSubsequenceCount(text, pattern);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
