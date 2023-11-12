import java.util.*;

public class Solution {
    public int findChampion(int[][] grid) {
        // 1ms
        for (int i = 0; i < grid.length; i++) {
            int cnt = 0;
            for (int data : grid[i]) {
                cnt += data;
            }
            if (cnt == grid.length - 1) {
                return i;
            }
        }
        return 0;
    }

    public int findChampion2(int[][] grid) {
        // 5ms
        for (int i = 0; i < grid.length; i++) {
            if (Arrays.stream(grid[i]).sum() == grid.length - 1) {
                return i;
            }
        }
        return 0;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("grid = " + ml.intIntArrayToString(grid));

        long start = System.currentTimeMillis();

        int result = findChampion(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
