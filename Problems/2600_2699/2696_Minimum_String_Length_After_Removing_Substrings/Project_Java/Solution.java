import java.util.*;

public class Solution {
    public int minLength(String s) {
        // 7ms
        Stack<Character> st = new Stack<>();
        int n = s.length();
        st.push(s.charAt(0));
        for (int i = 1; i < n; i++) {
            if (!st.isEmpty() && ((s.charAt(i) == 'B' && st.peek() == 'A') || (s.charAt(i) == 'D' && st.peek() == 'C'))) {
                st.pop();
            } else {
                st.push(s.charAt(i));
            }
        }
        return st.size();
    }

    public int minLength2(String s) {
        // 4ms
        StringBuilder sb = new StringBuilder(s);
        int i = 0;
        while (i < sb.length() - 1) {
            if (sb.charAt(i) == 'A' && sb.charAt(i + 1) == 'B') {
                sb.delete(i,i + 2);
                i = Math.max(0, i - 1);
            } else if (sb.charAt(i) == 'C' && sb.charAt(i + 1) == 'D') {
                sb.delete(i, i + 2);
                i = Math.max(0, i - 1);
            } else {
                i++;
            }
        }
        return sb.length();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = minLength(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
