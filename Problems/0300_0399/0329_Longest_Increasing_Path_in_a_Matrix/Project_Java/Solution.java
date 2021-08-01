import java.util.*;

public class Solution {
    // 8ms
    public static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0)
            return 0;
        int m = matrix.length, n = matrix[0].length;
        int[][] cache = new int[m][n];
        int max = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int len = dfs(matrix, i, j, m, n, cache);
                max = Math.max(max, len);
            }
        }   
        return max;
    }
    
    public int dfs(int[][] matrix, int i, int j, int m, int n, int[][] cache) {
        if (cache[i][j] != 0)
            return cache[i][j];
        int max = 1;
        for (int[] dir: dirs) {
            int x = i + dir[0], y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] <= matrix[i][j])
                continue;
            int len = 1 + dfs(matrix, x, y, m, n, cache);
            max = Math.max(max, len);
        }
        cache[i][j] = max;
        return max;
    }

/*
    // Time Limit Exceeded.
    private int max_count;

    public int longestIncreasingPath(int[][] matrix) {
        max_count = 0;

        Boolean[][] check = new Boolean[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                check[i][j] = false;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                dfs(matrix, check, i, j, -1, 0);
            }
        }
        return max_count;
    }

    private void dfs(int[][] matrix, Boolean[][] check, int i, int j, int v, int count) {
        if (i < 0 || i >= matrix.length)
            return;
        if (j < 0 || j >= matrix[i].length)
            return;
        if (check[i][j] || matrix[i][j] <= v)
            return;
        check[i][j] = true;
        max_count = Math.max(max_count, count + 1);
        dfs(matrix, check, i - 1, j, matrix[i][j], count + 1);
        dfs(matrix, check, i + 1, j, matrix[i][j], count + 1);
        dfs(matrix, check, i, j - 1, matrix[i][j], count + 1);
        dfs(matrix, check, i, j + 1, matrix[i][j], count + 1);
        check[i][j] = false;
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds);
        System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        int result = longestIncreasingPath(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
