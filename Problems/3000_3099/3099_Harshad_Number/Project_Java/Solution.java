import java.util.*;

public class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        // 0ms
        int smDigits = 0, temp_x = x;
        while (temp_x > 0) {
            smDigits += temp_x%10;
            temp_x /= 10;
        }
        return x%smDigits == 0 ? smDigits : -1;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim();

        int x = Integer.parseInt(flds);
        System.out.println("x = " + x);

        long start = System.currentTimeMillis();

        int result = sumOfTheDigitsOfHarshadNumber(x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
