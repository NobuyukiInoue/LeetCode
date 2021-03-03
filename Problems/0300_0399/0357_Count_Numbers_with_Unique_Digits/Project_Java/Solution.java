import java.util.*;

public class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        // 0ms
        if (n == 0)
            return 1;
        int res = 10, h = 9;
        for (int i = 0; i < n - 1; i++) {
            res += 9*h;
            h *= 8 - i;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = countNumbersWithUniqueDigits(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
