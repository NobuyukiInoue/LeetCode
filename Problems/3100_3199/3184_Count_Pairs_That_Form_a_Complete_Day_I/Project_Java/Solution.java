import java.util.*;

public class Solution {
    public int countCompleteDayPairs(int[] hours) {
        // 1ms
        int cnt = 0;
        for (int i = 0; i < hours.length - 1; i++) {
            for (int j = i + 1; j < hours.length; j++) {
                if ((hours[i] + hours[j])%24 == 0) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] hours = ml.stringToIntArray(flds);
        System.out.println("hours = " + ml.intArrayToString(hours));

        long start = System.currentTimeMillis();

        int result = countCompleteDayPairs(hours);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
