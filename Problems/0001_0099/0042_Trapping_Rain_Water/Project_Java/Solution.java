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

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] height = ml.stringTointArray(flds);
        System.out.println("height = " + Int_array_to_String(height));

        long start = System.currentTimeMillis();
        
        int result = trap(height);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
