import java.util.*;

public class Solution {
    public int myAtoi(String str) {
        // 1ms
        str = str.trim();
        boolean neg = false;
        long x = 0;

       for (int i = 0; i < str.length(); ++i) {
            if (i==0 && str.charAt(0) == '-') {
                neg = true;
                continue;
            }
            if (i==0 && str.charAt(0) == '+') {
                continue;
            }
            if (str.charAt(i) < '0' || str.charAt(i) > '9') {
                break;
            }
            x = x * 10 + (str.charAt(i) - '0');
            if (x > Integer.MAX_VALUE) {
                return neg? Integer.MIN_VALUE:Integer.MAX_VALUE;
            }
        }

        return neg? -1 * (int)x: (int) x;
    }

    public void Main(String temp) {
        String str = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("str = " + str);

        long start = System.currentTimeMillis();

        int result = myAtoi(str);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
