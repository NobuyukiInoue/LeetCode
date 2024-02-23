import java.util.*;

public class Solution {
    public int[][] modifiedMatrix(int[][] matrix) {
        // 1ms
        int n = Math.max(matrix.length, matrix[0].length);
        int[] max_col = new int[n];
        for (int[] row : matrix) {
            for (int j = 0; j < row.length; j++) {
                max_col[j] = Math.max(max_col[j], row[j]);
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == -1) {
                    matrix[i][j] = max_col[j];
                }
            }
        }
        return matrix;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("matrix = " + ml.intIntArrayToString(matrix));

        long start = System.currentTimeMillis();

        int[][] result = modifiedMatrix(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
