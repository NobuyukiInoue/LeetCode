import java.util.*;

public class Solution {
    public int[] decode(int[] encoded) {
        // 3ms - 4ms
        int n = encoded.length + 1, a = 0, res[] = new int[n];
        for (int i = 0; i <= n; ++i) {
            a ^= i;
            if (i < n && i % 2 == 1) {
                a ^= encoded[i];
            }
        }
        res[0] = a;
        for (int i = 0; i < n - 1; i++) {
            res[i + 1] = res[i] ^ encoded[i];
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] encoded = ml.stringToIntArray(flds);
        System.out.println("encoded = " + ml.intArrayToString(encoded));

        long start = System.currentTimeMillis();

        int[] result = decode(encoded);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
