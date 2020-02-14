import java.util.*;

public class Solution {
    public int tribonacci(int n) {
        if (n < 1)
            return 0;
        if (n <= 2)
            return 1;
        int t0 = 0, t1 = 1, t2 = 1, tn;
        for (int i = 3; i <= n; i++) {
            tn = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = tn;
        }

        return t2;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int result = tribonacci(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
