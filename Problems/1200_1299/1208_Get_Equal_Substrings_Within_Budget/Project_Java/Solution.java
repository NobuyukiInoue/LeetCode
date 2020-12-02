import java.util.*;

public class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        // 5ms
        int i = 0, j;
        int sLength = s.length();
        for (j = 0; j < sLength; j++) {
            maxCost -= Math.abs(s.charAt(j) - t.charAt(j));
            if (maxCost < 0) {
                maxCost += Math.abs(s.charAt(i) - t.charAt(i));
                i++;
            }
        }
        return j - i;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String s = flds[0];
        String t = flds[1];
        int maxCost = Integer.parseInt(flds[2]);
        System.out.println("s = " + s + ", t = " + t + ", maxCost = " + Integer.toString(maxCost));

        long start = System.currentTimeMillis();

        int result = equalSubstring(s, t, maxCost);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
