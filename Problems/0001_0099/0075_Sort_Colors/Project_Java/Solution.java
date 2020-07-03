import java.util.*;

public class Solution {
    public void sortColors(int[] nums) {
        // 0ms
        int red = 0, white = 0, blue = 0;
        for (int n : nums) {
            if (n == 0)
                red++;
            else if (n == 1)
                white++;
            else
                blue++;
        }

        int i = 0;
        int j;
        for (j = 0; j < red; j++)
            nums[i++] = 0;
        for (j = 0; j < white; j++)
            nums[i++] = 1;
        for (j = 0; j < blue; j++)
            nums[i++] = 2;
   }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        sortColors(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(nums));
        System.out.println((end - start)  + "ms\n");
    }
}
