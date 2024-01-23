import java.util.*;

public class Solution {
    public int kthFactor(int n, int k) {
        // 0ms
        int cnt = 0;
        for (int i = 1; i < n/2 + 1; i++) {
            if (n % i == 0) {
                if (++cnt == k) {
                    return i;
                }
            }
        }
        if (cnt == k - 1)
            return n;
        return -1;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = kthFactor(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
