import java.util.*;

public class Solution {
    public int countKeyChanges(String s) {
        // 1ms
        int ans = 0;
        for (int i = 1; i < s.length(); i++) {
            int val = Math.abs(s.charAt(i) - s.charAt(i - 1));
            if (val == 0 || val == 0x20) {
                continue;
            }
            ans++;
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = countKeyChanges(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
