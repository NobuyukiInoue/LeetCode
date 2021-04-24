import java.util.*;

public class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // 2ms
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.MAX_VALUE;
            }
        }

        for (int i = 0; i < times.length; i++) {
            graph[times[i][0] - 1][times[i][1] - 1] = times[i][2];
        }

        int[] dist = new int[n];
        boolean[] visited = new boolean[n];
        visited[k - 1] = true;
        for (int i = 0; i < n; i++) {
            dist[i] = graph[k - 1][i];
        }
        dist[k - 1] = 0;
        
        for (int i = 0; i < n - 1; i++) {
            int min = Integer.MAX_VALUE;
            int pos = -1;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && dist[j] < min) {
                    min = dist[j];
                    pos = j;
                }
            }
            if (pos == -1)
                break;
            visited[pos] = true;
            for (int k2 = 0; k2 < n; k2++) {
                if (graph[pos][k2] != Integer.MAX_VALUE) {
                    if (dist[k2] > dist[pos] + graph[pos][k2]) {
                        dist[k2] = dist[pos] + graph[pos][k2];
                    }
                }
            }
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, dist[i]);
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] times = ml.stringToIntIntArray(flds[0].replace("[[[", "").split("\\],\\["));
        String[] flds1 = flds[1].replace("]]", "").split("\\],\\[");
        int n = Integer.parseInt(flds1[0]);
        int k = Integer.parseInt(flds1[1]);
        System.out.println("times = " + ml.intIntArrayToString(times) + ", n = " + Integer.toString(n) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = networkDelayTime(times, n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
