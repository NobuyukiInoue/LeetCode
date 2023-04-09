import java.util.*;

public class Solution {
    public int[] evenOddBit(int n) {
        // 1ms
        int[] ans = new int[] {0, 0};
        boolean odd = false;
        while (n > 0) {
            if (odd == false) {
                if ((n & 1) == 1) {
                    ans[0]++;
                }
                odd = true;
            } else {
                if ((n & 1) == 1) {
                    ans[1]++;
                }
                odd = false;
            }
            n >>= 1;
        }
        return ans;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        int[] result = evenOddBit(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
