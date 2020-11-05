import java.util.*;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 0ms
        if (matrix == null || matrix[0] == null) {
            return false;
        }
        if (matrix.length <= 0 || matrix[0].length <= 0) {
            return false;
        }
        if (matrix[0][0] == target) {
            return true;
        }
        for (int i = 0; i < matrix.length;) {
            if (i + 1 < matrix.length) {
                if (matrix[i + 1][0] == target) {
                    return true;
                } else if (matrix[i + 1][0] < target) {
                    i++;
                    continue;
                }
            }
            if (matrix[i][0] == target) {
                return true;
            } else if (matrix[i][0] < target) {
                for (int j = 1; j < matrix[i].length; j++) {
                    if (matrix[i][j] == target) {
                        return true;
                    } else if (matrix[i][j] > target) {
                        return false;
                    }
                }
            }
            return false;
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]],\\[");
        String[] str_matrix = flds[0].split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(str_matrix);
        System.out.println("matrix = \n" + ml.matrixToString(matrix));

        int target = Integer.parseInt(flds[1].replace("]]",""));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        boolean result = searchMatrix(matrix, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
