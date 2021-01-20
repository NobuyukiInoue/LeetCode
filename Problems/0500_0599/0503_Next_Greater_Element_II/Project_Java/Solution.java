import java.util.*;

public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        // 7ms
        int numsLen = nums.length;
        int[] res = new int[numsLen];
        Arrays.fill(res, -1);

        Stack<Integer> stack = new Stack<>();
        for (int i = numsLen - 1; i >= 0; i--)
            stack.push(nums[i]);

        for (int i = numsLen - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i])
                stack.pop();
            if (!stack.isEmpty())
                res[i] = stack.peek();
            stack.push(nums[i]);
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = nextGreaterElements(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
