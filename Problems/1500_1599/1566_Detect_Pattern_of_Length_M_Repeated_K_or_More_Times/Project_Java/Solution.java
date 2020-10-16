import java.util.*;

public class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        // 0ms
        int streak = 0;
        for (int i = 0; i < arr.length - m; i++) {
            if (arr[i] == arr[i + m])
                streak = streak + 1;
            else
                streak = 0;

            if (streak == (k - 1)*m)
                return true;
        }

        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringTointArray(flds[0]);
        int m = Integer.parseInt(flds[1]);
        int k = Integer.parseInt(flds[2]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", m = " + m + ", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = containsPattern(arr, m, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
