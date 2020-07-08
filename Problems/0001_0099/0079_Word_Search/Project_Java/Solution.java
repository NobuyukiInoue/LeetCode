import java.util.*;

public class Solution {
    static boolean[][] visited;

    public boolean exist(char[][] board, String word) {
        // 8ms
        visited = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if ((word.charAt(0) == board[i][j]) && search(board, word, i, j, 0)) {
                    return true;
                }
            }
        }

        return false;
    }
    
    private boolean search(char[][]board, String word, int i, int j, int index){
        if (index == word.length()) {
            return true;
        }
        if (i >= board.length || i < 0 || j >= board[i].length || j < 0 || board[i][j] != word.charAt(index) || visited[i][j]) {
            return false;
        }

        visited[i][j] = true;
        if (search(board, word, i-1, j, index+1) || 
            search(board, word, i+1, j, index+1) ||
            search(board, word, i, j-1, index+1) || 
            search(board, word, i, j+1, index+1)) {
            return true;
        }
        visited[i][j] = false;

        return false;
    }

    private String boardToString(char[][] board) {
        if (board.length <= 0) {
            return "[[]]";
        }
        StringBuilder resultStr = new StringBuilder("[\n");
        resultStr.append("  [" + new String(board[0]) + "]\n");
        for (int i = 1; i < board.length; i++) {
            resultStr.append(" ,[" +  new String(board[i]) + "]\n");
        }
        resultStr.append("]");
        return resultStr.toString();
    }

/*
    private String boardToString(char[][] board) {
        if (board.length <= 0) {
            return "[[]]";
        }
        List<String> row = new ArrayList<String>();
        for (int i = 0; i < board.length; i++) {
            row.add(new String(board[i]));
        }
        String res = "[\n  [" + String.join("]\n ,[", row) + "]\n]";
        return res;
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");
        String[] rows = flds[0].split("\\],\\[");
        char[][] board = new char[rows.length][];
        for (int i = 0; i < board.length; i++) {
            board[i] = rows[i].replace(",", "").toCharArray();
        }
        String word = flds[1].replace("]", "");
        System.out.println("board = " + boardToString(board));
        System.out.println("word = \"" + word + "\"");

        long start = System.currentTimeMillis();
        
        boolean result = exist(board, word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
