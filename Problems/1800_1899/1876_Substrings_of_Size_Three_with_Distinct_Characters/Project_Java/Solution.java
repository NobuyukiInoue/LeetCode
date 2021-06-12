import java.util.*;

public class Solution {
    public int countGoodSubstrings(String s) {
        // 1ms
        int res = 0;
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) != s.charAt(i + 1) && s.charAt(i + 1) != s.charAt(i + 2) && s.charAt(i + 2) != s.charAt(i)) {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = countGoodSubstrings(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
