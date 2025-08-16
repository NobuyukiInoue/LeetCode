import java.util.*;

public class Solution {
    public boolean hasSameDigits(String s) {
        // 8ms
        while (s.length() > 2) {
            StringBuilder new_s =  new StringBuilder();
            for (int i = 0; i < s.length() - 1; i++) {
                new_s.append((s.charAt(i) - '0' + s.charAt(i + 1) - '0')%10);
            }
            s = new_s.toString();
        }
        return s.charAt(0) == s.charAt(1);
    }


    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        boolean result = hasSameDigits(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
