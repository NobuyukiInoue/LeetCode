import java.util.*;

public class Solution {
    public class Solution2 {
        boolean[][] col = new boolean[9][9];
        boolean[][] row = new boolean[9][9];
        boolean[][] box = new boolean[9][9];
        List<int[]> pos = new ArrayList<>();

        public void solveSudoku(char[][] board) {
            initPosAndCheck(board);
            solve(board, 0);
        }

        private boolean solve(char[][] board, int startPosIndex) {
            for (int pi = startPosIndex; pi < pos.size(); pi++) {
                int i = pos.get(pi)[0];
                int j = pos.get(pi)[1];
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (validPosition(i, j, c)) {
                            board[i][j] = c;
                            if (solve(board, pi + 1)) {
                                return true;
                            } else {
                                board[i][j] = '.';
                                int num = c - '1';
                                col[i][num] = row[j][num] = box[i/3*3 + j/3][num] = false;
                            }
                        }
                    }
                    return false;
                }
                
            }
            return true;
        }

        private boolean validPosition(int i, int j, char c) {
            int num = c - '1';
            int k = i/3*3 + j/3;
            if (col[i][num] || row[j][num] || box[k][num]) {
                return false;
            }
            col[i][num] = row[j][num] = box[k][num] = true;
            return true;
        }

        private boolean initPosAndCheck(char[][] board) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j <9; j++) {
                    if(board[i][j] != '.') {
                        int num = board[i][j] - '1';
                        col[i][num] = row[j][num] = box[i/3*3 + j/3][num] = true;
                    }
                    else{
                        pos.add(new int[]{i,j});
                    }
                }
            }
            return true;
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        char[][] board = new char[9][9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                board[i] = flds[i].replace(",", "").toCharArray();
            }
        }

        System.out.println("board = ");
        for (int i = 0; i < board.length; i++) {
            System.out.println((new String(board[i])));
        }

        long start = System.currentTimeMillis();
        
        Solution2 sl2 = new Solution2();
        sl2.solveSudoku(board);

        long end = System.currentTimeMillis();

        System.out.println("board = ");
        for (int i = 0; i < board.length; i++) {
            System.out.println((new String(board[i])));
        }
        System.out.println((end - start)  + "ms\n");
    }
}
