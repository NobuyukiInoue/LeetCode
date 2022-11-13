import java.util.*;

public class Solution {
    public int[] applyOperations(int[] nums) {
        // 1ms - 5ms
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }
        int[] result = new int[nums.length];
        for (int i = 0, pos = 0; i < result.length; i++) {
            if (nums[i] != 0) {
                result[pos++] = nums[i];
            }
        }
        return result;
    }

    public int[] applyOperations_one(int[] nums) {
        // 4ms
        int temp;
        for (int i = 0, j = 0; i < nums.length; ++i){
            if (i + 1 < nums.length && nums[i] == nums[i + 1]){
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
            if (nums[i] != 0){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j++;
            }
        }   
        return nums;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = applyOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
