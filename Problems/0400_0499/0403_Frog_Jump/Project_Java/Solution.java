import java.util.*;

public class Solution {
    public boolean canCross(int[] stones) {
        // 3ms
        int step = 1;
        for (int i = 0; i < stones.length - 1; i++) {
            if (stones[i + 1] - stones[i] > step)
                return false;
            step++;
        }

        return helper(stones, 1, stones[stones.length - 1], 1);
    }

    private boolean helper(int[] stones, int start, int end, int step) {
        if (start == end)
            return true;
        if (!contains(stones, start))
            return false;
        if (helper(stones, start + step + 1, end, step + 1))
            return true;
        if (helper(stones, start + step, end, step))
            return true;
        if (step > 1 && helper(stones, start + step - 1, end, step - 1))
            return true;
        return false;
    }

    private boolean contains(int[] nums, int target) {
        for (int n : nums)
            if (n == target)
                return true;
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] stones = ml.stringTointArray(flds);
        System.out.println("stones = " + ml.intArrayToString(stones));

        long start = System.currentTimeMillis();
        
        boolean result = canCross(stones);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
