import java.util.*;

public class Solution {
    public int maximumXorProduct(long a, long b, int n) {
        // 1ms
        long mask = ((1L << n) - 1);
        long temp_a = a & ~mask;
        long temp_b = b & ~mask;
        for (int i = n - 1; i >= 0; --i) {
            long x = 1L << i;
            if (((a >> i) & 1) == ((b >> i) & 1)){
                temp_a |= x;
                temp_b |= x;
            } else {
                if (temp_a > temp_b) {
                    temp_b |= x;
                } else {
                    temp_a |= x;
                }
            }
        }
        int MOD = 1_000_000_007;
        return (int)(((temp_a%MOD)*(temp_b%MOD))%MOD);
    }

    public int maximumXorProduct_bad(long a, long b, int n) {
        for (int i = 0; i < n; i++) {
            long x = 1L << i;
            long t1 = a^x;
            long t2 = b^x;
            if (t1*t2 > a*b) {
                a = t1;
                b = t2;
            }
        }
        int MOD = 1_000_000_007;
        long ans = ((a%MOD)*(b%MOD))%MOD;
        return (int)ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        long a = Long.parseLong(flds[0]);
        long b = Long.parseLong(flds[1]);
        int n = Integer.parseInt(flds[2]);
        System.out.println("a = " + a + ", b = " + b + ", n = " + n);

        long start = System.currentTimeMillis();

        int result = maximumXorProduct(a, b, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
