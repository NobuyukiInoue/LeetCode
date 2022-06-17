import java.util.*;

public class Solution {
    public int maxSumDivThree(int[] nums) {
        // 7ms
        int[] dp = new int[3];
        for (int num : nums) {
            for (int i: Arrays.copyOf(dp, dp.length)) {
                dp[(i + num) % 3] = Math.max(dp[(i + num) % 3], i + num);
            }
        }
        return dp[0];
    }

    public int maxSumDivThree2(int[] nums) {
        // 14ms - 17ms
        int total = arraySum(nums);
        Arrays.sort(nums);
        int rest = total % 3;
        if (rest == 0) {
            return total;
        }
        int a = 0, b = 0;
        for (int num : nums) {
            if (b > 0 && num > b) {
                break;
            }
            int mod = num % 3;
            if (mod != 0) {
                if (rest == mod) {
                    return total - num;
                } else {
                    if (a == 0) {
                        a = num;
                    } else if (b == 0) {
                        b = a + num;
                    }
                }
            }
        }
        return total - b;
    }

    private int arraySum(int[] nums) {
        int ret = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ret += nums[i];
        }
        return ret;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = maxSumDivThree(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
