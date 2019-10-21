import java.util.*;

public class Solution {
    public int maximalSquare(char[][] matrix) {
        // 4ms
        if (matrix.length == 0)
            return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int result = 0;
        int[][] areas = new int[m + 1][n + 1];
        for (int i = 1 ; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    areas[i][j] = Math.min(Math.min(areas[i][j - 1] , areas[i - 1][j - 1]), areas[i - 1][j]) + 1;
                    result = Math.max(areas[i][j], result);
                }
            }
        }
        return result*result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\",\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        char[][] matrix = new char[flds.length][];
        for (int i = 0; i < flds.length; i++) {
            matrix[i] = flds[i].toCharArray();
        }

        System.out.println("matrix = [");
        for (int i = 0; i < matrix.length; i++) {
            if (i == 0)
                System.out.println(" [" + new String(matrix[i]) + "]");
            else
                System.out.println(",[" + new String(matrix[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = maximalSquare(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
