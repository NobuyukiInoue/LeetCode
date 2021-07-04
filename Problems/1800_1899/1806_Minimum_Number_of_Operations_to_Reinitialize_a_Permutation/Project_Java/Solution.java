import java.util.*;

public class Solution {
    public int reinitializePermutation(int n) {
        // 0ms
        int res = 0, i = 1;
        while (res == 0 || i > 1) {
            if (i < n / 2)
                i *= 2;
            else
                i = (i - n / 2) * 2 + 1;
            res++;
        }
        return res;
    }

    public int reinitializePermutation2(int n) {
        // 0ms
        int opCount = 0, i = 1;
        do {
            if (i%2 == 0) {
                i /= 2;
            } else { 
                i = (n/2) + (i - 1)/2;
            }
            opCount++;
        } while (i != 1);
        return opCount;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = reinitializePermutation(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
