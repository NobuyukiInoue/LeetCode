import java.util.*;

public class Solution {
    public int largestAltitude(int[] gain) {
        // 0ms
        int height = 0, heightMax = 0;
        for (int n : gain) {
            height += n;
            if (height > heightMax)
                heightMax = height;
        }
        return heightMax;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] gain = ml.stringToIntArray(flds);
        System.out.println("gain = " + ml.intArrayToString(gain));

        long start = System.currentTimeMillis();

        int result = largestAltitude(gain);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
