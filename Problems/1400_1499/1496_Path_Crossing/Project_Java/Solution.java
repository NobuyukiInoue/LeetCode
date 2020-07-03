import java.util.*;

public class Solution {
    public boolean isPathCrossing(String path) {
        // 4ms
        Set<String> seen = new HashSet<>();
        seen.add(0 + ", " + 0);
        for (int i = 0, x = 0, y = 0; i < path.length(); i++) {
            char c = path.charAt(i);
            if (c == 'N') {
                y += 1;
            } else if (c == 'S') {
                y -= 1;
            } else if (c == 'E') {
                x -= 1;
            } else {
                x += 1;
            }
            if (!seen.add(x + ", " + y)) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String path = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("path = " + path);

        long start = System.currentTimeMillis();

        boolean result = isPathCrossing(path);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
