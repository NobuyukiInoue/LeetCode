import java.util.*;

public class Solution {
    public int binaryGap(int N) {
        int res = 0;
        for (int d = -32; N > 0; N /= 2, d++)
            if (N % 2 == 1) {
                res = Math.max(res, d);
                d = 0;
            }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int N = Integer.parseInt(flds);
        System.out.println("target = " + Integer.toString(N));

        long start = System.currentTimeMillis();
        
        int result = binaryGap(N);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
