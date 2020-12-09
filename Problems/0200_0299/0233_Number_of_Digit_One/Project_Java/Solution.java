import java.util.*;

public class Solution {
    public int countDigitOne(int n) {
        // 0ms
        int count = 0;
        for (long k = 1; k <= n; k *= 10) {
            long r = n / k, m = n % k;
            count += (r + 8) / 10 * k + (r % 10 == 1 ? m + 1 : 0);
        }
        return count;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int result = countDigitOne(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
