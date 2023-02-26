import java.util.*;

public class Solution {
    public long interchangeableRectangles(int[][] rectangles) {
        // 38ms - 43ms
        HashMap<Double, Long> map = new HashMap<>();
        long ans = 0;
        for (int[] rect : rectangles) {
            double ratio = (double)rect[0] / (double)rect[1];
            long cur = map.getOrDefault(ratio, 0L);
            ans += cur;
            map.put(ratio, cur + 1);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] rectangles = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("rectangles = " + ml.intIntArrayToString(rectangles));

        long start = System.currentTimeMillis();

        long result = interchangeableRectangles(rectangles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
