import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                result[1] = i;
                result[0] = map.get(target - nums[i]) - 1;
                return result;
            }
            map.put(nums[i], i + 1);
        }
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums = mc.str_to_int_array(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + mc.output_int_array(nums));
        System.out.println("target = " + String.valueOf(target));

        long start = System.currentTimeMillis();
        
        int[] result = twoSum(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
