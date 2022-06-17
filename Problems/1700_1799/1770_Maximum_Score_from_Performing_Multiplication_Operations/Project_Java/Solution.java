import java.util.*;

public class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        // 42ms - 54ms
        int n = nums.length;
        int m = multipliers.length;
        int[] first = new int[n];
        int[] second = new int[n];
        for (int i = 0; i < n; i++) {
            if (n - 1 < m) {
                first[i] = nums[i] * multipliers[(n-1)];
            } else {
                first[i] = 0;
            }
        }
        for (int l = 2; l <= n ; l++) {
            for (int i = 0; i + l - 1< n && (n - l < m); i++) {
                int j = i + l - 1;
                if (n - l < m) {
                    second[i] = Math.max(first[i + 1] + multipliers[n - l]*nums[i], first[i] + multipliers[n - l]*nums[j]);
                } else {
                    second[i] = Math.max(first[i + 1], first[i]);
                }
            }
            first = second;
        }
        return first[0];
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] arr = ml.stringToIntIntArray(str_mat);
        int[] nums = arr[0], multipliers = arr[1];
        System.out.println("nums = " + ml.intArrayToString(nums) + ", multipliers = " + ml.intArrayToString(multipliers));

        long start = System.currentTimeMillis();

        int result = maximumScore(nums, multipliers);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
