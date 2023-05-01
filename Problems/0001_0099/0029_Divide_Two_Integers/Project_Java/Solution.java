import java.util.*;

public class Solution {
    public int divide(int dividend, int divisor) {
        // 1ms
        if (divisor == 0) {
            return 0;
        }
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        int quotient = 0;
        boolean negative = (dividend < 0) != (divisor < 0);
        long longDividend = Math.abs((long) dividend);
        long longDivisor = Math.abs((long) divisor);
        while (longDividend >= longDivisor) {
            int shift = 0;
            while (longDividend >= (longDivisor << shift)) {
                shift++;
            }
            shift--;
            longDividend -= longDivisor << shift;
            quotient += 1 << shift;
        }
        return negative ? -quotient : quotient;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim().split(",");

        int divide = Integer.parseInt(flds[0]);
        int divisor = Integer.parseInt(flds[1]);
        System.out.println("divide = " + divide + ", divisor = " + divisor);

        long start = System.currentTimeMillis();

        int result = divide(divide, divisor);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
