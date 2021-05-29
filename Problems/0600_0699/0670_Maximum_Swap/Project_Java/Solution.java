import java.util.*;

public class Solution {
    public int maximumSwap(int num) {
        // 0ms
        int max = 0;
        for (int p = 1; p <= num; p *= 10) {
            for (int q = p; q <= num; q *= 10) {
                max = Math.max(max, num + num/p%10*(q - p) + num/q%10*(p - q));
            }
        }
        return max;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = maximumSwap(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
