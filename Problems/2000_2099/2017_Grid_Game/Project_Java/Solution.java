import java.util.*;

public class Solution {
    public long gridGame(int[][] grid) {
        // 4ms
        int n = grid[0].length;
        long res = 0;
        for (int j = 0; j < n; j++) {
            res += grid[0][j];
        }
        long r2sum = 0;
        for (int j = 0; j < n; j++) {
            res = Math.min(res, Math.max(res - grid[0][j], r2sum));
            r2sum += grid[1][j];
        }
        return res;
    }

    public long gridGame2(int[][] grid) {
        // 8ms
        long topSum = Arrays.stream(grid[0]).asLongStream().sum();
        long bottomSum = 0;
        long ans = Long.MAX_VALUE;
        for (int i = 0; i < grid[0].length; i++) {
            topSum -= grid[0][i];
            ans = Math.min(ans, Math.max(topSum, bottomSum));
            bottomSum += grid[1][i];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        long result = gridGame(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Long.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
