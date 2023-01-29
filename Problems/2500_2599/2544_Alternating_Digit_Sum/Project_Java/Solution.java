import java.util.*;

public class Solution {
    public int alternateDigitSum(int n) {
        // 0ms
        int sign = 1, cnt = 0, ans = 0;
        while (n > 0) {
            ans += sign*(n % 10);
            n /= 10;
            sign *= -1;
            cnt++;
        }
        return (cnt % 2 == 1)? ans : -ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = alternateDigitSum(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
