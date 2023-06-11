import java.util.*;

public class Solution {
    public boolean isFascinating(int n) {
        // 1ms
        int[] arr = new int[] {n, 2*n, 3*n};
        boolean[] cnts = new boolean[11];
        for (int cur : arr) {
            int temp = cur;
            while (temp > 0) {
                if (cnts[temp%10] == true || temp%10 == 0) {
                    return false;
                }
                cnts[temp%10] = true;
                temp /= 10;
            }
        }
        return true;
    }

    public boolean isFascinating_1liner(int n) {
        // 1ms
        return n == 192 || n == 219 || n == 273 || n == 327;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        boolean result = isFascinating(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
