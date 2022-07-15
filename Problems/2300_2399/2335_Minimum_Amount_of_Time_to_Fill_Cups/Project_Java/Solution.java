import java.util.*;

public class Solution {
    public int fillCups(int[] amount) {
        // 0ms
        int m_max = 0, total = 0;
        for (int num : amount) {
            m_max = Math.max(m_max, num);
            total += num;
        }
        return Math.max(m_max, (total + 1)/2);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] amount = ml.stringToIntArray(flds);
        System.out.println("amount = " + ml.intArrayToString(amount));

        long start = System.currentTimeMillis();

        int result = fillCups(amount);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
