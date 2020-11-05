import java.util.*;

public class Solution {
    public int maxDistance(int[][] grid) {
        // 11ms
        int N = grid.length;
        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1)
                    queue.offer(new int[] {i, j});
            }
        }

        if (queue.size() == N*N || queue.size() == 0)
            return -1;

        int dist = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] pos = queue.poll();
                int x = pos[0], y = pos[1];
                if (x > 0 && grid[x - 1][y] == 0) {
                    queue.offer(new int[] {x - 1, y});
                    grid[x - 1][y] = 1;
                }
                if (x < N-1 && grid[x+1][y] == 0) {
                    queue.offer(new int[] {x + 1, y});
                    grid[x + 1][y] = 1;
                }
                if (y > 0 && grid[x][y - 1] == 0) {
                    queue.offer(new int[] {x, y - 1});
                    grid[x][y - 1] = 1;
                }
                if (y < N-1 && grid[x][y+1] == 0) {
                    queue.offer(new int[] {x, y + 1});
                    grid[x][y + 1] = 1;
                }
            }
            if (!queue.isEmpty())
                dist++;
        }
        return dist;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim();


        String[] grid_str = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(grid_str);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        int result = maxDistance(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
