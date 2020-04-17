import java.util.*;

public class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        // 0ms
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            list.add(index[i], nums[i]);
        }

        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            res[i] = list.get(i);
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds[0]);
        int[] index = ml.stringTointArray(flds[1]);

        System.out.println("nums = " + ml.intArrayToString(nums) + ", index = " + ml.intArrayToString(index));

        long start = System.currentTimeMillis();
        
        int[] result = createTargetArray(nums, index);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
