import java.util.*;

public class Solution {
    public int commonFactors(int a, int b) {
        // 1ms - 4ms
        int ans = 0;
        for (int i = 1; i < Math.min(a, b) + 1; i++) {
            if (a % i == 0 && b % i == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int a = Integer.parseInt(flds[0]);
        int b = Integer.parseInt(flds[1]);
        System.out.println("a = " + Integer.toString(a) + ", b = " + Integer.toString(b));

        long start = System.currentTimeMillis();

        int result = commonFactors(a, b);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
