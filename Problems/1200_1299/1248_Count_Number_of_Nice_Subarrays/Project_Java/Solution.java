import java.util.*;

public class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        // 12ms
        int count = 0, res = 0, l = 0;
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            if ((nums[i] & 1) == 1) {
                queue.add(i);
                count = 0;
            }
            while (queue.size() == k) {
                while (l++ != queue.peek()){
                  count++;
                }
                count++;
                queue.poll();
            }
            res = count + res;
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = numberOfSubarrays(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
