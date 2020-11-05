import java.util.*;

public class Solution {
    public boolean backspaceCompare(String S, String T) {
        return check(S).equals(check(T));
    }

    private String check(String s) {
        int backspace = 0;
        StringBuilder sb = new StringBuilder();
        char[] sChar = s.toCharArray();
        for (int i = sChar.length - 1; i >= 0; i--) {
            char c = sChar[i];
            if (c == '#') {
                backspace++;
            } else if (c <= 'z' && c >= 'a' && backspace == 0) {
                sb.append(c);
            } else if (c <= 'z' && c >= 'a' && backspace > 0) {
                backspace--;
            } else {
                continue;
            }
        }
        
        return sb.toString();
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String S = words[0];
        String T = words[1];
        System.out.println("S = " + S + ", T = " + T);

        long start = System.currentTimeMillis();

        boolean result = backspaceCompare(S, T);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
