import java.util.*;

public class Solution {
    public int countDigits(int num) {
        // 0ms
        int n = num, ans = 0;
        while (n > 0) {
            int val = n % 10;
            if (num % val == 0) {
                ans++;
            }
            n /= 10;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = countDigits(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
