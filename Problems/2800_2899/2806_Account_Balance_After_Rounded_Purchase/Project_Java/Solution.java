import java.util.*;

public class Solution {
    public int accountBalanceAfterPurchase(int purchaseAmount) {
        // 0ms
        return 100 - ((purchaseAmount + 5)/10)*10;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int purchaseAmount = Integer.parseInt(fld);
        System.out.println("purchaseAmount = " + purchaseAmount);

        long start = System.currentTimeMillis();

        int result = accountBalanceAfterPurchase(purchaseAmount);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
