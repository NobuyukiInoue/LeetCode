import java.util.*;

public class Solution {
    public int hardestWorker(int n, int[][] logs) {
        // 1ms - 2ms
        int best_id = 0, best_time = 0, start_time = 0;
        for (int[] log : logs) {
            int time = log[1] - start_time;
            if (time > best_time || (time == best_time && best_id > log[0])) {
                best_id = log[0];
                best_time = time;
            };
            start_time = log[1];
        }
        return best_id;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("]]]", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0].replace("[[", ""));
        int[][] logs = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("n = " + Integer.toString(n) + ", logs = " + ml.intIntArrayToString(logs));

        long start = System.currentTimeMillis();

        int result = hardestWorker(n, logs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
