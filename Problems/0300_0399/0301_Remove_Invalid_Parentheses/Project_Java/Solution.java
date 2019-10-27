import java.util.*;

public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> res = new ArrayList<>();
        removeParenthesesHelper(s, 0, 0, res);
        return res;
    }

    private void removeParenthesesHelper(String rawStr, int lastJ, int lastI, List<String> res) {
        int stack = 0;
        for (int i = lastI; i < rawStr.length(); i++) {
            if (rawStr.charAt(i) == '(') {
                stack++;
            } else if (rawStr.charAt(i) == ')') {
                stack--;
            }
            if (stack >= 0) {
                continue;
            }

            for (int j = lastJ; j <= i; j++) {
                if (rawStr.charAt(j) != ')' || j > 0 && rawStr.charAt(j - 1) == ')') {
                    continue;
                }
                removeParenthesesHelper(rawStr.substring(0, j) + rawStr.substring(j + 1), j, i, res);
            }
            return;
        }
        int a = 0;
        removeRightInvalidParentheses(rawStr, rawStr.length() - 1, rawStr.length() - 1, res);
    }

    private void removeRightInvalidParentheses(String processedStr, int lastJ, int lastI, List<String> res) {
        int stack = 0;
        for (int i = lastI; i >= 0; i--) {
            if (processedStr.charAt(i) == ')') {
                stack++;
            } else if (processedStr.charAt(i) == '(') {
                stack--;
            }
            if (stack >= 0) {
                continue;
            }

            for (int j = lastJ; j >= i; j--) {
                if (processedStr.charAt(j) != '(' || j < processedStr.length() - 1 && processedStr.charAt(j + 1) == '(') {
                    continue;
                }
                removeRightInvalidParentheses(processedStr.substring(0, j) + processedStr.substring(j + 1), j - 1, i - 1, res);
            }
            return;
        }
        res.add(processedStr);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        List<String> result = removeInvalidParentheses(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
