import java.util.*;

public class Solution {
    // 0ms
    List<List<Integer>> res;
    boolean[][] grid;
    int[] king;
    
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        res = new ArrayList<>();
        grid = new boolean[8][8];
        this.king = king;

        for (int[] q : queens) {
            grid[q[0]][q[1]] = true;
        }

        helper(new int[] {0, -1});
        helper(new int[] {0, 1});

        helper(new int[] {-1, 0});
        helper(new int[] {1, 0});

        helper(new int[] {-1, -1});
        helper(new int[] {1, 1});

        helper(new int[] {-1, 1});
        helper(new int[] {1, -1});
        
        return res;
    }
    
    void helper(int[] dir) {
        int r = king[0], c = king[1];
        while (r + dir[0] >= 0 
              && r + dir[0] < 8
              && c + dir[1] >= 0
              && c + dir[1] < 8) {
            r += dir[0];
            c += dir[1];
            if (grid[r][c]) {
                List<Integer> q = new ArrayList<>();
                q.add(r); q.add(c);
                res.add(q);
                break;
            }
        }
    }

    // 1ms
    public List<List<Integer>> queensAttacktheKing2(int[][] queens, int[] king) {
        List<List<Integer>> result = new ArrayList<>();
        int move[][] = {{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}};
        
        for (int i = 0; i < 8; i++) {
            int x = king[0] + move[i][0];
            int y = king[1] + move[i][1];
            while (isValid(x, y)) {
                if(queenExist(x, y, queens)) {
                    result.add(Arrays.asList(x, y));
                    break;
                }
                x += move[i][0];
                y += move[i][1];
            }
        }
        
        return result;
    }

    private boolean queenExist(int x, int y, int[][] queens) {
        for(int i = 0; i < queens.length; i++) {
            if (queens[i][0] == x && queens[i][1] == y)
                return true;
        }
        return false;
    }

    private boolean isValid(int x, int y) {
        return (x >= 0 && x < 8 && y >= 0 & y < 8) ? true : false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        Mylib ml = new Mylib();
        int[][] queens   = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        System.out.println("queens = " + ml.intIntArrayToString(queens));
        int[] king = ml.stringToIntArray(flds[1].replace("]", ""));
        System.out.println("king = " + ml.intArrayToString(king));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = queensAttacktheKing(queens, king);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
