import java.util.*;

public class Solution {
    public int totalHammingDistance(int[] nums) {
        // 6ms - 7ms
        int ans = 0;
        for (int current_bit = 0; current_bit < 32; current_bit++) {
            int counter = 0;
            for (int num : nums) {
                counter += ((num >> current_bit) & 1);
            }     
            ans += counter*(nums.length - counter);
        }
        return ans;
    }

    public int totalHammingDistance_bad(int[] nums) {
        // Time Limit Exceeded.
        if (nums.length == 0) {
            return 0;
        }
        int current_bit = 1;
        int max_num = arrMax(nums);
        int ans = 0;
        while (current_bit <= max_num) {
            int counter = 0;
            for (int num : nums) {
                if ((num & current_bit) > 0) {
                    counter++;
                }
            }
            ans += counter*(nums.length - counter);
            current_bit <<= 1;
        }
        return ans;
    }

    private int arrMax(int[] arr) {
        int res = 0;
        for (int n : arr) {
            res += n;
        }
        return res;
    } 

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = totalHammingDistance(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
