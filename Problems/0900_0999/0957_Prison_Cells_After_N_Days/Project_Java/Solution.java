import java.util.*;

public class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        // 2ms
        int[] f_cells = new int[cells.length], next_cells = new int[cells.length];

        for (int cycle = 0; N-- > 0; cells = next_cells.clone(), ++cycle) {
            for (int i = 1; i < cells.length - 1; ++i)
                next_cells[i] = (cells[i - 1] == cells[i + 1] ? 1 : 0);
            if (cycle == 0)
                f_cells = next_cells.clone();
            else if (Arrays.equals(next_cells, f_cells))
                N %= cycle;
        }

        return cells;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] cells = ml.stringToIntArray(flds[0].replace("[[", ""));
        int N = Integer.parseInt(flds[1].replace("]]", ""));
        System.out.println("cells = " + ml.intArrayToString(cells) + ", N = " + Integer.toString(N));

        long start = System.currentTimeMillis();

        int[] result = prisonAfterNDays(cells, N);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
