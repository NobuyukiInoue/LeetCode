import java.util.*;

public class Solution {
    public int maxDistToClosest(int[] seats) {
        int i, j, res = 0, n = seats.length;
        for (i = j = 0; j < n; ++j)
            if (seats[j] == 1) {
                if (i == 0)
                    res = j;
                else
                    res = Math.max(res, (j - i + 1) / 2);
                i = j + 1;
            }
        res = Math.max(res, n - i);
        return res;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] seats = ml.stringTointArray(flds);

        System.out.println("seats = " + ml.intArrayToString(seats));

        long start = System.currentTimeMillis();
        
        int result = maxDistToClosest(seats);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
