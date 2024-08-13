import java.util.*;

// 18ms - 21ms
class NeighborSum {
    int n;
    int[][]grid;
    HashMap<Integer, Integer[]> pos = new HashMap<>();

    public NeighborSum(int[][] grid) {
        this.grid = grid.clone();
        n = grid.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                this.pos.put(this.grid[i][j], new Integer[] {i, j});
            }
        }
    }
    
    public int adjacentSum(int value) {
        Integer[] temp  = pos.get(value);
        int x = temp[0], y = temp[1];
        int[][] dirr = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};
        int total = 0;
        for (int[] dir : dirr) {
            if (0 <= dir[0] && dir[0] < n && 0 <= dir[1] && dir[1] < n) {
                total += grid[dir[0]][dir[1]];
            }
        }
        return total;
    }
    
    public int diagonalSum(int value) {
        Integer[] temp  = pos.get(value);
        int x = temp[0], y = temp[1];
        int[][] dirr = {{x - 1, y - 1}, {x - 1, y + 1}, {x + 1, y - 1}, {x + 1, y + 1}};
        int total = 0;
        for (int[] dir : dirr) {
            if (0 <= dir[0] && dir[0] < n && 0 <= dir[1] && dir[1] < n) {
                total += grid[dir[0]][dir[1]];
            }
        }
        return total;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */
 