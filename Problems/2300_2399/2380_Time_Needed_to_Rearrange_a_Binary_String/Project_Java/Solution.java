import java.util.*;

public class Solution {
    public int secondsToRemoveOccurrences(String s) {
        // 3ms
        int ans = 0, prefix = 0, prev = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ans = Math.max(prev, i - prefix);
                prefix++;
                if (ans > 0) {
                    prev = ans + 1;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = secondsToRemoveOccurrences(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
