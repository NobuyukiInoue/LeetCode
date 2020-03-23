import java.util.*;

public class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        // 2ms
        int m = matrix.length, n = matrix[0].length;
        int[] mr = new int[matrix.length];
        int[] mc = new int[matrix[0].length];

        Arrays.fill(mr, Integer.MAX_VALUE);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mr[i] = Math.min(matrix[i][j], mr[i]);
                mc[j] = Math.max(matrix[i][j], mc[j]);
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mr[i] == mc[j]) {
                    res.add(mr[i]);
                }
            }
        }

        return res;
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + Integer.toString(list.get(i)));
        }

        return sb.append("]").toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_matrix = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] matrix = new int[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
            matrix[i] = ml.stringTointArray(str_matrix[i]);
        }

        System.out.println("matrix = [");
        for (int i = 0; i < matrix.length; i++) {
            if (i == 0)
                System.out.println("  " + ml.intArrayToString(matrix[i]));
            else
                System.out.println(", " + ml.intArrayToString(matrix[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        List<Integer> result = luckyNumbers(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
