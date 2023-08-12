import java.util.*;

public class Solution {
    public int lastStoneWeightII(int[] stones) {
        // 1ms
        int n = stones.length;
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }
        boolean[] dp = new boolean[sum/2 + 1];
        dp[0] = true;
        for (int i = 0; i < n; i++) {
            int stone = stones[i];
            for (int j = sum/2; j >= stone; j--) {
                if (dp[j - stone]) {
                    dp[j] = true;
                }
            }
        }
        int i = sum/2;
        while (i >= 0 && !dp[i]) {
            i--;
        }
        return sum - 2*i;
    }

    public int lastStoneWeightII2(int[] stones) {
        // 15ms
        Set<Integer> set = new HashSet<>();
        set.add(stones[0]);
        set.add(-stones[0]);
        for (int i = 1; i < stones.length; i++) {
            Set<Integer> set2 = new HashSet<>();
            for (int item : set) {
                set2.add(item + stones[i]);
                set2.add(item - stones[i]);
            }
            set = set2;
        }
        int min = Integer.MAX_VALUE;
        for (int item : set) {
            min = Math.min(Math.abs(item), min);
        }
        return min;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] stones = ml.stringToIntArray(flds);
        System.out.println("stones = " + ml.intArrayToString(stones));

        long start = System.currentTimeMillis();

        int result = lastStoneWeightII(stones);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
