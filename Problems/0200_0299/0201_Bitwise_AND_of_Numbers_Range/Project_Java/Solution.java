import java.util.*;

public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        // 4ms
        if (m == 0) {
            return 0;
        }

        int shift = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            shift += 1;
        }

        return m << shift;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int m = Integer.parseInt(flds[0]);
        int n = Integer.parseInt(flds[1]);
        System.out.println("m = " + Integer.toString(m) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = rangeBitwiseAnd(m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
