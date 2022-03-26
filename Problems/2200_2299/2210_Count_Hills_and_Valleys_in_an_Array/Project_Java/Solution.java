import java.util.*;

public class Solution {
    public int countHillValley(int[] nums) {
        // 1ms
        int i = 0, res = 0;
        Boolean dirrection = true;
        while (i < nums.length - 1) {
            if (nums[i] == nums[i + 1]) {
                i++;
                continue;
            }
            dirrection = (nums[i] < nums[i + 1]);
            i++;
            break;
        }
        while (i < nums.length - 1) {
            if (dirrection) {
                if (nums[i] > nums[i + 1]) {
                    dirrection = false;
                    res++;
                }
            } else {
                if (nums[i] < nums[i + 1]) {
                    dirrection = true;
                    res++;
                }
            }
            i++;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = countHillValley(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
