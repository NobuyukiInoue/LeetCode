import java.util.*;

public class Solution {
    public String minRemoveToMakeValid(String s) {
        // 28ms - 45ms
        StringBuilder res = new StringBuilder();
        Stack<Integer>stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch ==')') {
                if (stack.empty()) {
                    continue;
                } else {
                    stack.pop();
                    res.append(ch);
                }
            } else if (ch =='(') {
                stack.push(res.length());
                res.append(ch);
            } else {
                res.append(ch);
            }
        }
        while (!stack.empty()) {
            res.deleteCharAt(stack.pop());
        }
        return res.toString();
    }

    public String minRemoveToMakeValid2(String s) {
        // 57ms - 61ms
        StringBuilder sb = new StringBuilder(s);
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < sb.length(); ++i) {
            if (sb.charAt(i) == '(') {
                st.add(i);
            }
            if (sb.charAt(i) == ')') {
                if (!st.empty()) {
                    st.pop();
                } else {
                    sb.setCharAt(i, '*');
                }
            }
        }
        while (!st.empty()) {
            sb.setCharAt(st.pop(), '*');
        }
        return sb.toString().replaceAll("\\*", "");
    }

    public void Main(String temp) {
        String word = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("word = \"" + word + "\"");

        long start = System.currentTimeMillis();

        String result = minRemoveToMakeValid(word);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
