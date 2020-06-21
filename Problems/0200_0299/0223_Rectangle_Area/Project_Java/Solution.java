import java.util.*;

public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        // 2ms
        int areaOfSqrA = (C - A)*(D - B);
        int areaOfSqrB = (G - E)*(H - F);
        int left = Math.max(A, E);
        int right = Math.min(G, C);
        int bottom = Math.max(F, B);
        int top = Math.min(D, H);
        int overlap = 0;
        if(right > left && top > bottom)
            overlap = (right - left) * (top - bottom);
        return areaOfSqrA + areaOfSqrB - overlap;
    }

    public int computeArea_bad(int A, int B, int C, int D, int E, int F, int G, int H) {
        return (G - E) * (H - F) + (C - A) * (D - B) - (Math.max(Math.min(C, G)  -  Math.max(E, A), 0) * Math.max(Math.min(D, H) - Math.max(F, B), 0));
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        int A = nums[0];
        int B = nums[1];
        int C = nums[2];
        int D = nums[3];
        int E = nums[4];
        int F = nums[5];
        int G = nums[6];
        int H = nums[7];
        StringBuilder sb = new StringBuilder();
        Formatter formatter = new Formatter(sb, Locale.JAPANESE);
        System.out.println(formatter.format("A = %d, B = %d, C = %d, D = %d, E = %d, F = %d, G = %d, H = %d", A, B, C, D, E, F, G, H));

        long start = System.currentTimeMillis();
        
        int result = computeArea(A, B, C, D, E, F, G, H);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
