import java.util.*;

public class Solution {
    public int[][] merge(int[][] intervals) {
        // 2ms
        int n = intervals.length;
        int[] starts = new int[n];
        int[] ends = new int[n];

        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }

        Arrays.sort(starts);
        Arrays.sort(ends);

        List<int[]> result = new ArrayList<int[]>();
        for (int i = 0, j = 0; i < n; i++) {
            if (i == n - 1 || starts[i + 1] > ends[i]) {
                result.add(new int[] {starts[j], ends[i]});
                j = i + 1;
            }
        }
        return result.toArray(new int[result.size()][]);
    }

    public int[][] merge2(int[][] intervals) {
        // 37ms
        if (intervals.length <= 1)
            return intervals;

        // Sort by ascending starting point
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

        List<int[]> result = new ArrayList<>();
        int[] newInterval = intervals[0];
        result.add(newInterval);
        for (int[] interval : intervals) {
            if (interval[0] <= newInterval[1]) // Overlapping intervals, move the end if needed
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            else {                             // Disjoint intervals, add the new interval to the list
                newInterval = interval;
                result.add(newInterval);
            }
        }

        return result.toArray(new int[result.size()][]);
    }

    public String intintArrayToString(Mylib ml, int[][] list) {
        if (list == null)
            return "[]";

        if (list.length <= 0)
            return "[]";

        String resultStr = "[" + ml.output_int_array(list[0]);
        for (int i = 1; i < list.length; i++) {
                resultStr += ",[" + ml.output_int_array(list[i]) + "]";
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] intervals = new int[flds.length][];
        for (int i = 0; i < flds.length; i++) {
            intervals[i] = ml.str_to_int_array(flds[i]);
        }

        System.out.println("intervals = " + intintArrayToString(ml, intervals));

        long start = System.currentTimeMillis();

        int[][] result = merge(intervals);

        long end = System.currentTimeMillis();

        System.out.println("result = " + intintArrayToString(ml, result));
        System.out.println((end - start)  + "ms\n");
    }
}
