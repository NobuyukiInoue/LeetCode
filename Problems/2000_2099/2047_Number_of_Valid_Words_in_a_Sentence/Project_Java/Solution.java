import java.util.*;

public class Solution {
    public int countValidWords2(String sentence) {
        // 51ms
        String regex = "^([a-z]+(-?[a-z]+)?)?(!|\\.|,)?$";
        String r2 = "[^0-9]+";
        String[] arr = sentence.split("\\s+");
        int ans = 0;
        for (String s: arr) {
            if (s.matches(regex) && s.matches(r2)) {
                ans++;
            }
        }
        return ans;
    }

    public int countValidWords(String sentence) {
        // 1ms
        int result = 0;
        char s[] = sentence.toCharArray(), ch;
        for (int i = 0, state = 0; i < s.length; ) {
            if (state == 0) {
                if ((ch = s[i++]) == ' ') {
                    continue;
                } else if (isLetter(ch) || (isPunctuationMark(ch) && (i == s.length || s[i] == ' '))) {
                    result++;
                    state = 2;
                } else {
                    state = 1;
                }
            } else if (state > 1) {
                if (isDigit(ch = s[i++]) || (ch == '-' && (4 == ++state || i == s.length || !isLetter(s[i]))) || (isPunctuationMark(ch) && i < s.length && s[i] != ' ')) {
                    result--;
                    state = 1;
                } else if (ch == ' ') {
                    state = 0;
                }
            } else if (s[i++] == ' ') {
                state = 0;
            }
        }
        return result;
    }

    boolean isLetter(int c) {
        return c >= 'a' && c <= 'z';
    }

    boolean isDigit(int c) {
        return c >= '0' && c <= '9';
    }

    boolean isPunctuationMark(int c) {
        return c == '!' || c == '.' || c == ',';
    }

    public void Main(String temp) {
        String sentence = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        int result = countValidWords(sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
