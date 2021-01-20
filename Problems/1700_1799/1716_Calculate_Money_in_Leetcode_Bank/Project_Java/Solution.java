import java.util.*;

public class Solution {
    public int totalMoney(int n) {
        // 0ms
        int startSum = 28;
        int startMonday = 1;
        int total = 0;
        while (n > 0) {
            if (n > 7) {
                total += startSum;
            } else {
                total += startMonday;
            }
            if (n > 7) {
                n -= 7;
            } else {
                n--;
            }
            startMonday++;
            startSum += 7;
        }
        return total;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = totalMoney(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
