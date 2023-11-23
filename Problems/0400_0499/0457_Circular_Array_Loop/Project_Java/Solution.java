import java.util.*;

public class Solution {
    public boolean circularArrayLoop(int[] nums) {
        // 0ms
        boolean[] visited = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) {
                continue;
            }
            Set<Integer> dic = new HashSet<>();
            boolean forward = nums[i] >= 0 ? true : false;
            int index = i;
            while (true) {
                visited[index] = true;
                int newIndex = (index + nums[index])%nums.length;
                if (newIndex < 0) {
                    newIndex += nums.length; 
                }
                if (index == newIndex || forward != nums[newIndex] >= 0) {
                    break;
                }
                if (!dic.add(index)) {
                    return true;
                }
                index = newIndex;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = circularArrayLoop(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
