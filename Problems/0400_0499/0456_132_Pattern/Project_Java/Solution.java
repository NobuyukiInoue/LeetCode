import java.util.*;

public class Solution {
    public boolean find132pattern(int[] nums) {
        // 10ms
        if (nums == null || nums.length < 3) {
            return false;
        }
        Stack<Integer> stack = new Stack<Integer>();
        int mid = Integer.MIN_VALUE, N = nums.length;
        int i;
        for (i = N - 1; i >= 0; i--) {
            if (nums[i] < mid) {
                return true;
            }
            while (!stack.isEmpty() && nums[i] > stack.peek()) { 
                mid = stack.pop();
            }
            stack.push(nums[i]);
        }
        return false;            
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = find132pattern(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
