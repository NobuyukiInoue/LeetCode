import java.util.*;

public class Solution {
    public int minCostToMoveChips(int[] chips) {
        // 0ms
        int nOdd = 0, nEven = 0;
        for (int i : chips)
            if (i % 2 == 0)
                nEven++;
            else
                nOdd++;
        return Math.min(nEven, nOdd);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] chips = ml.stringToIntArray(flds);
        System.out.println("chips = " + ml.intArrayToString(chips));

        long start = System.currentTimeMillis();

        int result = minCostToMoveChips(chips);

        long end = System.currentTimeMillis();

        System.out.print("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
