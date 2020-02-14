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

    public String IntInt_array_to_String(int[][] list) {
        if (list.length <= 0)
            return "[]";

        StringBuffer resultStr = new StringBuffer("[");
        for (int i = 0; i < list.length; i++) {
            if (i == 0)
                resultStr.append("[");
            else
                resultStr.append(",[");

            for (int j = 0; j < list[i].length; j++) {
                if (j == 0)
                    resultStr.append(Integer.toString(list[i][j]));
                else
                    resultStr.append("," + Integer.toString(list[i][j]));
            }
            resultStr.append("]");
        }

        return resultStr.append("]").toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();

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

        System.out.println("result = " + IntInt_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
