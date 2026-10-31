import java.util.*;

public class Solution {
    public List<Integer> findValidElements(int[] nums) {
        // 2ms
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            boolean leftValid = true;
            boolean rightValid = true;
            for (int j = 0; j < i; j++){
                if(nums[j] >= nums[i]){
                    leftValid = false;
                    break;
                }
            }
            for (int j = i + 1; j < nums.length; j++){
                if(nums[j] >= nums[i]){
                    rightValid = false;
                    break;
                } 
            }
            if (leftValid || rightValid){
                ans.add(nums[i]);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<Integer> result = findValidElements(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
