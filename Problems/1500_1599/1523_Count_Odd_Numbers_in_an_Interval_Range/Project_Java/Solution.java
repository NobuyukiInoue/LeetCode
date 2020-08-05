import java.util.*;

public class Solution {
    public int countOdds(int low, int high) {
        // 0ms
        return (high + 1)/2 - low/2;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int low  = Integer.parseInt(flds[0]);
        int high = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        int result = countOdds(low, high);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
