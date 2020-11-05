import java.util.*;

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        // 0ms
        List<Integer> result = new ArrayList<Integer>();

        if (matrix == null || matrix.length == 0)
            return result;

        int top = 0;
        int left = 0;
        int right = matrix[0].length - 1;
        int bottom = matrix.length - 1;

        while (top <= bottom && left <= right) {
            for (int col = left; col <= right; col++)
                result.add(matrix[top][col]);
            top++;

            for (int row = top; row <= bottom; row++)
                result.add(matrix[row][right]);
            right--;

            if (top > bottom)
                break;
            for (int col = right; col >= left; col--)
                result.add(matrix[bottom][col]);
            bottom--;

            if (left > right)
                break;
            for (int row = bottom; row >= top; row--)
                result.add(matrix[row][left]);
            left++;
        }

        return result;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds);
        System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        List<Integer> result = spiralOrder(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
