import java.util.*;

public class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        // 1ms
        int balls[][] = new int[n][11];
        int winner[] = new int[n];
        for (int p[] : pick) {
            balls[p[0]][p[1]]++;
            if (balls[p[0]][p[1]] == p[0] + 1) {
                winner[p[0]] = 1;
            }
        }
        int ans = 0;
        for (int val : winner) {
            if (val == 1) {
                ans++;
            }
        }
        return ans;
    }

    public int winningPlayerCount2(int n, int[][] pick) {
        // 5ms - 6ms
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(i, new HashMap<>());
        }
        for (int[] p : pick) {
            int x = p[0], y = p[1];
            map.get(x).put(y, map.get(x).getOrDefault(y, 0) + 1);
        }
        int ans = 0;
        for (int key : map.keySet()) {
            Map<Integer, Integer> m = map.get(key);
            for (int k : m.keySet()) {
                if (key < m.get(k)) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("]]]", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0].replace("[[", ""));
        int[][] pick = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("n = " + n + ", pick = " + ml.intIntArrayToString(pick));

        long start = System.currentTimeMillis();

        int result = winningPlayerCount(n ,pick);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
