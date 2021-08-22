import java.util.*;

public class Solution {
    public String makeFancyString(String s) {
        // 35ms
        StringBuilder sb = new StringBuilder();
        for (int i = 0, cnt = 0; i < s.length(); i++) {
            if (i > 0 && s.charAt(i - 1) == s.charAt(i)) {
                ++cnt;
            } else {
                cnt = 1;
            }
            if (cnt < 3) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = makeFancyString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
