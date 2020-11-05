import java.util.*;

public class Solution {
    public int trap(int[] height) {
        // 1ms
        int i = 0, j = height.length - 1;
        int left_max = 0, right_max = 0;
        int ans = 0;
        while (i < j) {
            left_max = Math.max(left_max, height[i]);
            right_max = Math.max(right_max, height[j]);
            if (left_max <= right_max)
                ans += left_max - height[i++];
            else
                ans += right_max - height[j--];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] height = ml.stringToIntArray(flds);
        System.out.println("height = " + ml.intArrayToString(height));

        long start = System.currentTimeMillis();
        
        int result = trap(height);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
