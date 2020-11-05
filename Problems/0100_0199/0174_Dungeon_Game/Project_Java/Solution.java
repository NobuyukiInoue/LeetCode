import java.util.*;

public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        // 1ms
        int m = dungeon.length;
        int n = dungeon[0].length;
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++)
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        
        dp[m][n - 1] = 1; dp[m - 1][n] = 1;
        for (int i = m-1; i >= 0; i--) {
            for (int j = n-1; j >= 0; j--) {
                int minHp = Math.min(dp[i+1][j], dp[i][j+1])  - dungeon[i][j];
                if (minHp <= 0)
                    dp[i][j] = 1;
                else
                    dp[i][j] = minHp;
            }
        }
        return dp[0][0];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();

        String[] dungeon_str = flds.split("\\],\\[");
        int[][] dungeon = ml.stringToIntIntArray(dungeon_str);
        System.out.println("dungeon = " + ml.matrixToString(dungeon));

        long start = System.currentTimeMillis();

        int result = calculateMinimumHP(dungeon);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
