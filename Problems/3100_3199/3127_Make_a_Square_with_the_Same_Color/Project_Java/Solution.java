import java.util.*;

public class Solution {
    public boolean canMakeSquare(char[][] grid) {
        // 0ms
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                if (isPossible(grid, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean isPossible(char[][] grid, int i, int j) {
        int cnt_w = 0, cnt_b = 0;
        for (int x = i; x < i + 2; x++) {
            for (int y = j; y < j + 2; y++) {
                if (grid[x][y] == 'W') {
                    cnt_w++;
                } else {
                    cnt_b++;
                }
            }
        }
        if (cnt_w > 2 || cnt_b > 2) {
            return true;
        }
        return false;
    }

    public String gridToString(char[][] grid) {
        if (grid == null)
            return "[]";
        if (grid.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[\n  ");
        sb.append(new String(grid[0]) + "\n");
        for (int i = 1; i < grid.length; i++) {
            sb.append(", " + new String(grid[i]) + "\n");
        }

        return sb.append("]").toString();
   }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        char[][] grid = new char[3][3]; 
        String[] rows = flds.split("\\],\\[");
        for (int i = 0; i < rows.length; i++) {
            grid[i] = rows[i].replace(",", "").toCharArray();
        }
        System.out.println("grid = " + gridToString(grid));

        long start = System.currentTimeMillis();

        boolean result = canMakeSquare(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
