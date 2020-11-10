import java.util.*;

public class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        // 0ms
        int t = Math.abs(target[0]) + Math.abs(target[1]);
        for (int[] g :ghosts)
            if (t >= Math.abs(g[0] - target[0]) + Math.abs(g[1] - target[1]))
                return false;
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] ghosts = ml.stringToIntIntArray(flds[0].replace("[[[", "").split("\\],\\["));
        int[] target = ml.stringToIntArray(flds[1].replace("]]", ""));
        System.out.println("ghosts = " + ml.intIntArrayToString(ghosts) + ", target = " + ml.intArrayToString(target));

        long start = System.currentTimeMillis();

        boolean result = escapeGhosts(ghosts, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
