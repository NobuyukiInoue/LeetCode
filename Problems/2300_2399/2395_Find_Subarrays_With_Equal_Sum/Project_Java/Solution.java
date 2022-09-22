import java.util.*;

public class Solution {
    public boolean findSubarrays(int[] nums) {
        // 2ms
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length - 1; i++) {
            int t = nums[i] + nums[i + 1];
            if (hm.containsKey(t)) {
                return true;
            }
            hm.put(t, 1);
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = findSubarrays(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
