import java.util.*;

public class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        // 4ms
        if (grid == null || grid.length == 0 )
            return null;

        int n = grid.length;
        int m = grid[0].length;
        k = k % (n * m);
        
        int[][] arr = new int[n][m];
        for (int i = 0; i< n; i++){
            for (int j = 0; j< m; j++){
                int i1 = (i + (j + k) / m ) % n;
                int j1 = (j + (k % m)) % m;
                arr[i1][j1] = grid[i][j];
            }
        }
        
        List<List<Integer>> list = new ArrayList<>(n);
        for (int i = 0; i < n; i++){
            List<Integer> l = new ArrayList<>(m);
            for (int j = 0; j < m; j++){
                l.add(arr[i][j]);
            }
            list.add(l);
        }
        
        return list;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        String[] fld0 = flds[0].split("\\],\\[");

        int[][] grid = ml.stringToIntIntArray(fld0);
        System.out.println("grid = " + ml.matrixToString(grid));

        int k = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = shiftGrid(grid, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.gridToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
