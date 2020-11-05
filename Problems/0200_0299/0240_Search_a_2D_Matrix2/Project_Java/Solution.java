import java.util.*;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 5ms
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;
        int n = matrix.length, m = matrix[0].length;
        int i = 0, j = m - 1;
        while (i < n && j >= 0) {
            int num = matrix[i][j];
            
            if (num == target)
                return true;
            else if (num > target)
                j--;
            else
                i++;
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.trim().split("\\]\\],\\[");

        flds[0] = flds[0].replace("[[[", "");
    //  System.out.println("flds[0] = " + flds[0] + ", flds[0].length = " + Integer.toString(flds[0].length()));

        int[][] matrix;
        if (flds[0].length() > 0) {
            Mylib ml = new Mylib();
            String[] dataStr = flds[0].split("\\],\\[");
            matrix = ml.stringToIntIntArray(dataStr);
            System.out.println("matrix = " + ml.matrixToString(matrix));
        } else {
            matrix = new int[0][0];
            System.out.println("matrix = [[]]");
        }

        int target = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        boolean result = searchMatrix(matrix, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
