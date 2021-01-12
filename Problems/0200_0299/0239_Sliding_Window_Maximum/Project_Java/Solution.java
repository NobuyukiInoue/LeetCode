import java.util.*;

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // 27ms
        ArrayDeque<Integer> q = new ArrayDeque<>();
        int[] res = new int[nums.length - k + 1];
        int pos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i - k >= 0) {
                res[pos++] = nums[q.getLast()];
                while (!q.isEmpty() && q.getLast() <= i - k) {
                    q.pollLast();
                }
            }
            while (!q.isEmpty() && nums[i] > nums[q.getFirst()]) {
                q.pop();
            }
            q.push(i);
        }
        res[pos] = nums[q.getLast()];
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);

        long start = System.currentTimeMillis();

        int[] result = maxSlidingWindow(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
