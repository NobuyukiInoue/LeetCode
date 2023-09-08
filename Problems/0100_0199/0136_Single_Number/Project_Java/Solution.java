import java.util.*;

public class Solution {
    public int singleNumber(int[] nums) {
        // 1ms
        int result = 0;
        for (int num : nums) {
            result = result^num;
        }
        return result;
    }

    public int singleNumber2(int[] nums) {
        // 361ms
		int i, j;
		Boolean[] nums_checked = new Boolean[nums.length];
        for (i = 0; i < nums_checked.length; i++) {
            nums_checked[i] = false;
        }
		for (i = 0; i < nums.length; i++) {
			if (nums_checked[i])
				continue;
			for (j = i + 1; j < nums.length; j++) {
				if (nums_checked[j]) {
					continue;
                }
				if (nums[i] == nums[j]) {
					nums_checked[i] = nums_checked[j] = true;
				}
			}
		}
		for (i = 0; i < nums.length; i++) {
			if (nums_checked[i] == false) {
				return nums[i];
			}
		}
		return -1;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = singleNumber(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
