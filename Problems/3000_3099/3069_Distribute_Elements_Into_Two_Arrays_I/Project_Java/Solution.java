import java.util.*;

public class Solution {
    public int[] resultArray(int[] nums) {
        // 1ms
        int last1 = nums[0], last2 = nums[1];
        List<Integer> arr1 = new ArrayList<>();
        arr1.add(last1);
        List<Integer> arr2 = new ArrayList<>();
        arr2.add(last2);
        for (int i = 2; i < nums.length; i++) {
            if (last1 > last2) {
                arr1.add(nums[i]);
                last1 = nums[i];
            } else {
                arr2.add(nums[i]);
                last2 = nums[i];
            }
        }
        int[] ans = new int[nums.length];
        int pos = 0;
        for (int i = 0; i < arr1.size(); i++) {
            ans[pos++] = (int)arr1.get(i);
        }
        for (int i = 0; i < arr2.size(); i++) {
            ans[pos++] = (int)arr2.get(i);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = resultArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
