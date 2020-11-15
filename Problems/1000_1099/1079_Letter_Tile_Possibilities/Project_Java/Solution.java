import java.util.*;

public class Solution {
    int count = 0;

    public int numTilePossibilities(String tiles) {
        // 1ms
        char[] chars = tiles.toCharArray();
        Arrays.sort(chars);
        backtrack(chars, new boolean[chars.length]);
        return count - 1;
    }

    private void backtrack(char[] chars, boolean[] used) {
        count = count + 1;
        for (int i = 0; i < chars.length; i++) {
            if (used[i] || i > 0 && chars[i] == chars[i - 1] && !used[i - 1])
                continue;
            used[i] = true;
            backtrack(chars, used);
            used[i] = false;
        }
    }

    public void Main(String temp) {
        String tiles = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("tiles = " + tiles);

        long start = System.currentTimeMillis();

        int result = numTilePossibilities(tiles);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
