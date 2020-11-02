import java.util.*;

public class Solution {

    public int[][] updateMatrix(int[][] matrix) {
        // 4ms
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = matrix;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (matrix[i][j] == 1)
                    dp[i][j] = Integer.MAX_VALUE - 1;

        for (int i = 1; i < m; i++)
            dp[i][0] = Math.min(dp[i][0], dp[i - 1][0] + 1);
        for (int i = 1; i < n; i++)
            dp[0][i] = Math.min(dp[0][i], dp[0][i - 1] + 1);

        for (int i = 1; i < m; i++)
            for (int j = 1; j < n; j++)
                dp[i][j] = Math.min(dp[i][j], Math.min(dp[i][j - 1], dp[i - 1][j]) + 1);

        for (int i = m - 2; i >= 0; i--)
            dp[i][n - 1] = Math.min(dp[i + 1][n - 1] + 1, dp[i][n - 1]);
        for (int i = n - 2; i >= 0; i--)
            dp[m - 1][i] = Math.min(dp[m - 1][i + 1] + 1, dp[m - 1][i]);

        for (int i = m - 2; i >= 0; i--)
            for (int j = n - 2; j >= 0; j--)
                dp[i][j] = Math.min(dp[i][j], Math.min(dp[i][j + 1], dp[i + 1][j]) + 1);

        return dp;
    }

    public int[][] updateMatrix_bug(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m][];

        for (int i = 0; i < m; i++) {
            dp[i] = new int[n];
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != 0) {
                    if (i == 0 && j == 0) {
                        dp[i][j] = Integer.MAX_VALUE - 1;
                    } else if (i == 0) {
                        dp[i][j] = matrix[i][j - 1] + 1;
                    } else if (j == 0) {
                        dp[i][j] = matrix[i - 1][j] + 1;
                    } else {
                        dp[i][j] = Math.min(matrix[i - 1][j], matrix[i][j - 1]) + 1;
                    }
                }
            }
        }

        for (int x = m - 1; x >= 0; x--) {
            for (int y = n - 1; y >= 0; y--) {
                if (matrix[x][y] != 0) {
                    if (x == m - 1 && y == n - 1) {
                        matrix[x][y] = dp[x][y];
                    } else if (x == m - 1) {
                        matrix[x][y] = Math.min(dp[x][y], 1 + matrix[x][y + 1]);
                    } else if (y == n - 1) {
                        matrix[x][y] = Math.min(dp[x][y], 1 + matrix[x + 1][y]);
                    } else {
                        matrix[x][y] = Math.min(dp[x][y], 1 + Math.min(matrix[x + 1][y], matrix[x][y + 1]));
                    }
                }
            }
        }
        return matrix;
    }

    public String matrixToString(int[][] list) {
        if (list.length <= 0)
            return "[]";

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[\n  " + ml.intArrayToString(list[0]) + "\n");
        for (int i = 1; i < list.length; i++) {
            sb.append(" ," + ml.intArrayToString(list[i]) + "\n") ;
        }

        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_matrix = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] matrix = new int[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
            matrix[i] = ml.stringTointArray(str_matrix[i]);
        }

        System.out.println("matrix = " + matrixToString(matrix));

        long start = System.currentTimeMillis();

        int[][] result = updateMatrix(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + matrixToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
