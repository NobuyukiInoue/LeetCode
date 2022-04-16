import java.util.*;

public class Solution {
    public int convertTime(String current, String correct) {
        // 1ms - 3ms
        String[] v1 = current.split(":"), v2 = correct.split(":");
        int minutes = (Integer.parseInt(v2[0])*60 + Integer.parseInt(v2[1])) - (Integer.parseInt(v1[0])*60 + Integer.parseInt(v1[1]));
        int[] ops = new int[] {60, 15, 5 ,1};
        int ans = 0;
        for (int op : ops) {
            ans += minutes / op;
            minutes %= op;
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        String current = flds[0], correct = flds[1];
        System.out.println("current = " + current + ", correct = " + correct);

        long start = System.currentTimeMillis();

        int result = convertTime(current, correct);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
