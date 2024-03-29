import java.util.*;

public class Solution {
    public int countSquares(int[][] matrix) {
        // 6ms
        int count = 0, m = matrix.length, n = matrix[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1 && (i != 0 && j != 0)) {
                    matrix[i][j] = Math.min(matrix[i - 1][j - 1], Math.min(matrix[i - 1][j], matrix[i][j - 1])) + 1;
                }
            }
            // 9ms - 10ms
            //count += Arrays.stream(matrix[i]).sum();
            count += sum(matrix[i]);
        }
        return count;
    }

    private int sum(int[] nums) {
        int res = 0;
        for (int num : nums) {
            res += num;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] matrix = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("matrix = " + ml.intIntArrayToString(matrix));

        long start = System.currentTimeMillis();

        int result = countSquares(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
