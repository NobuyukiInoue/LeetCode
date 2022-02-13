import java.util.*;

public class Solution {
    public int findFinalValue(int[] nums, int original) {
        // 5ms
		Set<Integer> h_nums = new HashSet<>();
		for (int num: nums) {
			h_nums.add(num);
		}
        while (h_nums.contains(original)) {
            original *= 2;
        }
        return original;
    }

    public int findFinalValue_with_array1000(int[] nums, int original) {
        // 0ms
        int [] store = new int[1001];
        for (int i = 0; i < nums.length; i++) {
            store[nums[i]]++;
        }
        int ans = original;
        while (store[ans] >= 1) {
            store[ans] = 0;
            ans *= 2;
            if (ans > 1000) {
                break;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int original = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", original = " + Integer.toString(original));

        long start = System.currentTimeMillis();

        int result = findFinalValue(nums, original);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
