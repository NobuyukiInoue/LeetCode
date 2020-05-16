import java.util.*;

public class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        // 13ms
        if (maxChoosableInteger > desiredTotal)
            return true;
        if ((maxChoosableInteger*(maxChoosableInteger + 1)) >> 1 < desiredTotal)
            return false;
        return helper(0, maxChoosableInteger, desiredTotal, new int[1 << maxChoosableInteger]);
    }

    private boolean helper(int bits, int maxChoosableInteger, int desiredTotal, int[] dp) {
        if (dp[bits] != 0)
            return dp[bits] == 1;
        for (int i = 0; i < maxChoosableInteger; i++) {
            if (((bits >> i) & 1) == 0 && (i + 1 >= desiredTotal || !helper(bits | (1 << i), maxChoosableInteger, desiredTotal - i - 1, dp))) {
                dp[bits] = 1;
                return true;
            }
        }

        dp[bits] = -1;
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        int maxChoosableInteger = Integer.parseInt(flds[0]);
        int desiredTotal = Integer.parseInt(flds[1]);

        System.out.println("maxChoosableInteger = " + Integer.toString(maxChoosableInteger) + ", desireTotal = " + Integer.toString(desiredTotal));

        long start = System.currentTimeMillis();
        
        boolean result = canIWin(maxChoosableInteger, desiredTotal);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
