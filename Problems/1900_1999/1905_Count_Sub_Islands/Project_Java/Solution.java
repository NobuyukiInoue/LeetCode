import java.util.*;

public class Solution {
    // 30ms
    int R, C;
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        R = grid1.length;
        C = grid1[0].length;
        int ans = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid2[i][j] == 1) {
                    if (dfs(grid1, grid2, i, j)) {
                        ans++;
                    }
                }
            }
        }
        return ans;
    }

    private boolean dfs(int[][] grid1, int[][] grid2, int i, int j) {
        boolean isSubIsland = true;
        if (0 <= i && i < R && 0 <= j && j < C && grid2[i][j] == 1) {
            if (grid1[i][j] != 1) {
                return false;
            }
            grid2[i][j] = -1;
            int[][] dirrections = new int[][] {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
            for (int[] d : dirrections) {
                isSubIsland &= dfs(grid1, grid2, i + d[0], j + d[1]);
            }
        }
        return isSubIsland;
    }

    public String gridToString(int[][] matrix) {
        if (matrix == null)
            return "[]";
        if (matrix.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[\n");
        Mylib ml = new Mylib();
        sb.append("  " + ml.intArrayToString(matrix[0]) + "\n");
        for (int i = 1; i < matrix.length; i++) {
            sb.append(", " + ml.intArrayToString(matrix[i]) + "\n");
        }

        return sb.append("]").toString();
   }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        Mylib ml = new Mylib();
        int[][] grid1 = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int[][] grid2 = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("grid1 = \n" + gridToString(grid1));
        System.out.println("grid2 = \n" + gridToString(grid2));

        long start = System.currentTimeMillis();

        int result = countSubIslands(grid1, grid2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
