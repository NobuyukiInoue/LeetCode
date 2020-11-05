import java.util.*;

public class Solution {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int[] counter = new int[R + C + 1];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                int dist = Math.abs(r - r0) + Math.abs(c - c0);
                counter[dist + 1] += 1;
            }
        }
        
        for (int i = 1; i < counter.length; i++) {
            counter[i] += counter[i - 1];
        }
        
        int[][] ans = new int[R * C][];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                int dist = Math.abs(r - r0) + Math.abs(c - c0);
                ans[counter[dist]] = new int[] { r, c };
                counter[dist]++;
            }
        }
        
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int R = Integer.parseInt(flds[0]);
        int C = Integer.parseInt(flds[1]);
        int r0 = Integer.parseInt(flds[2]);
        int c0 = Integer.parseInt(flds[3]);

        System.out.println("R = " + Integer.toString(R) +
                         ", C = " + Integer.toString(C) +
                         ", r0 = " + Integer.toString(r0) +
                         ", c0 = " + Integer.toString(c0));

        long start = System.currentTimeMillis();

        int[][] result = allCellsDistOrder(R, C, r0, c0);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
