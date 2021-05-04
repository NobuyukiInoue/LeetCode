import java.util.*;

public class Solution {
    public int smallestRepunitDivByK(int K) {
        // 1ms
        if (K%2 == 0 || K%5 == 0) {
            return -1;
        }
        int num = 1, base = 1;
        while (num%K != 0) {
            num = (num*10 + 1)%K;
            base++;
        }
        return base;
    }

    public int smallestRepunitDivByK2(int K) {
        // 2ms
        if (K%2 == 0 || K%5 == 0) {
            return -1;
        }
        int r = 0;
        for (int i = 1; i <= K; i++) {
            r = (r*10 + 1)%K;
            if (r == 0) {
                return i;
            }
        }
        return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int K = Integer.parseInt(flds);
        System.out.println("K = " + Integer.toString(K));

        long start = System.currentTimeMillis();

        int result = smallestRepunitDivByK(K);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
