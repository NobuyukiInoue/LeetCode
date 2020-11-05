import java.util.*;

public class Solution {
    public int[] frequencySort(int[] nums) {
        // 0ms
        Map<Integer, Integer> map = new HashMap<>(); // count the number of occurence..
        for (int i=0; i<nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> (a.getValue() == b.getValue() ? b.getKey() - a.getKey() : a.getValue() - b.getValue()));
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            pq.offer(e);
        }
        int index = 0;
        int[] res = new int[nums.length];
        while (!pq.isEmpty()) {
            Map.Entry<Integer, Integer> e = pq.poll();
            for (int i = index; i < index + e.getValue(); i++) {
                res[i] = e.getKey();
            }
            index += e.getValue();
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = frequencySort(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
