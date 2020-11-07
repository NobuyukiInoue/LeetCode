import java.util.*;

public class Solution {

    public void solve(char[][] board) {
        // 1ms
        int m = board.length;
        if (m < 1)
            return;

        int n = board[0].length;

        for (int i = 0; i < m; ++i) {
            dfs(board, m, n, i, 0);
            dfs(board, m, n, i, n - 1);
        }

        for (int j = 0; j < n; ++j) {
            dfs(board, m, n, 0, j);
            dfs(board, m, n, m - 1, j);
        }

        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                board[i][j] = board[i][j] == 'O' ? 'X' : board[i][j] == 't' ? 'O' : board[i][j];
    }

    private void dfs(char[][] board, int m, int n, int i, int j) {
        if (i < 0 || j < 0 || i > m - 1 || j > n - 1 || board[i][j] != 'O')
            return;

        board[i][j] = 't';
        dfs(board, m, n, i - 1, j);
        dfs(board, m, n, i + 1, j);
        dfs(board, m, n, i, j - 1);
        dfs(board, m, n, i, j + 1);
    }

    public void solve2(char[][] board) {
        // 18ms
        if (board == null || board.length == 0)
            return;

        Map<String, Boolean> visited = new HashMap();
        for (int j = 0; j < board[0].length; j++) {
            if (board[0][j] == 'O')
                dfs2(board, 0, j, visited);
            if (board[board.length - 1][j] == 'O')
                dfs2(board, board.length - 1, j, visited);
        }

        for (int i = 0; i < board.length; i++) {
            if (board[i][0]=='O')
                dfs2(board, i, 0, visited);
            if (board[i][board[0].length - 1] == 'O')
                dfs2(board, i, board[0].length - 1, visited);
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                String ij = Integer.toString(i) + " " + Integer.toString(j);
                if (!visited.containsKey(ij))
                    board[i][j] = 'X';
            }
        }
    }

    private void dfs2(char[][] board, int i, int j, Map<String, Boolean> visited) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] == 'X')
            return;

        String ij = Integer.toString(i) + " " + Integer.toString(j);
        if (visited.containsKey(ij))
            return;
        if (board[i][j] == 'O')
            visited.put(ij, true);

        dfs2(board, i - 1, j, visited);
        dfs2(board, i + 1, j, visited);
        dfs2(board, i, j - 1, visited);
        dfs2(board, i, j + 1, visited);
    }

    private void printBoard(char[][] board) {
        System.out.println("board = [");
        for (int i = 0; i < board.length; i++) {
            if (i == 0)
                System.out.println("  [" + new String(board[i]) + "]");
            else
                System.out.println(", [" + new String(board[i]) + "]");
        }
        System.out.println("]");
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_board = flds.split("\\],\\[");

        char[][] board = new char[str_board.length][];
        for (int i = 0; i < str_board.length; i++) {
            board[i] = str_board[i].replace(",", "").toCharArray();
        }
        printBoard(board);

        long start = System.currentTimeMillis();

        solve(board);

        long end = System.currentTimeMillis();

        printBoard(board);
        System.out.println((end - start)  + "ms\n");
    }
}
