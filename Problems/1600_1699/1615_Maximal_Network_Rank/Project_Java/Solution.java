import java.util.*;

public class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        // 4ms
        int[] connections = new int[n];
        boolean[][] graph = new boolean[n][n];
        for (int[] cities : roads) {
            connections[cities[0]]++;
            connections[cities[1]]++;
            graph[cities[0]][cities[1]] = graph[cities[1]][cities[0]] = true;
        }
        int max_rank = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int rank = connections[i] + connections[j];
                if (graph[i][j]) {
                    rank--;
                }
                max_rank = Math.max(max_rank, rank);
            }
        }
        return max_rank;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("]]]", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0].replace("[[", ""));
        int[][] roads = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("n = " + n + ", roads = " + ml.intIntArrayToString(roads));

        long start = System.currentTimeMillis();

        int result = maximalNetworkRank(n ,roads);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
