import java.util.*;

public class Solution {
    public int largestRectangleArea(int[] heights) {
        // 7ms
        int maxArea = 0;
        List<int[]> stack = new ArrayList<>();

        for (int i = 0; i < heights.length; i++) {
            int start = i;

            while (stack.size() > 0 && stack.get(stack.size() - 1)[1] > heights[i]) {
                int height = stack.get(stack.size() - 1)[1];
                int width = i - stack.get(stack.size() - 1)[0];
                maxArea = Math.max(maxArea, height*width);
                start = stack.get(stack.size() - 1)[0];
                stack.remove(stack.size() - 1);
            }
            stack.add(new int[] {start, heights[i]});
        }

        for (int i = 0; i < stack.size(); i++) {
            int height = stack.get(i)[1], start = stack.get(i)[0];
            int area = height * (heights.length - start);
            maxArea = Math.max(area, maxArea);
        }

        return maxArea;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] heights = ml.stringToIntArray(flds);
        System.out.println("heights = " + ml.intArrayToString(heights));

        long start = System.currentTimeMillis();

        int result = largestRectangleArea(heights);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
