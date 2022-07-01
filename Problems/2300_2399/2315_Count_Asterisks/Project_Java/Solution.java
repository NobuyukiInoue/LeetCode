import java.util.*;

public class Solution {
    public int countAsterisks(String s) {
        // 1ms - 2ms
        int cnt = 0, bar = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '|') {
                bar++;
            }
            if (bar % 2 == 0 && ch == '*') {
                cnt++;
            }
        }
        return cnt;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = countAsterisks(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
