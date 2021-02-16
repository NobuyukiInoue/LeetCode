import java.util.*;

public class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        // 1ms
        int maxLen = 0;
        int numSquares = 0;

        for (int[] arr : rectangles) {
            int curLen = Math.min(arr[0], arr[1]);

            if (curLen == maxLen) {
                ++numSquares;
            } else if (curLen > maxLen) {
                maxLen = curLen;
                numSquares = 1;
            } else {
                // do nothing
            }
        }

        return numSquares;
    }

    public int countGoodRectangles2(int[][] rectangles) {
        // 1ms
        int maxLen = 0;
        int[] mins = new int[rectangles.length];

        for (int i = 0; i < rectangles.length; i++) {
            mins[i] = Math.min(rectangles[i][0], rectangles[i][1]);
            maxLen = Math.max(maxLen, mins[i]);
        }

        int res = 0;
        for (int i = 0; i < mins.length; i++) {
            if (maxLen == mins[i]) {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[[", "").replace("]]", "").replace(", ", ",").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] rectangles = ml.stringToIntIntArray(flds);
        System.out.println("rectangles = " + ml.intIntArrayToString(rectangles));

        long start = System.currentTimeMillis();

        int result = countGoodRectangles(rectangles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
