import java.util.*;

public class Solution {
    public boolean checkValidGrid(int[][] grid) {
        // 1ms
        int row = grid.length, col = grid[0].length;
        boolean visited[][] = new boolean[row][col];
        isValid(grid, visited,0, 0, 0, row, col);
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (!visited[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    static void isValid(int grid[][],boolean visited[][],int v1,int v2,int move,int r,int c){
        if (v1 < 0 || v2 < 0 || v1 >= r || v2 >= c) {
            return;
        }
        if (!visited[v1][v2] && grid[v1][v2] == move) {
            visited[v1][v2] = true;
            isValid(grid, visited, v1 + 1, v2 + 2, move + 1, r, c);
            isValid(grid, visited, v1 + 1, v2 - 2, move + 1, r, c);
            isValid(grid, visited, v1 - 1, v2 + 2, move + 1, r, c);
            isValid(grid, visited, v1 - 1, v2 - 2, move + 1, r, c);
            
            isValid(grid, visited, v1 + 2, v2 + 1, move + 1, r, c);
            isValid(grid, visited, v1 - 2, v2 + 1, move + 1, r, c);
            isValid(grid, visited, v1 + 2, v2 - 1, move + 1, r, c);
            isValid(grid, visited, v1 - 2, v2 - 1, move + 1, r, c);
        }
    }
    
    public boolean checkValidGrid2(int[][] grid) {
        // 2ms
        int n = grid.length*grid.length;
        int[][] dic = new int[n][2];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                dic[grid[i][j]] = new int[] {i, j};
            }
        }
        int[] cur = dic[0];
        if (cur[0] != 0 || cur[1] != 0) {
            return false;
        }
        for (int idx = 1; idx < n; idx++) {
            int[] n_cur = dic[idx];
            if (Math.abs(n_cur[0] - cur[0]) == 1 && Math.abs(n_cur[1] - cur[1]) == 2
             || Math.abs(n_cur[0] - cur[0]) == 2 && Math.abs(n_cur[1] - cur[1]) == 1) {
                cur = n_cur;
                continue;
             }
             return false;
        }
        return true;
    }

    public boolean checkValidGrid3(int[][] grid) {
        // 3ms
        HashMap<Integer, Integer[]> dic = new HashMap<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                dic.put(grid[i][j], new Integer[] {i, j});
            }
        }
        int n = grid.length*grid.length;
        Integer[] cur = dic.get(0);
        if (cur[0] != 0 || cur[1] != 0) {
            return false;
        }
        for (int idx = 1; idx < n; idx++) {
            Integer[] n_cur = dic.get(idx);
            if (Math.abs(n_cur[0] - cur[0]) == 1 && Math.abs(n_cur[1] - cur[1]) == 2
             || Math.abs(n_cur[0] - cur[0]) == 2 && Math.abs(n_cur[1] - cur[1]) == 1) {
                cur = n_cur;
                continue;
             }
             return false;
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] grid = ml.stringToIntIntArray(str_mat);
        System.out.println("grid = " + ml.matrixToString(grid));

        long start = System.currentTimeMillis();

        boolean result = checkValidGrid(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
