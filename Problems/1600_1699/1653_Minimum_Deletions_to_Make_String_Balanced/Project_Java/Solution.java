import java.util.*;

public class Solution {
    public int minimumDeletions(String s) {
        // 28ms
        int dp = 0, count_b = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'a') {
                dp = Math.min(dp + 1, count_b);
            } else {
                count_b++;
            }
        }
        return dp;
    }

    public int minimumDeletions_stack(String s) {
        // 95ms
        Stack<Character> stack = new Stack<>();
        int count = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'b') {
                stack.push(ch);
            } else if (stack.size() > 0) {
                stack.pop();
                count++;
            }
        }
        return count;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = minimumDeletions(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
