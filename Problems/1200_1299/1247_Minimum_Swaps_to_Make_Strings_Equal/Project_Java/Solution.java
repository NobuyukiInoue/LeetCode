import java.util.*;

public class Solution {
    public int minimumSwap(String s1, String s2) {
        // 1ms
        int len1 = s1.length();
        int len2 = s2.length();
        if (len1 != len2) {
            return -1;
        }
        int x = 0, y = 0, ans = 0;
        for (int i = 0; i < len1; i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            if (c1 != c2) {
                if (c1 == 'x') {
                    x++;
                }
                if (c1 == 'y') {
                    y++;
                }
            }
        }
        ans += x/2 + y/2;
        x %= 2;
        y %= 2;
        if (x != y) {
            return -1;
        }
        return ans + x + y;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s1 = flds[0];
        String s2 = flds[1];
        System.out.println("s1 = " + s1 + ", s2 = " + s2);

        long start = System.currentTimeMillis();

        int result = minimumSwap(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
