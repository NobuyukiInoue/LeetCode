import java.util.*;

public class Solution {
    public int[] shuffle(int[] nums, int n) {
        // 0ms
        int[] res = new int[nums.length];
        int mid = nums.length / 2;
        for (int i = 0; i < mid; i++) {
            res[2*i] = nums[i];
            res[2*i + 1] = nums[mid + i];
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int n = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", n = " + String.valueOf(n));

        long start = System.currentTimeMillis();

        int[] result = shuffle(nums, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
