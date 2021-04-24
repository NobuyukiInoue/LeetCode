import java.util.*;

public class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        // 1ms
        double[] oldRow = new double[1];
        oldRow[0] = poured;
        for (int i = 0; i < query_row; i++) {
            double[] newRow = new double[Math.min(i + 2, query_glass + 1)];
            for (int j = 0; j < oldRow.length - 1; j++) {
                if (oldRow[j] > 1) {
                    newRow[j] += (oldRow[j] - 1)/2.0;
                    newRow[j + 1] += (oldRow[j] - 1)/2.0;
                }
            }
            if (oldRow[oldRow.length - 1] > 1) {
                newRow[newRow.length - 1] += (oldRow[oldRow.length - 1] - 1)/2.0;
                if (oldRow.length < newRow.length) {
                    newRow[newRow.length - 2] += (oldRow[oldRow.length - 1] - 1)/2.0;
                }
            }
            oldRow = newRow;
        }
        return Math.min(oldRow[oldRow.length - 1], 1);
    }

    public double champagneTower2(int poured, int query_row, int query_glass) {
        // 2ms
        double[] res = new double[query_row + 2];
        res[0] = poured;
        for (int row = 1; row <= query_row; row++) {
            for (int i = row; i >= 0; i--) {
                res[i + 1] += res[i] = Math.max(0.0, (res[i] - 1) / 2);
            }
        }
        return Math.min(res[query_glass], 1.0);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim().split(",");

        int poured = Integer.parseInt(flds[0]);
        int query_row = Integer.parseInt(flds[1]);
        int query_glass = Integer.parseInt(flds[2]);
        System.out.println("poured = " + Integer.toString(poured) + ", query_row = " + Integer.toString(query_row) + ", query_glass = " + Integer.toString(query_glass));

        long start = System.currentTimeMillis();

        double result = champagneTower(poured, query_row, query_glass);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
