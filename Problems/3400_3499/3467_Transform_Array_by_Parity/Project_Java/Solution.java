import java.util.*;

public class Solution {
    public int[] transformArray(int[] nums) {
        // 1ms
        int cnt_odd = 0, n = nums.length;
        for (int num : nums) {
            if (num%2 == 1) {
                cnt_odd++;
            }
        }
        int[] res = new int[nums.length];
        for (int i = n - cnt_odd; i < n; i++) {
            res[i] = 1;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = transformArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
