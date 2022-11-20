import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        // 1ms - 3ms
        Stack<Character> stack = new Stack<>();
        for (char element : s.toCharArray()) {
            if (element == '(' || element == '[' || element == '{') {
                stack.push(element);
                continue;
            } else if (stack.empty()) {
                return false;
            }
            char top = stack.pop();
            if (top == '(' && element != ')') {
                return false;
            } else if (top == '[' && element != ']') {
                return false;
            } else if (top == '{' && element != '}') {
                return false;
            }
        }
        return stack.empty();
    }

    public boolean isValid2(String s) {
        // 2ms - 5ms
        HashMap<Character, Integer> dic = new HashMap<>();
        dic.put('(', 1);
        dic.put(')', 2);
        dic.put('[', 3);
        dic.put(']',6);
        dic.put('{',5);
        dic.put('}',10);
        Stack<Integer> res = new Stack<>();
        for (char ch : s.toCharArray()) {
            int temp = dic.get(ch);
            if (temp % 2 > 0) {
                res.add(temp);
            } else {
                if (res.size() > 0 && res.peek() == temp / 2) {
                    res.pop();
                } else {
                    return false;
                }
            }
        }
        return res.isEmpty();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        boolean result = isValid(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
