import java.util.*;

public class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        // 0ms
        int count = 0;
        for (int i = 0; i < startTime.length; i++) {
            if (startTime[i] <= queryTime && queryTime <= endTime[i]) {
                count++;
            }
        }
        
        return count;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] startTime = mc.stringTointArray(flds[0]);
        int[] endTime = mc.stringTointArray(flds[1]);
        int queryTime = Integer.parseInt(flds[2]);

        System.out.println("startTime = " + mc.intArrayToString(startTime));
        System.out.println("endTime = " + mc.intArrayToString(endTime));
        System.out.println("queryTime = " + Integer.toString(queryTime));

        long start = System.currentTimeMillis();
        
        int result = busyStudent(startTime, endTime, queryTime);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
