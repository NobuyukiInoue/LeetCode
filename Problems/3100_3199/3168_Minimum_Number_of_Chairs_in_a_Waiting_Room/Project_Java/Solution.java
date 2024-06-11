import java.util.*;

public class Solution {
    public int minimumChairs(String s) {
        // 1ms
        int ans = 0, cnt = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'E') {
                cnt++;
            } else {
                cnt--;
            }
            ans = Math.max(ans, cnt);
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = minimumChairs(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
