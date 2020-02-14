import java.util.*;

public class Solution {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        // 9ms
        int cols = colsum.length;
        int[][] data = new int[2][cols];
        for (int i = 0; i < cols; i++) {
            if (colsum[i] == 2) {
                data[0][i] = data[1][i] = 1;
                upper--;
                lower--;
            } else if (colsum[i] == 1) {
                if (upper > lower) {
                    data[0][i] = 1;
                    upper--;
                } else {
                    data[1][i] = 1;
                    lower--;
                }
            }
        }

        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (upper != 0 || lower != 0) {
            return res;
        }

        for (int[] row : data) {
            List<Integer> temp = new ArrayList<Integer>();
            for (int col : row) {
                temp.add(col);
            }
            res.add(temp);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("]]", "").trim().split(",\\[");

        String[] fld0 = flds[0].replace("[", "").split(",");
        int upper = Integer.parseInt(fld0[0]);
        int lower = Integer.parseInt(fld0[1]);
        System.out.println("upper = " + Integer.toString(upper) + ", lower = " + Integer.toString(lower));

        String[] data = flds[1].split(",");
        int[] colsum = new int[data.length];
    
        for (int i = 0; i < data.length; i++) {
            colsum[i] = Integer.parseInt(data[i]);
        }

        System.out.print("colsum = [");
        for (int i = 0; i < colsum.length; i++) {
            if (i == 0)
                System.out.print(Integer.toString(colsum[i]));
            else
                System.out.print("," + Integer.toString(colsum[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = reconstructMatrix(upper, lower, colsum);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
