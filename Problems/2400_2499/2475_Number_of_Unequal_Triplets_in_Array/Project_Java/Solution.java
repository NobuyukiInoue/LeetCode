import java.util.*;

public class Solution {
    public int unequalTriplets(int[] nums) {
        // 1ms
        int trips = 0, pairs = 0;
        int[] cnts = new int[1001];
        for (int i = 0; i < nums.length; i++) {
            trips += pairs - cnts[nums[i]] * (i - cnts[nums[i]]);
            pairs += i - cnts[nums[i]];
            cnts[nums[i]]++;
        }
        return trips;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = unequalTriplets(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
