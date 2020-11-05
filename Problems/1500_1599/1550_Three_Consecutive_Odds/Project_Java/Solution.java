import java.util.*;

public class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        // 0ms
        int i = 0;
        while (i < arr.length - 2) {
            if (arr[i] % 2 == 0) {
                i++;
                continue;
            }
            i++;
            if (arr[i] % 2 == 0)
                continue;
            i++;
            if (arr[i] % 2 == 0)
                continue;
            return true;
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        boolean result = threeConsecutiveOdds(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
