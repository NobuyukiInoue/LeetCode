import java.util.*;

public class Solution {
    public int[] productExceptSelf(int[] nums) {
        // 2ms
        int numsLength = nums.length;
        int[] res = new int[numsLength];
        int[] postfix = new int [numsLength];

        res[0] = 1;
        postfix[numsLength - 1] = 1;

        for (int i = 1; i < numsLength; i++) {
            res[i] = res[i - 1]*nums[i - 1];
        }

        for (int i = numsLength-2; i >= 0; i--) {
            postfix[i] = postfix[i + 1]*nums[i + 1];
        }

        for (int i = 0; i < numsLength; i++) {
            res[i] = res[i]*postfix[i];
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = productExceptSelf(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
