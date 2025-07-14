import java.util.*;

public class Solution {
    public int minimumOperations(int[] nums) {
        // 2ms
        List<Integer> cnts = new ArrayList<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (cnts.contains(nums[i])) {
                return i/3 + 1;
            }
            cnts.add(nums[i]);
        }
        return 0;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minimumOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
