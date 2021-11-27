import java.util.*;

public class Solution {
    public int getLastMoment(int n, int[] left, int[] right) {
        // 0ms
        int res = 0;
        for (int i: left)
            res = Math.max(res, i);
        for (int i: right)
            res = Math.max(res, n - i);
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);

        int[] left, right;
        if (flds[1].length() > 0)
            left = ml.stringToIntArray(flds[1]);
        else
            left = new int[0];
        if (flds[2].length() > 0)
            right = ml.stringToIntArray(flds[2]);
        else
            right = new int[0];

        System.out.println("n = " + Integer.toString(n) 
                       + ", left = " + ml.intArrayToString(left)
                       + ", right = " + ml.intArrayToString(right));

        long start = System.currentTimeMillis();

        int result = getLastMoment(n, left, right);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
