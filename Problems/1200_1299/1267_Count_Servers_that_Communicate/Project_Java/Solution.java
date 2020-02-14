import java.util.*;

public class Solution {
    public int countServers(int[][] grid) {
        // 2ms
        int m = grid.length, n = grid[0].length;
        int[] rows = new int[m], cols = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    rows[i]++;
                    cols[j]++;
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (rows[i] > 1 || cols[j] > 1)) res++;
            }
        }
        
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] grid = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            grid[i] = ml.stringTointArray(flds[i]);
        }

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(grid[i]));
            else
                System.out.print("," + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = countServers(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
