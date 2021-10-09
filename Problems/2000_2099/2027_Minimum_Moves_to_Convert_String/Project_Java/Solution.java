import java.util.*;

public class Solution {
    public int minimumMoves(String s) {
        // 0ms
        int left = 0, right = s.length();
        int ans = 0;
        while (left < right) {
            if (s.charAt(left) == 'X') {
                ans++;
                left += 3;
            } else {
                left++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = minimumMoves(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
