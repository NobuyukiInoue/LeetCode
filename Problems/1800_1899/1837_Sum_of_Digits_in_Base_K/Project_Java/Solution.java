import java.util.*;

public class Solution {
    public int sumBase(int n, int k) {
        // 0ms
        int num = 0;
        while (n > 0) {
            num += n % k;
            n /= k;
        }
        return num;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = sumBase(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
