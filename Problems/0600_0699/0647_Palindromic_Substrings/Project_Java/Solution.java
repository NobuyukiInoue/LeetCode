import java.util.*;

public class Solution {
    public int countSubstrings(String s) {
        // 2ms
        int s_length = s.length();
        int res = s.length();
        for (int i = 1; i < s_length; i++) {
            for (int j = 1;  j < Math.min(s_length - i - 1, i) + 1; j++) {
                if (s.charAt(i - j) == s.charAt(i + j)) {
                    res++;
                } else {
                    break;
                }
            }
            if (s.charAt(i) == s.charAt(i - 1)) {
                res++;
                for (int j = 1;  j < Math.min(i - 1, s_length - i - 1) + 1; j++) {
                    if (s.charAt(i + j) == s.charAt(i - 1 - j)) {
                        res++;
                    } else {
                        break;
                    }
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = countSubstrings(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
