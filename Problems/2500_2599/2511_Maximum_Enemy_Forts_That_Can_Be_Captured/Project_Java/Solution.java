import java.util.*;

public class Solution {
    public int captureForts(int[] forts) {
        // 0ms
        int current_idx = 0, max_forts = 0;
        for (int i = 0; i < forts.length; i++) {
            if (forts[i] != 0) {
                if (forts[current_idx] == -forts[i]) {
                    max_forts = Math.max(max_forts, i - current_idx - 1);
                }
                current_idx = i;
            }
        }
        return max_forts;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] forts = ml.stringToIntArray(flds);
        System.out.println("forts = " + ml.intArrayToString(forts));

        long start = System.currentTimeMillis();

        int result = captureForts(forts);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
