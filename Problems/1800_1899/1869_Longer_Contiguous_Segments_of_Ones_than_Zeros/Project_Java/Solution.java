import java.util.*;

public class Solution {
    public boolean checkZeroOnes(String s) {
        // 0ms
        int c0 = 0, c1 = 0, max_c0 = 0, max_c1 = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '1') {
                c0 = 0;
                c1++;
                max_c1 = Math.max(max_c1, c1);
            } else {
                c1 = 0;
                c0++;
                max_c0 = Math.max(max_c0, c0);
            }
        }
        return max_c1 > max_c0;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        boolean result = checkZeroOnes(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
