import java.util.*;

public class Solution {
    public int countValidSelections(int[] nums) {
        // 1ms
        int left = 0, right = 0, index = 0;
        for (int i = 0; i < nums.length; i++) {
            left += nums[i];
            if (nums[i] == 0) {
                index = i;
                break;
            }
        }
        for (int i = index; i < nums.length; i++) {
            right += nums[i];
        }
        int count = 0;
        for (int i = index; i < nums.length; i++) {
            left += nums[i];
            right -= nums[i]; 
            if (nums[i] != 0) {
                continue;
            }
            if (left == right) {
                count += 2;
            } else if (left - 1 == right || left + 1 == right) {
                count++;
            }
        }
        return count;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countValidSelections(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
