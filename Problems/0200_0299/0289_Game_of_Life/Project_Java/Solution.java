import java.util.*;

public class Solution {
    Mylib ml = new Mylib();

    public void gameOfLife(int[][] board) {
        // 0ms
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int lives = liveNeighbors(board, i, j, m, n);
    
                if (board[i][j] == 1 && lives >= 2 && lives <= 3)
                    board[i][j] = 3;
                if (board[i][j] == 0 && lives == 3)
                    board[i][j] = 2;
            }
        }
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] >>= 1;
            }
        }

        print_board(board);
    }
    
    public int liveNeighbors(int[][] board, int i, int j, int m, int n) {
        int lives = 0;
        for (int x = Math.max(i - 1, 0); x <= Math.min(i + 1, m - 1); x++) {
            for (int y = Math.max(j - 1, 0); y <= Math.min(j + 1, n - 1); y++) {
                lives += board[x][y] & 1;
                /*
                if (board[x][y] % 2 == 1)
                    lives++;
                */
            }
        }
        lives -= board[i][j] & 1;

        return lives;
    }

    private void print_board(int[][] board) {
        System.out.println("board = [");
        for (int i = 0; i < board.length; i++) {
            if (i == 0)
                System.out.println("  " + ml.intArrayToString(board[i]));
            else
                System.out.println(", " + ml.intArrayToString(board[i]));
        }
        System.out.println("]");
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int[][] board = new int[flds.length][];
            for (int i = 0; i < flds.length; i++) {
            board[i] = ml.stringTointArray(flds[i]);
        }

        print_board(board);

        long start = System.currentTimeMillis();
        
        gameOfLife(board);

        long end = System.currentTimeMillis();

    //  System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
