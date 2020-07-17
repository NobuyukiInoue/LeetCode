import java.util.*;

public class Solution {
    public int calculate(String s) {
        // 10ms
        int total = 0;
        Stack<Integer> signs = new Stack<>();
        signs.push(1);
        signs.push(1);
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0') {
                int number = 0;
                while (i < s.length()  &&  s.charAt(i) >= '0') {
                    number = 10 * number + s.charAt(i++) - '0';
                }
                total += signs.peek() * number;
                signs.pop();
                i--;
            } else if (c == ')') {
                signs.pop();
            } else if (c != ' ') {
                signs.push(signs.peek() * (c == '-' ? -1 : 1));
            }
        }
        return total;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = calculate(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
