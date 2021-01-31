import java.util.*;

public class Solution {
    // 3ms
    private Integer[][][] memo;
    private int mod = (int) 1e9 + 7;
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; 

    public int findPaths(int m, int n, int N, int i, int j) {
        memo = new Integer[m][n][N + 1];
        return dfs(m, n, i, j, N) % mod;
    }

    private int dfs(int rows, int cols, int r, int c, int steps) {
        if (!inBound(rows, cols, r, c)) {
            return 1;
        }
        if (steps == 0) {
            return 0;
        }
        if (memo[r][c][steps] != null) {
            return memo[r][c][steps];
        }
        int res = 0;
        for (int[] direction : directions) {
            res = (res + dfs(rows, cols, r + direction[0], c + direction[1], steps -1)) % mod;
        }
        return memo[r][c][steps] = res;
    }

    private boolean inBound(int rows, int cols, int r, int c) {
        return r >= 0 && c >= 0 && r < rows && c < cols;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int m = Integer.parseInt(flds[0]);
        int n = Integer.parseInt(flds[1]);
        int N = Integer.parseInt(flds[2]);
        int i = Integer.parseInt(flds[3]);
        int j = Integer.parseInt(flds[4]);
        System.out.println("m = " + m + ", n = " + n + ", N = " + N + ", i = " + i + ", j = " + j);

        long start = System.currentTimeMillis();

        int result = findPaths(m, n, N, i, j);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
