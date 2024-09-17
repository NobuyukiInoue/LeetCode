import java.util.*;

public class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        // 0ms
        int d1 = coordinate1.charAt(0) + coordinate1.charAt(1);
        int d2 = coordinate2.charAt(0) + coordinate2.charAt(1);
        return d1%2 == d2%2;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("[[", "").replace("]]", "").replace("\"", "").trim().split("\\],\\[");

        String coordinate1 = flds[0];
        String coordinate2 = flds[1];
        System.out.println("coordinate1 = \"" + coordinate1 + "\", coordinate2 = \"" + coordinate2 + "\"");

        long start = System.currentTimeMillis();

        boolean result = checkTwoChessboards(coordinate1, coordinate2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
