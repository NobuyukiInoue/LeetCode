import java.util.*;

public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // 1ms
        List<int[]> result = new ArrayList<>();
        boolean added = false;
        for (int[] interval : intervals) {
            if ((interval[1] < newInterval[0])) {
                result.add(interval);
            } else if (interval[0] > newInterval[1]) {
                if (!added) {
                    result.add(newInterval);
                    added = true;
                }
                result.add(interval);
            } else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }
        if (!added) {
            result.add(newInterval);
        }
        return result.toArray(new int[result.size()][]);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[[", "").trim().split("\\]],\\[");
        Mylib ml = new Mylib();
        String[] data0 = flds[0].split("\\],\\[");
        int[][] intervals = ml.stringToIntIntArray(data0);
        int[] newInterval = ml.stringToIntArray(flds[1].replace("]]", ""));

        System.out.println("intervals = " + ml.intIntArrayToString(intervals));
        System.out.println("newInterval = " + ml.intArrayToString(newInterval));

        long start = System.currentTimeMillis();

        int[][] result = insert(intervals, newInterval);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
