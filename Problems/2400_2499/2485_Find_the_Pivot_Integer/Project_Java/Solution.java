import java.util.*;

public class Solution {
    public int pivotInteger(int n) {
        // 1ms - 2ms
        int l_sum = 0;
        int r_sum = n*(n + 1) / 2;
        for (int i = 1; i < n + 1; i++) {
            r_sum -= i;
            if (l_sum == r_sum) {
                return i;
            }
            l_sum += i;
        }
        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = pivotInteger(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
