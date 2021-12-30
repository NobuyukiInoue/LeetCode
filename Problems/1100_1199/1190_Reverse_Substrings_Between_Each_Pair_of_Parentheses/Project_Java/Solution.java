import java.util.*;

public class Solution {
    public String reverseParentheses(String s) {
        // 3ms
        int n = s.length();
        Stack<Integer> opened = new Stack<>();
        int[] pair = new int[n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(')
                opened.push(i);
            if (s.charAt(i) == ')') {
                int j = opened.pop();
                pair[i] = j;
                pair[j] = i;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0, d = 1; i < n; i += d) {
            if (s.charAt(i) == '(' || s.charAt(i) == ')') {
                i = pair[i];
                d = -d;
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
    
    public void Main(String temp) {
        String rings = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("rings = " + rings);

        long start = System.currentTimeMillis();

        String result = reverseParentheses(rings);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
