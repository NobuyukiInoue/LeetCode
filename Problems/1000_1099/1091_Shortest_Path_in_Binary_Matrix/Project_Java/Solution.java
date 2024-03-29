import java.util.*;

public class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        // 24ms - 26ms
        int m = grid.length, n = grid[0].length;
        if (grid[0][0] != 0 || grid[m - 1][n - 1] != 0) {
            return -1;
        }
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> que = new ArrayDeque<>();
        visited[0][0] = true;
        que.offer(new int[] {0, 0, 1});
        while (!que.isEmpty()) {
            int[] curr = que.poll();
            int i = curr[0], j = curr[1], dist = curr[2];
            if (i == m - 1 && j == n - 1) {
                return dist;
            }
            for (int[] d : new int[][] {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}, {1, 0}, {0, 1}, {0, -1}, {-1, 0}}) {
                int ni = i + d[0], nj = j + d[1];
                if (0 <= ni && ni < m && 0 <= nj && nj < n && grid[ni][nj] == 0 && !visited[ni][nj]) {
                    visited[ni][nj] = true;
                    que.offer(new int[] {ni, nj, dist + 1});
                }
            }
        }
        return -1;
    }

    private String gridToString(int[][] grid) {
        if (grid == null)
            return "[]";
        if (grid.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + "\n");
        Mylib ml = new Mylib();
        sb.append("  " + ml.intArrayToString(grid[0]) + "\n");
        for (int i = 1; i < grid.length; i++) {
            sb.append(", " + ml.intArrayToString(grid[i]) + "\n");
        }

        return sb.append("]").toString();
   }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + gridToString(grid));

        long start = System.currentTimeMillis();

        int result = shortestPathBinaryMatrix(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
