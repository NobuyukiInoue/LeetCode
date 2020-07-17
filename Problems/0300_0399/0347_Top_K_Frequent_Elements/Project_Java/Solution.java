import java.util.*;

public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 9ms
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        PriorityQueue<int[]> que = new PriorityQueue<>((a,b) -> (b[1] - a[1]));
        for(int num: map.keySet()){
            que.add(new int[]{num, map.get(num)});
        }
        
        int[] res = new int[k];
        int index = 0;
        while (k-- > 0) {
            res[index++] = que.poll()[0];
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums = mc.stringTointArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + mc.intArrayToString(nums) + ", k = " + String.valueOf(k));

        long start = System.currentTimeMillis();
        
        int[] result = topKFrequent(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
