import java.util.*;

public class Solution {
    public int[] numberOfPairs(int[] nums) {
        // 1ms - 2ms
        int cnts[] = new int[101];
        for(int num : nums) {
            cnts[num]++;
        }
        int pairs = 0, leftover = 0;
        for (int cnt : cnts) {
            pairs += cnt/2;
            leftover += cnt%2;
        }
        return new int[] {pairs, leftover};
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = numberOfPairs(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
