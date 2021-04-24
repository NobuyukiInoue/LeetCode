import java.util.*;

public class Solution2 {
    // 157ms
    HashMap<Integer, HashMap<Integer, Integer>> graph;
    boolean[] arrived;
    int[] distances;

    public int networkDelayTime(int[][] times, int n, int k) {
        graph = new HashMap<>();
        for (int[] item : times) {
            if (!graph.containsKey(item[0])) {
                HashMap<Integer, Integer> tempHash = new HashMap<>();
                tempHash.put(item[1], item[2]);
                graph.put(item[0], new HashMap<>(tempHash));
            } else {
                HashMap<Integer, Integer> tempHash = graph.get(item[0]);
                tempHash.put(item[1], item[2]);
                graph.put(item[0], tempHash);
            }
        }
        distances = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            distances[i] = Integer.MAX_VALUE;
        }

        start(k, n);

        int max_distance = -1;
        for (int i = 1; i < distances.length; i++) {
            if (distances[i] == Integer.MAX_VALUE) {
                return -1;
            } else {
                if (distances[i] > max_distance) {
                    max_distance = distances[i];
                }
            }
        }
        return max_distance;
    }

    private int minD(int n) {
        int max_arrival_time = Integer.MAX_VALUE;
        int min_index = -1;
        for (int v = 1; v < n + 1; v++) {
            if (distances[v] < max_arrival_time && arrived[v] == false) {
                max_arrival_time = distances[v];
                min_index = v;
            }
        }
        return min_index;
    }

    private void start(int src, int n) {
        distances[src] = 0;
        arrived = new boolean[n + 1];
        for (int i = 0; i < n; i++) {
            int u = minD(n);
            if (u == -1) {
                arrived[arrived.length - 1] = true;
            } else {
                arrived[u] = true;
            }
            for (int v = 1; v < n + 1; v++) {
                if (graph.containsKey(u)) {
                    HashMap<Integer, Integer> uv = new HashMap<>(graph.get(u));
                    if (uv.containsKey(v)) {
                        if (arrived[v] == false && distances[v] > distances[u] + uv.get(v)) {
                            distances[v] = distances[u] + uv.get(v);
                        }
                    }
                }
            }
        }
    }
}
