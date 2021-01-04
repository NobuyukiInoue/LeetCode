import java.util.*;

public class Solution {
    public int countBattleships(char[][] board) {
        // 0ms
        int res = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'X') {
                    if (i > 0 && board[i - 1][j] == 'X' || j > 0 && board[i][j - 1] == 'X') {
                        continue;
                    }
                    res++;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\",\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        char[][] board = new char[flds.length][];
        for (int i = 0; i < board.length; i++) {
            board[i] = flds[i].toCharArray();
        }

        System.out.print("board = [");
        for (int i = 0; i < board.length; i++) {
            if (i == 0)
                System.out.print("[" + new String(board[i]) + "]");
            else
                System.out.print(",[" + new String(board[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        int result = countBattleships(board);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
