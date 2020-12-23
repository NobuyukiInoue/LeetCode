import java.util.*;

public class Solution {
    public int deleteAndEarn(int[] nums) {
        // 2ms
        int[] dp = new int[10001];
        for (int num:nums)
            dp[num] += num;
        for (int i= 2 ; i < dp.length; i++)
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + dp[i]);
        return dp[dp.length - 1];
    }


    public int deleteAndEarn2(int[] nums) {
        // 1ms
        if (nums.length < 1)
            return 0;
        
        int[] array = new int[10001];
        
        for (int num: nums)
            array[num] += num;
        
        int maxPoints = 0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] > 0) {
                int left = i;
                int right = left;
                while (right < array.length && array[right] > 0)
                    right++;
                maxPoints += getMax(array, left, right);
                i = right - 1;
            }
        }
        
        return maxPoints;
    }

    private int getMax(int[] array, int start, int end) {
        int length = end - start;
        
        if (length < 1)
            return 0;
        
        if (length < 2)
            return array[start];
        
        if (length < 3)
            return Math.max(array[start], array[start + 1]);
        
        int first = array[start];
        int second = array[start + 1];
        int third = first + array[start + 2];
        
        for (int i = start + 3; i < end; i++) {
            int fourth = Math.max(first, second) + array[i];
            first = second;
            second = third;
            third = fourth;
        }
        
        return Math.max(second, third);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = deleteAndEarn(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
