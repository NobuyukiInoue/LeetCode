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

    private String listListIntToString(List<List<Integer>> data) {
        if (data == null) {
            return "";
        }
        if (data.size() <= 0) {
            return "";
        }
        StringBuilder resultStr = new StringBuilder("");
        for (int i = 0; i < data.size(); i++) {
            if (i == 0)
                resultStr.append("[" + listIntToString(data.get(i)) + "]");
            else
                resultStr.append(",[" + listIntToString(data.get(i)) + "]");
        }

        return resultStr.toString();
    }

    private String listIntToString(List<Integer> data) {
        if (data.size() <= 0) {
            return "";
        }
        StringBuilder resultStr = new StringBuilder(Integer.toString(data.get(0)));
        for (int i = 1; i < data.size(); i++)
            resultStr.append("," + Integer.toString(data.get(i)));

        return resultStr.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        String[] fld0 = flds[0].split("\\],\\[");

        int[][] grid = new int[fld0.length][];
    
        for (int i = 0; i < fld0.length; i++) {
            grid[i] = ml.stringTointArray(fld0[i]);
        }

        System.out.print("grid = [");
        for (int i = 0; i < grid.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(grid[i]));
            else
                System.out.print("," + ml.intArrayToString(grid[i]));
        }
        System.out.println("]");

        int k = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = shiftGrid(grid, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listListIntToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
