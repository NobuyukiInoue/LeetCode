import java.util.*;

public class Solution {
    public int maxCoins(int[] piles) {
        // 27ms
        Arrays.sort(piles);
        int ans = 0;
        for (int i = piles.length - 2; i > piles.length/3 - 1; i -= 2) {
            ans += piles[i];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] piles = ml.stringToIntArray(flds);
        System.out.println("piles = " + ml.intArrayToString(piles));

        long start = System.currentTimeMillis();

        int result = maxCoins(piles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
