import java.util.*;

public class Solution {
    public int minimumLength(String s) {
        // 4ms - 6ms
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }
            char ch = s.charAt(left);
            while (s.charAt(left) == ch && left < right) {
                left++;
            }
            while (s.charAt(right) == ch && left <= right) {
                right--;
            }
        }
        return right - left + 1;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = minimumLength(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
