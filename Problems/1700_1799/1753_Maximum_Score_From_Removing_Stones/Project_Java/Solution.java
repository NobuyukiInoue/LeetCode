import java.util.*;

public class Solution {
    public int maximumScore(int a, int b, int c) {
        // 0ms
        return Math.min((a + b + c) / 2, a + b + c - Math.max(Math.max(a, b), c));
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int a = nums[0], b = nums[1], c = nums[2];
        System.out.println("a = " + Integer.toString(a) + ", b = " + Integer.toString(b) + ", c = " + Integer.toString(c));

        long start = System.currentTimeMillis();

        int result = maximumScore(a, b, c);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
