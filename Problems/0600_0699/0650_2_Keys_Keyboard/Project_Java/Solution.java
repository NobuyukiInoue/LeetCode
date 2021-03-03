import java.util.*;

public class Solution {
    public int minSteps(int n) {
        // 0ms
        if (n == 1)
            return 0;

        for (int i = 2; i < (int)Math.sqrt(n) + 1; i++) {
            if (n%i == 0) {
                return minSteps(i) + minSteps(n/i);
            }
        }
        return n;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = minSteps(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
