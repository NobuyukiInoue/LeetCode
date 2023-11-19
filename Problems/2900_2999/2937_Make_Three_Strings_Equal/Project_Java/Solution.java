import java.util.*;

public class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        // 2ms
        int min_length = Math.min(Math.min(s1.length(), s2.length()), s3.length());
        int total_length = s1.length() + s2.length() + s3.length();
        if (s1.charAt(0) != s2.charAt(0)
         || s2.charAt(0) != s3.charAt(0)
         || s3.charAt(0) != s1.charAt(0))
            return -1;
        for (int i = 0; i < min_length; i++) {
        if (s1.charAt(i) == s2.charAt(i)
         && s2.charAt(i) == s3.charAt(i)
         && s3.charAt(i) == s1.charAt(i)) {
                total_length -= 3;
            } else {
                break;
            }
        }
        return total_length;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        String s1 = flds[0], s2 = flds[1], s3 = flds[2];
        System.out.println("s1 = " + s1 + ", s2 = " + s2 + ", s3 = " + s3);

        long start = System.currentTimeMillis();

        int result = findMinimumOperations(s1, s2, s3);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
