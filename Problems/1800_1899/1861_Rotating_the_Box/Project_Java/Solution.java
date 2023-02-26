import java.util.*;

public class Solution {
    public char[][] rotateTheBox(char[][] box) {
        // 5ms
        int m = box.length, n = box[0].length;
        char [][] res = new char[n][m];
        for (int i = 0; i < m; ++i)
            for (int j = n - 1, k = n - 1; j >= 0; --j) {
                res[j][m - i - 1] = '.';
                if (box[i][j] != '.') {
                    k = box[i][j] == '*' ? j : k;
                    res[k--][m - i - 1] = box[i][j];
                }
            }
        return res;
    }

    public char[][] stringToCharCharArray(String[] s) {
        if (s == null)
            return null;
        char[][] box = new char[s.length][];
        for (int i = 0; i < s.length; i++) {
            box[i] = s[i].toCharArray();
        }
        return box;
    }

    public String gridToString(char[][] box) {
        if (box == null)
            return "[]";
        if (box.length <= 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[\n");
        sb.append(" [" + new String(box[0]) + "]\n");
        for (int i = 1; i < box.length; i++) {
            sb.append(" [" + (new String(box[i])) + "]\n");
        }
        return sb.append("]\n").toString();
   }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        char[][] grid = stringToCharCharArray(str_mat);
        System.out.println("grid = " + gridToString(grid));

        long start = System.currentTimeMillis();

        char[][] result = rotateTheBox(grid);

        long end = System.currentTimeMillis();

        System.out.println("result = " + gridToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
