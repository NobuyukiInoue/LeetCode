import java.util.*;

public class Solution {
    public int maxProduct(int[] nums) {
        // 0ms
        int m = Integer.MIN_VALUE, n = m;
        for (int num: nums) {
            if (num >= m) {
                n = m;
                m = num;
            } else if (num > n) {
                n = num;
            }
        } 
        return (m - 1) * (n - 1);
    }

    public int maxProduct2(int[] nums) {
        // 1ms
        Arrays.sort(nums);
        return ((nums[nums.length - 1]-1)*(nums[nums.length - 2] - 1));
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

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        int result = maxProduct(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
