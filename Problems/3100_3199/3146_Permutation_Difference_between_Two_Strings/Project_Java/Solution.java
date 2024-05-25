import java.util.*;

public class Solution {
    public int findPermutationDifference(String s, String t) {
        // 1ms
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            ans += Math.abs(s.indexOf(ch) - t.indexOf(ch));
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(", ", ",").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");

        String s = flds[0];
        String t = flds[1];
        System.out.println("s = \"" + s + "\", t = \"" + t + "\"");

        long start = System.currentTimeMillis();

        int result = findPermutationDifference(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
