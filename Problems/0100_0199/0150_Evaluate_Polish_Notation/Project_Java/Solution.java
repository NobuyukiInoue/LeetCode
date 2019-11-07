import java.util.*;

public class Solution {
    public int evalRPN(String[] tokens) {
        // 5ms
        Deque<String> st = new ArrayDeque<>();
        for (String ch : tokens) {
            if (ch.equals("+")) {
                int b = Integer.parseInt(st.pop());
                int a = Integer.parseInt(st.pop());
                st.push(Integer.toString(a + b));
            } else if (ch.equals("-")) {
                int b = Integer.parseInt(st.pop());
                int a = Integer.parseInt(st.pop());
                st.push(Integer.toString(a - b));
            } else if (ch.equals("*")) {
                int b = Integer.parseInt(st.pop());
                int a = Integer.parseInt(st.pop());
                st.push(Integer.toString(a * b));
            } else if (ch.equals("/")) {
                int b = Integer.parseInt(st.pop());
                int a = Integer.parseInt(st.pop());
                st.push(Integer.toString(a / b));                
            } else {
                st.push(ch);
            }
        }
        return Integer.parseInt(st.peek());
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] tokens = args.replace(" ", "").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        System.out.print("tokens = [");
        for (int i = 0; i < tokens.length; i++)
            if (i == 0)
                System.out.print(tokens[i]);
            else
                System.out.print(", " + tokens[i]);
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = evalRPN(tokens);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
