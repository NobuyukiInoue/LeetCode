import java.util.*;

public class Solution {
    public boolean squareIsWhite(String coordinates) {
        // 0ms
        if ((coordinates.charAt(0) + coordinates.charAt(1)) % 2 == 0)
            return false;
        return true;
    }

    public void Main(String temp) {
        String coordinates = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("coordinates = " + coordinates);

        long start = System.currentTimeMillis();

        boolean result = squareIsWhite(coordinates);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
