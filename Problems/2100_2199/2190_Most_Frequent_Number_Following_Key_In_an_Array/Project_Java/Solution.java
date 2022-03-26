import java.util.*;

public class Solution {
    public int mostFrequent(int[] nums, int key) {
        // 2ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        int target = 0, max_cnts = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == key) {
                int current_cnt = cnts.getOrDefault(nums[i + 1], 0) + 1;
                cnts.put(nums[i + 1], current_cnt);
                if (max_cnts < current_cnt) {
                    target = nums[i + 1];
                    max_cnts = current_cnt;
                }
            }
        }
        return target;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int key = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", key = " + Integer.toString(key));

        long start = System.currentTimeMillis();

        int result = mostFrequent(nums, key);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
