import java.util.*;

public class Solution {
    public int maxDepth(String s) {
        // 0ms
        int depth = 0, max_depth = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                if (++depth > max_depth) {
                    max_depth = depth;
                }
            } else if (ch == ')') {
                depth--;
            }
        }
        return max_depth;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = maxDepth(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
