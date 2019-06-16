import java.util.*;

public class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, i = 0, d[][] = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};
        for (int j = 0; j < instructions.length(); ++j)
            if (instructions.charAt(j) == 'R')
                i = (i + 1) % 4;
            else if (instructions.charAt(j) == 'L')
                i = (i + 3) % 4;
            else {
                x += d[i][0]; y += d[i][1];
            }
        return x == 0 && y == 0 || i > 0;
    }

    public void Main(String temp) {
        String instructions = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("instructions = " + instructions);

        long start = System.currentTimeMillis();
        
        Boolean result = isRobotBounded(instructions);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
