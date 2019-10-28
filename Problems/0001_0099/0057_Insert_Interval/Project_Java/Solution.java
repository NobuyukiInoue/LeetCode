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
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[[", "").trim().split("\\]],\\[");
        Mylib ml = new Mylib();
        String[] data0 = flds[0].split("\\],\\[");
        int[][] intervals = new int[data0.length][];

        for (int i = 0; i < data0.length; i++) {
            intervals[i] = ml.str_to_int_array(data0[i]);
        }
        int[] newInterval = ml.str_to_int_array(flds[1].replace("]]", ""));

        System.out.println("intervals = " + intintArrayToString(ml, intervals));
        System.out.println("newInterval = " + ml.output_int_array(newInterval));

        long start = System.currentTimeMillis();

        int[][] result = insert(intervals, newInterval);

        long end = System.currentTimeMillis();

        System.out.println("result = " + intintArrayToString(ml, result));
        System.out.println((end - start)  + "ms\n");
    }
}
