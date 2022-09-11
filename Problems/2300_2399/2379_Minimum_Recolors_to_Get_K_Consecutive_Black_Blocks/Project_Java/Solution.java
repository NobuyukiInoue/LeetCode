import java.util.*;

public class Solution {
    public int minimumRecolors(String blocks, int k) {
        // 1ms
        int lo = -1, white = 0, mi = Integer.MAX_VALUE;
        for (int i = 0; i < blocks.length(); i++) {
            if (blocks.charAt(i) == 'W') {
                white++;
            }
            if (i - lo >= k) {
                mi = Math.min(white, mi);
                lo++;
                if (blocks.charAt(lo) == 'W') {
                    white--;
                }
            }
        }
        return mi;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String blocks = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("blocks = " + blocks + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = minimumRecolors(blocks, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
