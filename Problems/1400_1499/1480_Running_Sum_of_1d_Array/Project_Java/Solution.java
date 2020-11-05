import java.util.*;

public class Solution {
    public int[] runningSum(int[] nums) {
        // 0ms
        int[] res = new int[nums.length];
        res[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            res[i] = res[i - 1] + nums[i];
        }
        return res;
    }

    public List<Integer> minSubsequence2(int[] nums) {
        // 4ms
        List<Integer> res = new ArrayList<>();
        var pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        int sub_sum = 0, total_sum = 0;
        for (var n : nums) {
            pq.offer(n);
            total_sum += n;
        }
        while (sub_sum <= total_sum / 2) {
            res.add(pq.peek());
            sub_sum += pq.poll();
        }    
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = runningSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
