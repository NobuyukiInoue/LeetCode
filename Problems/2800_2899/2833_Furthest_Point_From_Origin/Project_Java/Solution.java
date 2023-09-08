import java.util.*;

public class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        // 1ms
        int l = 0, r = 0, m = 0;
        for (char move : moves.toCharArray()) {
            if (move == 'L') {
                l++;
            } else if (move == 'R') {
                r++;
            } else {
                m++;
            }
        }
        return l >= r ? l - r + m : r - l + m;
    }

    public void Main(String temp) {
        String moves = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("moves = \"" + moves + "\"");

        long start = System.currentTimeMillis();

        int result = furthestDistanceFromOrigin(moves);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
