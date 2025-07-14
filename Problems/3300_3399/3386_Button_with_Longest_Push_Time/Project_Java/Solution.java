import java.util.*;

public class Solution {
    public int buttonWithLongestTime(int[][] events) {
        // 0ms
        int ans = events[0][0], p_time = events[0][1];
        int mx = p_time;
        for (int[] cur : events) {
            int diff = cur[1] - p_time;
            if (diff > mx) {
                mx = diff;
                ans = cur[0];
            } else if (diff == mx && cur[0] < ans) {
                ans = cur[0];
            }
            p_time = cur[1];
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] events = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("events = " + ml.intIntArrayToString(events));

        long start = System.currentTimeMillis();

        int result = buttonWithLongestTime(events);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
