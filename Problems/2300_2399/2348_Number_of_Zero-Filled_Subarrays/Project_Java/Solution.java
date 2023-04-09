import java.util.*;

public class Solution {
    public long zeroFilledSubarray(int[] nums) {
        // 3ms
        long cnt = 0;
        int n = nums.length, j = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                j = i;
            } else {
                cnt += i - j;
            }
        }
        return cnt;
    }

    public long zeroFilledSubarray2(int[] nums) {
        // 5ms
        long ans = 0, cnt = 0;
        for (int num : nums) {
            if (num == 0) {
                cnt++;
            } else if (cnt > 0) {
                ans += cnt*(cnt + 1)/2;
                cnt = 0;
            }
        }
        return ans + cnt*(cnt + 1)/2;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = zeroFilledSubarray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Long.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
