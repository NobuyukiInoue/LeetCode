import java.util.*;

public class Solution {
    public int returnToBoundaryCount(int[] nums) {
        // 0ms
        int ans = 0, pos = 0;
        for (int num : nums) {
            pos += num;
            if (pos == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = returnToBoundaryCount(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
