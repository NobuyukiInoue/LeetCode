import java.util.*;

public class Solution {
    public int maxArea(int[] height) {
        int leftHigh = 0;
        int rightHigh = height.length - 1;
        int maxArea = 0;

        while (leftHigh < rightHigh) {
            if (height[leftHigh] < height[rightHigh]) {
                int curArea = height[leftHigh] *(rightHigh - leftHigh);
                if (curArea > maxArea) {
                    maxArea = curArea;
                }
                leftHigh++;
            } else {
                int curArea = height[rightHigh] *(rightHigh - leftHigh);
                if (curArea > maxArea) {
                    maxArea = curArea;
                }
                rightHigh--;
            }
        }

        return maxArea;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] height = ml.stringTointArray(flds);
        System.out.println("height = " + ml.intArrayToString(height));

        long start = System.currentTimeMillis();

        int result = maxArea(height);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
