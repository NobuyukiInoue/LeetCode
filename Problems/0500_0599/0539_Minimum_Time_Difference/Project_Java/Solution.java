import java.util.*;

public class Solution {
    public int findMinDifference(List<String> timePoints) {
        // 1ms
        boolean[] visited = new boolean[24 * 60];
        for (String time : timePoints) {
            int h = Integer.parseInt(time.substring(0, 2));
            int m = Integer.parseInt(time.substring(3));
            if (visited[h * 60 + m])
                return 0;
            visited[h * 60 + m] = true;
        }

        int prev = 0, min = Integer.MAX_VALUE;
        int first = 0, last = 0;
        int idx = visited.length - 1;
        while (!visited[idx]) {
            idx--;
        }

        last = idx;
        idx = 0;
        while (!visited[idx])
            idx++;

        first = idx;
        prev = first;
        for (int i = first + 1; i <= last; i++){
            if (visited[i]){
                min = Math.min(min, i - prev);
                prev = i;
            }
        }

        min = Math.min(min, (24 * 60 - last + first));
        return min;
    }

    public int findMinDifference2(List<String> timePoints) {
        // 6ms
        int[] timePointsInt = new int[timePoints.size()];
        for (int i = 0; i < timePoints.size(); i++) {
            String[] t = timePoints.get(i).split(":");
            int h = Integer.parseInt(t[0]);
            int m = Integer.parseInt(t[1]);
            timePointsInt[i] = h*60 + m;
        }

        Arrays.sort(timePointsInt);

        int minimum = 1440;
        int diff;
        for (int i = 1; i < timePointsInt.length; i++) {
            diff = timePointsInt[i] - timePointsInt[i - 1];
            minimum = Math.min(minimum, diff);
        }

        diff = timePointsInt[0] - timePointsInt[timePointsInt.length - 1] + 1440;

        return Math.min(minimum, diff);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        List<String> timePoints = ml.stringArrayToListStringArray(flds.split(","));
        System.out.println("timePoints = " + ml.listStringArrayToString(timePoints));

        long start = System.currentTimeMillis();

        int result = findMinDifference(timePoints);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
