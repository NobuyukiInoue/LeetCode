import java.util.*;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 1ms
        boolean[][] rule1 = new boolean[9][10];
        boolean[][] rule2 = new boolean[9][10];
        boolean[][] rule3 = new boolean[9][10];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char digit = board[i][j];
                if (digit != '.') {
                    int idx3 = 3 * (i / 3) + j / 3;
                    // convert char to int '0' -> 0
                    digit -= '0';
                    if (rule1[j][digit] || rule2[i][digit] || rule3[idx3][digit]) {
                        return false;
                    }
                    rule1[j][digit] = true;
                    rule2[i][digit] = true;
                    rule3[idx3][digit] = true;
                }
            }
        }
        return true;
    }

    public boolean isValidSudoku_bad(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            HashMap<String, Integer> dic = new HashMap<String, Integer>();
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.')
                    continue;
                if (dic.containsKey(board[i][j]))
                    return false;
                else
                    dic.put(String.valueOf(board[i][j]), 1);
            }
        }
        for (int j = 0; j < board[0].length; j++) {
            HashMap<String, Integer> dic = new HashMap<String, Integer>();
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] == '.')
                    continue;
                if (dic.containsKey(board[i][j]))
                    return false;
                else
                    dic.put(String.valueOf(board[i][j]), 1);
            }
        }

        char[] data = new char[81];
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[i].length; j++)
                data[i*8 + j] = board[i][j];

        for (int i = 0; i < board.length; i += 3) {
            for (int j = 0; j < 3; j++) {
                List<String> temp = new ArrayList<String>();
                for (int n = i*9 + j*3; n < i*9 + (j + 1)*3; n++)
                    temp.add(String.valueOf(data[n]));
                for (int n = (i + 1)*9 + j*3; n < (i + 1)*9 + (j + 1)*3; n++)
                    temp.add(String.valueOf(data[n]));
                for (int n = (i + 2)*9 + j*3; n < (i + 2)*9 + (j + 1)*3; n++)
                    temp.add(String.valueOf(data[n]));

                List<String> elem = new ArrayList<String>();
                for (int n = 0; n < temp.size(); n++) {
                    if (!temp.get(n).equals(".")) {
                        elem.add(String.valueOf(temp.get(n)));
                    }
                }
                if (temp.size() != elem.size())
                    return false;
            }
        }

        return true;
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
        
        boolean result = isValidSudoku(board);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
