import java.util.*;

public class Solution {
    public char[][] updateBoard(char[][] board, int[] click) {
        // 0ms
        int m = board.length, n = board[0].length;
        int row = click[0], col = click[1];
        
        if (board[row][col] == 'M') {
            board[row][col] = 'X';
        } else {
            int count = 0;
            for (int i = -1; i < 2; i++) {
                for (int j = -1; j < 2; j++) {
                    if (i == 0 && j == 0)
                        continue;
                    int r = row + i, c = col + j;
                    if (r < 0 || r >= m || c < 0 || c >= n)
                        continue;
                    if (board[r][c] == 'M' || board[r][c] == 'X')
                        count++;
                }
            }
            
            if (count > 0) {
                board[row][col] = (char)(count + '0');
            } else {
                board[row][col] = 'B';
                for (int i = -1; i < 2; i++) {
                    for (int j = -1; j < 2; j++) {
                        if (i == 0 && j == 0)
                            continue;
                        int r = row + i, c = col + j;
                        if (r < 0 || r >= m || c < 0 || c >= n)
                            continue;
                        if (board[r][c] == 'E')
                            updateBoard(board, new int[] {r, c});
                    }
                }
            }
        }
        return board;
    }

    // 1ms
    int[][] directions = new int[][] {{1, 0}, {0, 1}, {1, 1}, {-1, 0}, {0, -1}, {-1, -1}, {-1, 1}, {1, -1}};

    public char[][] updateBoard2(char[][] board, int[] click) {
        return recursive(board, click[0], click[1]);
    }

    private char[][] recursive(char[][] board, int row, int col) {
        int mines = 0;
        if (board[row][col] == 'M' || board[row][col] == 'E') {
            if (board[row][col] == 'M') {
                board[row][col] = 'X';
                return board;
            } else if (board[row][col] == 'E') {
                List<int[]> l = new ArrayList<>();
                mines = 0;
                for (int[] direction : directions) {
                    int r = row + direction[0];
                    int c = col + direction[1];
                    if (0 <= r && r < board.length && 0 <= c && c < board[0].length) {
                        if (board[r][c] == 'M' || board[r][c] == 'X') {
                            mines++;
                        }
                        if (board[r][c] == 'M' || board[r][c] == 'E') {
                            l.add(new int[] {r, c});
                        }
                    }
                }
                if (mines == 0) {
                    board[row][col] = 'B';
                    for (int[] flds : l) {
                        recursive(board, flds[0], flds[1]);
                    }
                } else {
                    board[row][col] = (char)(mines + '0');
                }
            }
        }
        return board;
    }

    public String charBoardToString(String title, char[][]board) {
        if (board == null || board.length == 0) {
            return title + " = [[]]";
        }
        StringBuilder sb = new StringBuilder(title + " = [\n  [" + new String(board[0]) + "]\n");
        for (int i = 1; i < board.length; i++) {
            sb.append(", [" + new String(board[i]) + "]\n");
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\",\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");
        String[] flds0 = flds[0].split("\\],\\[");

        char[][] board = new char[flds0.length][];
        for (int i = 0; i < board.length; i++) {
            board[i] = flds0[i].replace(",", "").toCharArray();
        }
        System.out.println(charBoardToString("board", board));

        int[] click = new int[2];
        String[] flds1 = flds[1].replace("]", "").split(",");
        for (int i = 0; i < flds1.length; i++) {
            click[i] = Integer.parseInt(flds1[i]);
        }
        Mylib ml = new Mylib();
        System.out.println("click = " + ml.intArrayToString(click));

        long start = System.currentTimeMillis();

        char[][] result = updateBoard(board, click);

        long end = System.currentTimeMillis();

        System.out.println(charBoardToString("result", result));
        System.out.println((end - start)  + "ms\n");
    }
}
