import java.util.*;

public class Solution {
    public String removeDuplicateLetters(String s) {
        // 1ms
        if (s == null || s.length() == 0) {
            return "";
        }
        char[] ss = s.toCharArray();
        int[] cnt = new int[26];
        char[] stack = new char[26];
        int leftMost = 0, rightMost = 0;
        boolean[] existInStack = new boolean[26];
        StringBuilder sb = new StringBuilder();
        for (char curChar : ss) {
            cnt[curChar - 'a']++;
        }
        for (char curChar : ss) {
            if (cnt[curChar - 'a'] == -1) {
                continue;
            }
            if (!existInStack[curChar - 'a']) {
                existInStack[curChar - 'a'] = true;
                while (leftMost < rightMost && curChar < stack[rightMost - 1]) {
                    existInStack[stack[--rightMost] - 'a'] = false;
                }
                stack[rightMost++] = curChar;
            }
            if (--cnt[curChar - 'a'] == 0) {
                while (leftMost < rightMost) {
                    cnt[stack[leftMost] - 'a'] = -1;
                    if (stack[leftMost++] == curChar) {
                        break;
                    }
                }
            }
        }
        sb.append(stack, 0, rightMost);
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        String result = removeDuplicateLetters(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
