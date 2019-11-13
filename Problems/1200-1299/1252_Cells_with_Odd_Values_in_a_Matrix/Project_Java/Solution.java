import java.util.*;

public class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        // 1ms
        boolean[] row = new boolean[n], col = new boolean[m];
        for (int[] idx : indices) {
            row[idx[0]] ^= true;
            col[idx[1]] ^= true;
        }
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cnt += row[i] ^ col[j] ? 1 : 0;
            }
        }
        return cnt;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("]]]", "").trim().split("\\],\\[\\[");

        String[] fld0 = flds[0].replace("[[", "").split(",");
        int n = Integer.parseInt(fld0[0]);
        int m = Integer.parseInt(fld0[1]);
        System.out.println("n = " + Integer.toString(n) + ", m = " + Integer.toString(m));

        Mylib ml = new Mylib();
        String[] data = flds[1].split("\\],\\[");
        int[][] indices = new int[data.length][];
    
        for (int i = 0; i < data.length; i++) {
            indices[i] = ml.str_to_int_array(data[i]);
        }

        System.out.print("indices = [");
        for (int i = 0; i < indices.length; i++) {
            if (i == 0)
                System.out.print(ml.output_int_array(indices[i]));
            else
                System.out.print("," + ml.output_int_array(indices[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = oddCells(n, m, indices);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
