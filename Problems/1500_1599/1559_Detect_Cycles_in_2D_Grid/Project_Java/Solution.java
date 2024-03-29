import java.util.*;

public class Solution {
    // 19ms - 21ms
    int m, n;
    boolean[][] visited;
    int[][] direction = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public boolean containsCycle(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && bfs(grid, i, j, -1, -1))
                    return true;
            }
        }
        return false;
    }
    
    private boolean bfs(char[][] g, int i, int j, int x, int y) {
        char c = g[i][j];
        Queue<int[]> q = new LinkedList<>();
        visited[i][j] = true;
        q.offer(new int[]{i, j, x, y});
        while (!q.isEmpty()) {
            for (int k = 0, l = q.size(); k < l; k++) {
                int curr[] = q.poll();
                for (int[] d : direction) {
                    int ni = curr[0] + d[0], nj = curr[1] + d[1];
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n || g[ni][nj] != c)
                        continue;
                    if (ni == curr[2] && nj == curr[3])
                        continue;
                    if (visited[ni][nj])
                        return true;
                    q.offer(new int[]{ni, nj, curr[0], curr[1]});
                    visited[ni][nj] = true;
                }
            }
        }
        return false;
    }

    public char[][] stringToCharCharArray(String[] s) {
        if (s == null)
            return null;

        char[][] arr = new char[s.length][];
        for (int i = 0; i < s.length; i++) {
            arr[i] = s[i].replace(",", "").toCharArray();
        }

        return arr;
    }

    public String charGridToString(char[][] grid) {
        if (grid == null)
            return "[]";
        if (grid.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[\n [" + new String(grid[0]) + "]\n");
        for (int i = 1; i < grid.length; i++) {
            sb.append(",[" + new String(grid[i]) + "]\n") ;
        }

        return sb.append("]").toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        char[][] grid = stringToCharCharArray(flds.split("\\],\\["));
        System.out.println("grid = " + charGridToString(grid));

        long start = System.currentTimeMillis();

        boolean result = containsCycle(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
