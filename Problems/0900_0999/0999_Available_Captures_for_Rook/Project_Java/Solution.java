import java.util.*;

public class Solution {
    public int numRookCaptures(char[][] board) {
        int i, j;
        int x0 = 0, y0 = 0;
        for (i = 0; i < 8; i++) {
            for (j = 0; j < 8; j++) {
                if (new String(board[i]).charAt(j) == 'R') {
                    x0 = i;
                    y0 = j;
                }
            }
        }
        int res = 0;
        /*
        int x, y;
        int[][] data = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (int n = 0; n < data.length; n++) {
            x = x0 + data[n][0];
            y = y0 + data[n][1];
            while (0 <= x && x < 8 && 0 <= y && y < 8) {
                if (board[x][y] == 'p')
                    res++;
                if (board[x][y] != '.')
                    break;
                x = x + data[n][0];
                y = y + data[n][1];
            }
        }
        */
        for (int[] d : new int[][] {{1, 0}, {0, 1}, { -1, 0}, {0, -1}}) {
            for (int x = x0 + d[0], y = y0 + d[1]; 0 <= x && x < 8 && 0 <= y && y < 8; x += d[0], y += d[1]) {
                if (board[x][y] == 'p') res++;
                if (board[x][y] != '.') break;
            }
        }
        return res;
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        char[][] board = new char[8][8];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i] = flds[i].replace(",", "").toCharArray();
            }
        }

        System.out.println("board = ");
        for (int i = 0; i < board.length; i++) {
            System.out.println((new String(board[i])));
        }

        long start = System.currentTimeMillis();
        
        int result = numRookCaptures(board);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
