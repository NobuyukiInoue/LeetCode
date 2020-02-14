import java.util.*;

public class Solution {
    public int clumsy(int N) {
        // 0ms
        return clumsy(N, 1);
    }

    private int clumsy(int n, int sign) {
        if (n <= 0)
            return 0;
        return sign * n * Math.max(n - 1, 1) / Math.max(n - 2, 1) + Math.max(n - 3, 0) + clumsy(n - 4, -1);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int N = Integer.parseInt(flds);
        System.out.println("N = " + Integer.toString(N));

        long start = System.currentTimeMillis();
        
        int result = clumsy(N);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
