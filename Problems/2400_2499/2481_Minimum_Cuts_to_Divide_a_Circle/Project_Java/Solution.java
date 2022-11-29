import java.util.*;

public class Solution {
    public int numberOfCuts(int n) {
        // 0ms
        if (n == 1) {
            return 0;
        }
        return n % 2 > 0 ? n : n / 2;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = numberOfCuts(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
