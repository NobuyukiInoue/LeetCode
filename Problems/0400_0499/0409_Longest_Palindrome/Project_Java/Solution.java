import java.util.*;

public class Solution {
    public int longestPalindrome(String s) {
        // 1ms
        int[] count = new int[256];
        int l = 0;
        for (char c:s.toCharArray())
            count[c]++;
        for (int i: count)
            l += i >> 1 << 1;
        if (l == s.length())
            return l;
        else
            return l + 1;
    }

    public void Main(String temp) {
        String s = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        int result = longestPalindrome(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
