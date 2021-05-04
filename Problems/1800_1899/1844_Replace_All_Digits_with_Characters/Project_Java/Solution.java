import java.util.*;

public class Solution {
    public String replaceDigits(String s) {
        // 0ms
        char[] res = s.toCharArray();
        for (int i = 1; i < s.length(); i += 2) {
            res[i] = (char)(res[i - 1] + res[i] - '0');
        }
        return String.valueOf(res);
    }

    public String replaceDigits2(String s) {
        // 0ms
        char[] ans = new char[s.length()];
        ans[0] = s.charAt(0);
        for (int i = 1; i < s.length(); i++) {
            char ch = (char)(s.charAt(i) - '0');
            if (0 <= ch && ch <= 9) {
                ans[i] = (char)(s.charAt(i - 1) + ch);
            } else {
                ans[i] = s.charAt(i);
            }
        }
        return String.valueOf(ans);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = replaceDigits(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
