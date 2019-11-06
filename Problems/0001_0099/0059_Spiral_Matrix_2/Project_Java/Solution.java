import java.util.*;

public class Solution {
    public int[][] generateMatrix(int n) {
        // 0ms
        int[][] result = new int[n][n];

        if (n == 0)
            return result;

        int top = 0;
        int left = 0;
        int right = n - 1;
        int bottom = n - 1;
        int count = 1;

        while (top <= bottom && left <= right) {
            for (int col = left; col <= right; col++)
                result[top][col] = count++;
            top++;

            for (int row = top; row <= bottom; row++)
                result[row][right] = count++;
            right--;

            if (top > bottom)
                break;
            for (int col = right; col >= left; col--)
                result[bottom][col] = count++;
            bottom--;

            if (left > right)
                break;
            for (int row = bottom; row >= top; row--)
                result[row][left] = count++;
            left++;
        }

        return result;
    }

    private String intIntArrayToString(int[][] nums) {
        if (nums.length <= 0)
            return "";

        StringBuilder resultStr = new StringBuilder();
        resultStr.append("[" + intArrayToString(nums[0]) + "]");
        for (int i = 1; i < nums.length; i++) {
            resultStr.append(", [" + intArrayToString(nums[i]) + "]");
        }
        return resultStr.toString();
    }

    private String intArrayToString(int[] nums) {
        if (nums.length <= 0)
            return "";
        StringBuilder resultStr = new StringBuilder();
        resultStr.append(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            resultStr.append("," + Integer.toString(nums[i]));
        }
        return resultStr.toString();
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int[][] result = generateMatrix(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
