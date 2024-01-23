import java.util.*;

public class Solution {
    public int matrixSum(int[][] nums) {
        // 13ms
        for (int i = 0; i < nums.length; i++) {
            Arrays.sort(nums[i]);
        }
        int ans = 0;
        for (int col = 0; col < nums[0].length; col++) {
            int col_max = nums[0][col];
            for (int i = 1; i < nums.length; i++) {
                col_max = Math.max(col_max, nums[i][col]);
            }
            ans += col_max;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] nums = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("nums = " + ml.intIntArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = matrixSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
