import java.util.*;

public class Solution {
    public long continuousSubarrays(int[] nums) {
        // 85ms - 88ms
        int i = 0;
        long ans = 0;
        HashMap<Integer, Integer> dic = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            HashMap<Integer, Integer> temp = new HashMap<>(dic);
            for (int k : temp.keySet()) {
                if (Math.abs(k - nums[j]) > 2) {
                    i = Math.max(i, temp.get(k) + 1);
                    dic.remove(k);
                }
            }
            dic.put(nums[j], j);
            ans += j - i + 1;
        }
        return ans;
    }

    public long continuousSubarrays2(int[] nums) {
        // 61ms - 63ms
        int n = nums.length;
        Map<Integer, Integer> countMap = new HashMap<>();
        int j = 0;
        long count = 0;
        for (int i = 0; i < n; i++) {
            countMap.put(nums[i], 1 + countMap.getOrDefault(nums[i], 0));
            while (i - j + 1 > getCount(nums[i], countMap)) {
                countMap.put(nums[j], countMap.get(nums[j]) - 1);
                j++;
            }
            count += i-j+1;
        }
        return count;
    }

    private int getCount(int num, Map<Integer, Integer> countMap) {
        return countMap.getOrDefault(num, 0) + countMap.getOrDefault(num - 1, 0) + countMap.getOrDefault(num + 1, 0) + countMap.getOrDefault(num-2, 0) + countMap.getOrDefault(num+2, 0);
    }

    public long continuousSubarrays3(int[] nums) {
        // 225ms - 227ms
        long ans = 0;
        int start = 0, end = 0;
        PriorityQueue<Integer> min = new PriorityQueue<>();
        PriorityQueue<Integer> max = new PriorityQueue<>((a, b) -> b - a);
        while (end < nums.length) {
            max.offer(nums[end]);
            min.offer(nums[end]);
            while (max.peek() - min.peek() > 2) {
                max.remove(nums[start]);
                min.remove(nums[start]);
                start++;
            }
            ans += end-start + 1;
            end++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        long result = continuousSubarrays(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
