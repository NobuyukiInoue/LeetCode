import java.util.*;

public class Solution {
    public int numberOfRounds(String loginTime, String logoutTime) {
        // 1ms
        int ts = 60 * Integer.parseInt(loginTime.substring(0, 2))+ Integer.parseInt(loginTime.substring(3));
        int tf = 60 * Integer.parseInt(logoutTime.substring(0, 2)) + Integer.parseInt(logoutTime.substring(3));
        if (0 <= tf - ts && tf - ts < 15) {
            return 0;
        }
        if (ts > tf) {
            return tf /15 - (ts + 14)/15 + 96;
        }
        return tf /15 - (ts + 14)/15;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String loginTime = flds[0];
        String logoutTime = flds[1];
        System.out.println("loginTime = " + loginTime + ", logoutTime = " + logoutTime);

        long start = System.currentTimeMillis();

        int result = numberOfRounds(loginTime, logoutTime);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
