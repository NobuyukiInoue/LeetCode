import java.util.*;

public class Solution {
    public int maxPower(String s) {
        // 1ms
        char s_ch = s.charAt(0);
        int max_count = 1, count = 1;
        for (int i = 1; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == s_ch) {
                count++;
                if (count > max_count) {
                    max_count = count;
                }
            } else {
                s_ch = ch;
                count = 1;
            }
        }
        return max_count;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = maxPower(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
