import java.util.*;

public class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        // 15ms - 16ms
        int n = nums.length;
        int res[] = new int[n - k + 1];
        for (int i = 0; i < res.length; i++) {
            int sum = 0;
            Set<Integer> set = new HashSet<>();
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int j = i; j < i + k; j++) {
                sum += nums[j];
                set.add(nums[j]);
                map.put(nums[j], map.getOrDefault(nums[j], 0) + 1);
            }
            if (set.size() < x) {
                res[i] = sum;
            } else {
                PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> {
                    if (map.get(a) == map.get(b)) {
                        return b - a;
                    }
                    return map.get(b)-map.get(a);
                });
                for (int ele : set) {
                    pq.add(ele);
                }
                int ct = x;
                while (ct-- > 0) {
                    int top = pq.remove();
                    res[i] += (top*map.get(top));
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        int x = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k + ", x = " + x);

        long start = System.currentTimeMillis();

        int[] result = findXSum(nums, k, x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
