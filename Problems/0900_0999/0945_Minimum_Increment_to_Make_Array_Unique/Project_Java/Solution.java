import java.util.*;

public class Solution {
    public int minIncrementForUnique(int[] A) {
        // 11ms
        Arrays.sort(A);
        int last = Integer.MIN_VALUE;
        int res = 0;
        for (int a : A) {
            if (a <= last) {
                last++;
                res += last - a;
            } else {
                last = a;
           }
        }
        return res;
    }

    public int minIncrementForUnique2(int[] A) {
        // 13ms
        Arrays.sort(A);
        int res = 0, need = 0;
        for (int a : A) {
            res += Math.max(need - a, 0);
            need = Math.max(a, need) + 1;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();

        int result = minIncrementForUnique(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
