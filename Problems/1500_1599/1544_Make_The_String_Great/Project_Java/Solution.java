import java.util.*;

public class Solution {
    public String makeGood(String s) {
        // 2ms
        Deque<Character> dq = new ArrayDeque<>();
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (!dq.isEmpty() && (dq.peekLast() ^ 32) == c) {
                dq.pollLast();
            } else {
                dq.offer(c);
            }
        }
        StringBuilder ans = new StringBuilder();
        for (char c : dq) {
            ans.append(c);
        }
        return ans.toString();
    }

    public void Main(String temp) {
        String s = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = makeGood(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
