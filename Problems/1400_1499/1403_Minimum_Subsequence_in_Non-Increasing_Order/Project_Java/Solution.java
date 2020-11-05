import java.util.*;

public class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        // 3ms
        Arrays.sort(nums);

        int n = nums.length;
        int ans = 0, sum = 0;
        List<Integer> res = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            sum += nums[i];
        }

        for(int i = n - 1; i >= 0; i--) {
            ans += nums[i];
            res.add(nums[i]);
            if (ans > sum - ans)
                return res;
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

        List<Integer> result = minSubsequence(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
