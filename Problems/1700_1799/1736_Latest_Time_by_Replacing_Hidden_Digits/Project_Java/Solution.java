import java.util.*;

public class Solution {
    public String maximumTime(String time) {
        // 0ms
        char[] times = time.toCharArray();

        if (times[0] == '?')
            times[0] = (times[1] <= '3' || times[1] == '?') ? '2' : '1';
        if (times[1] == '?')
            times[1] = times[0] == '2' ? '3' : '9';
        if (times[3] == '?')
            times[3] = '5';
        if (times[4] == '?')
            times[4] = '9';

        return new String(times);
    }

    public void Main(String temp) {
        String time = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("time = " + time);

        long start = System.currentTimeMillis();

        String result = maximumTime(time);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
