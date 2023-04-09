import java.util.*;

public class Solution {
    public String smallestNumber(String pattern) {
        // 0ms
        StringBuilder res = new StringBuilder();
        StringBuilder stack = new StringBuilder();
        for (int i = 0; i <= pattern.length(); i++) {
            stack.append((char)('1' + i));
            if (i == pattern.length() || pattern.charAt(i) == 'I') {
                res.append(stack.reverse());
                stack = new StringBuilder();
            }
        }
        return res.toString();
    }

    public void Main(String temp) {
        String sentence = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        String result = smallestNumber(sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
