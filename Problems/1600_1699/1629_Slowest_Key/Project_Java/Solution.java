import java.util.*;

public class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        // 0ms
        int maxDiff = releaseTimes[0];
        char result = keysPressed.charAt(0);
        for (int i = 1; i < releaseTimes.length; i++) {
            int diff = releaseTimes[i] - releaseTimes[i - 1];
            if (diff >= maxDiff) {
                char currChar = keysPressed.charAt(i);
                if (diff > maxDiff || currChar > result) {
                    result = currChar;
                }
                maxDiff = diff;
            }
        }
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[");
        String releaseTimesStr = flds[0].replace("[[", "");

        Mylib ml = new Mylib();
        int[] releaseTimes = ml.stringToIntArray(releaseTimesStr);
        String keysPressed = flds[1].replace("]]", "");

        System.out.println("releaseTimesStr[] = " + ml.intArrayToString(releaseTimes));
        System.out.println("keysPressed = " + keysPressed);

        long start = System.currentTimeMillis();

        char result = slowestKey(releaseTimes, keysPressed);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Character.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
