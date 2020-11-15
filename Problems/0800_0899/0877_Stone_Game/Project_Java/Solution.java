import java.util.*;

public class Solution {
    public boolean stoneGame(int[] piles) {
        // 0ms
        if (piles.length % 2 == 0)
            return true;
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] piles = ml.stringToIntArray(flds);
        System.out.println("piles = " + ml.intArrayToString(piles));

        long start = System.currentTimeMillis();

        boolean result = stoneGame(piles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
