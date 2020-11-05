import java.util.*;

public class Solution {
    public int[][] generateMatrix(int n) {
        // 0ms
        int[][] result = new int[n][n];

        if (n == 0)
            return result;

        int top = 0;
        int left = 0;
        int right = n - 1;
        int bottom = n - 1;
        int count = 1;

        while (top <= bottom && left <= right) {
            for (int col = left; col <= right; col++)
                result[top][col] = count++;
            top++;

            for (int row = top; row <= bottom; row++)
                result[row][right] = count++;
            right--;

            if (top > bottom)
                break;
            for (int col = right; col >= left; col--)
                result[bottom][col] = count++;
            bottom--;

            if (left > right)
                break;
            for (int row = bottom; row >= top; row--)
                result[row][left] = count++;
            left++;
        }

        return result;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int[][] result = generateMatrix(n);

        long end = System.currentTimeMillis();

    	Mylib ml = new Mylib();
        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
