import java.util.*;

public class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        // 1ms
        for (int i = 0; i < grid.length; i++) {
            if (i % 2 != 0) {
                for (int left = 0, right = grid[i].length - 1; left < right; left++, right--) {
                    int temp = grid[i][left];
                    grid[i][left] = grid[i][right];
                    grid[i][right] = temp;
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        boolean alt = true;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (alt) {
                    res.add(grid[i][j]);
                }
                alt = !alt;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        List<Integer> result = zigzagTraversal(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
