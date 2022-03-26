import java.util.*;

public class Solution {
    public int rangeSum(int[] nums, int n, int left, int right) {
        // 57ms - 100ms
        int[] sums = new int[n*(n+1) / 2];
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            int current_sum = 0;
            for (int j = i; j < nums.length; j++) {
                current_sum += nums[j];
                sums[index++] = current_sum;
            }
        }
        Arrays.sort(sums);
        long ans = 0;
        for (int i = left - 1; i < right; i++) {
            ans += sums[i];
        }
        return (int)(ans % ((int)Math.pow(10, 9) + 7));
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int n = Integer.parseInt(flds[1]);
        int left = Integer.parseInt(flds[2]);
        int right = Integer.parseInt(flds[3]);
        System.out.println("nums = " + ml.intArrayToString(nums) 
                        + ", n = " + Integer.toString(n) 
                        + ", left = " + Integer.toString(left) 
                        + ", right = " + Integer.toString(left));

        long start = System.currentTimeMillis();

        int result = rangeSum(nums, n, left, right);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
