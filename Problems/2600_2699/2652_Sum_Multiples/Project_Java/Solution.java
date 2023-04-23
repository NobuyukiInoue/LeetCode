import java.util.*;

public class Solution {
    public int sumOfMultiples(int n) {
        // 4ms
        int res = 0;
        for (int i = 1; i < n + 1; i++) {
            if (i%3 == 0 || i%5 == 0 || i%7 == 0) {
                res += i;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int result = sumOfMultiples(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
