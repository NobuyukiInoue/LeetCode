import java.util.*;

public class Solution {
    public int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        // 1ms
        if (a == e && !(a == c && d > Math.min(b, f) && d < Math.max(b, f)))
            return 1;
        if (b == f && !(b == d && c > Math.min(a, e) && c < Math.max(a, e)))
            return 1;
        if (c + d == e + f && !(c + d == a + b && a > Math.min(c , e) && a < Math.max(c, e)))
            return 1;
        if (c - d == e - f && !(c - d == a - b && a > Math.min(c , e) && a < Math.max(c, e)))
            return 1;
        return 2;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int a = Integer.parseInt(flds[0]);
        int b = Integer.parseInt(flds[1]);
        int c = Integer.parseInt(flds[2]);
        int d = Integer.parseInt(flds[3]);
        int e = Integer.parseInt(flds[4]);
        int f = Integer.parseInt(flds[5]);
        System.out.println("a = " + a + ", b = " + b + ",c = " + c + ",d = " + d + ",e = " + e + ", f = " + f);

        long start = System.currentTimeMillis();

        int result = minMovesToCaptureTheQueen(a, b, c, d, e, f);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
