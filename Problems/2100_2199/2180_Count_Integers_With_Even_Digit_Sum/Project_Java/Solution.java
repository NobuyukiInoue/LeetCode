import java.util.*;

public class Solution {
    public int countEven(int num) {
        // 0ms
        int k = num, total = 0;
        num -= num%10;
        while (num > 0) {
            total += num%10;
            num /= 10;
        }
        if (total%2 == 0) {
            return k/2;
        }
        return (k + 1)/2 - 1;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = countEven(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
