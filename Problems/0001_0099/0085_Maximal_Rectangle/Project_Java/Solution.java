import java.util.*;

public class Solution {
    public int maximalRectangle(char[][] matrix) {
        // 4ms
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return 0;

        int[] hist = new int[matrix[0].length + 1];
        int res = 0;

        for (char[] row : matrix) {
            for (int i = 0; i < row.length; i++) {
                if (row[i] == '0') {
                    hist[i] = 0;
                } else {
                    hist[i]++;
                }
            }
            res = Math.max(res, max_area(hist));
        }

        return res;
    }

    private int max_area(int[] hist) {
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int max_ = 0;

        for (int i = 0; i < hist.length; i++) {
            while (!stack.isEmpty() && hist[stack.peek()] > hist[i]) {
                int v = hist[stack.pop()];
                int j;
                if (stack.size() > 0) {
                    j = stack.peek() + 1;
                } else {
                    j = 0;
                }
                max_ = Math.max(max_, v*(i - j));
            }
            stack.push(i);
        }

        return max_;
    }

    private String charAttayToString(char[][] flds) {
        if (flds == null)
            return "[]";
        if (flds.length == 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[\n \"" + new String(flds[0]) + "\"\n");
        for (int i = 1; i < flds.length; i++) {
            sb.append(",\"" + new String(flds[i]) + "\"\n");
        }

        return sb.append("]").toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        char[][] matrix;
        if (flds.equals("[]")) {
            matrix = null;
        } else {
            String[] str_matrix = flds.split("\\],\\[");
            matrix = new char[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
                matrix[i] = str_matrix[i].replace(",", "").toCharArray();
            }
        }
        System.out.println("matrix = " + charAttayToString(matrix));

        long start = System.currentTimeMillis();

        int result = maximalRectangle(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
