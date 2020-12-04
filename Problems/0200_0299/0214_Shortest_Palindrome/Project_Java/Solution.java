import java.util.*;

public class Solution {
    public String shortestPalindrome(String s) {
        // 6ms
        if (s.length() <= 1)
            return s;

        String new_s = s + "#" + new StringBuilder(s).reverse().toString();
        int[] position = new int[new_s.length()];

        for (int i = 1; i < position.length; i++) {
            int pre_pos = position[i - 1];
            while (pre_pos > 0 && new_s.charAt(pre_pos) != new_s.charAt(i))
                pre_pos = position[pre_pos - 1];
            position[i] = pre_pos+((new_s.charAt(pre_pos) == new_s.charAt(i))? 1: 0);
        }

        return new StringBuilder(s.substring(position[position.length - 1])).reverse().toString() + s;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = shortestPalindrome(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
