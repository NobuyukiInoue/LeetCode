import java.util.*;

public class Solution {
    public int partitionArray(int[] nums, int k) {
        // 36ms - 38ms
        Arrays.sort(nums);
        int ans = 1, start = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int diff = nums[i] - start;
            if (diff > k) {
                ans++;
                start = nums[i];
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = partitionArray(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
