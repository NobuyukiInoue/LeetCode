import java.util.*;

public class Solution {
    public int findCenter(int[][] edges) {
        // 0ms
        int n1 = edges[0][0], n2 = edges[0][1];
        if (n1 == edges[1][0] || n1 == edges[1][1]) {
            return n1;
        }
        return n2;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] edges   = ml.stringToIntIntArray(flds);
        System.out.println("edges = " + ml.intIntArrayToString(edges));

        long start = System.currentTimeMillis();

        int result = findCenter(edges);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
