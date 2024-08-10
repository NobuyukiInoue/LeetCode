import java.util.*;

public class Solution {
    public String getSmallestString(String s) {
        // 8ms - 10ms
        char[] arr_s = s.toCharArray();
        for (int i = 0; i < arr_s.length - 1; i++) {
            int m1 = arr_s[i]%2;
            int m2 = arr_s[i + 1]%2;
            if (m1 == m2 && arr_s[i] > arr_s[i + 1]) {
                return s.substring(0, i) + arr_s[i + 1] + arr_s[i] + s.substring(i + 2);
            }
        }
        return s;
    }

    public String getSmallestString2(String s) {
        // 9ms
        for (int i = 0; i < s.length() - 1; i++) {
            char c1 = s.charAt(i);
            char c2 = s.charAt(i + 1);
            int m1 = c1%2;
            int m2 = c2%2;
            if (m1 == m2 && c1 > c2) {
                return s.substring(0, i) + c2 + c1 + s.substring(i + 2);
            }
        }
        return s;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = getSmallestString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
