import java.lang.reflect.Array;
import java.util.*;

public class Solution {
    public int[] separateDigits(int[] nums) {
        // 7ms
        List<Integer> ans = new ArrayList<>();
        for (int num : nums) {
            String s_num = Integer.toString(num);
            for (char ch : s_num.toCharArray()) {
                ans.add(ch - '0');
            }
        }
        return ans.stream().mapToInt(i->i).toArray();
    }

    public int[] separateDigits_fast(int[] nums) {
        // 3ms
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = nums.length - 1; i >= 0; i--) {
            while (nums[i] != 0) {
                int rem = nums[i]%10;
                ans.add(rem);
                nums[i] = nums[i]/10;
            }
        }
        int arr[] = new int[ans.size()];
        int k = 0;
        for(int i = ans.size() - 1; i >= 0; i--) {
            arr[k++] = ans.get(i);
        }
        return arr;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = separateDigits(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
