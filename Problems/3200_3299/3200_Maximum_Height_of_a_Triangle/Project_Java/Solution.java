import java.util.*;

public class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        // 0ms
        if (red < blue)
            return maxHeightOfTriangle(blue, red);
        int h1 = (int)Math.sqrt(blue*4 + 1);
        int h2 = (int)Math.sqrt(blue)*2;
        if (Math.pow(h1 + 1, 2)/4 <= red)
            return h1;
        if ((Math.pow(h2 + 1, 2) - 1)/4 <= red)
            return h2;
        if (Math.pow(h1 - 1, 2)/4 <= red)
            return h1 - 1;
        return h2 - 1;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int red = Integer.parseInt(flds[0]);
        int blue = Integer.parseInt(flds[1]);
        System.out.println("red = " + red + ", blue = " + blue);

        long start = System.currentTimeMillis();

        int result = maxHeightOfTriangle(red, blue);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
