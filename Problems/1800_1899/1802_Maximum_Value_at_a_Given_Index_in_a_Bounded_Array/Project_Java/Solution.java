import java.util.*;

public class Solution {
    public int maxValue(int n, int index, int maxSum) {
        // 1ms - 2ms
        maxSum -= n;
        int left = 0 , right = maxSum;
        while (left < right) {
            int mid = (left + right + 1) / 2;
            if (test(n, index, mid) <= maxSum) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left + 1;
    }

    private long test(int n, int index, int a) {
        int b = Math.max(a - index, 0);
        long res = (long)(a + b) * (a - b + 1) / 2;
        b = Math.max(a - ((n - 1) - index), 0);
        res += (long)(a + b) * (a - b + 1) / 2;
        return res - a;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int n = nums[0], index = nums[1], maxSum = nums[2];
        System.out.println("n = " + Integer.toString(n) + ", index = " + Integer.toString(index) + ", maxSum = " + Integer.toString(maxSum));

        long start = System.currentTimeMillis();

        int result = maxValue(n, index, maxSum);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
