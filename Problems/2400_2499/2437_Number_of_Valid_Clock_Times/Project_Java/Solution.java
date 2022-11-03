import java.util.*;

public class Solution {
    public int countTime(String time) {
        // 0ms
        int res = 1;
        if (time.charAt(0) == '?')
            res = time.charAt(1) == '?' ? 24 : time.charAt(1) < '4' ? 3 : 2;
        else if (time.charAt(1) == '?')
            res = time.charAt(0) < '2' ? 10 : 4; 
        return res * (time.charAt(3) == '?' ? 6 : 1) * (time.charAt(4) == '?' ? 10 : 1);
    }

    public void Main(String temp) {
        String time = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("time = " + time);

        long start = System.currentTimeMillis();

        int result = countTime(time);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
