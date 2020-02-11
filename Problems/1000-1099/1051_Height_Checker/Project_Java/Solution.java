import java.util.*;

public class Solution {
    public int heightChecker(int[] heights) {
        int[] s_heights = Arrays.copyOf(heights, heights.length);
        Arrays.sort(s_heights);
        int count = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != s_heights[i])
                count++;
        }
        
        return count;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] heights = ml.stringTointArray(flds);

        System.out.println("heights = " + ml.intArrayToString(heights));

        long start = System.currentTimeMillis();
        
        int result = heightChecker(heights);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
