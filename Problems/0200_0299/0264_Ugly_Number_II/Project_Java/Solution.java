import java.util.*;

public class Solution {
    public int nthUglyNumber(int n) {
        // 2ms
        int[] ugly = new int[n];
        for (int i = 0; i < ugly.length; i++)
            ugly[i] = 1;

        int i2, i3, i5, x, v2, v3, v5;
        i2 = i3 = i5 = -1;
        x = v2 = v3 = v5 = 1;

        for (int k = 0; k < n; k++) {
            x = min(v2, v3, v5);
            ugly[k] = x;
            if (x == v2) {
                i2++;
                v2 = ugly[i2] * 2;
            }
            if (x == v3) {
                i3++;
                v3 = ugly[i3] * 3;
            }
            if (x == v5) {
                i5++;
                v5 = ugly[i5] * 5;
            }
        }
        return x;
    }

    private int min(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= a && b <= c)
            return b;
        else
            return c;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = nthUglyNumber(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
