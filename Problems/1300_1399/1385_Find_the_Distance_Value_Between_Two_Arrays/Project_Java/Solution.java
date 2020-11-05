import java.util.*;

public class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        // 3ms
        int res = 0;
        for (int i = 0; i < arr1.length; i++) {
            for (int j = 0; j < arr2.length; j++) {
                if (myAbs(arr1[i] - arr2[j]) <= d) {
                    break;
                }
                if (j == arr2.length - 1) {
                    res++;
                }
            }
        }
        return res;
    }

    private int myAbs(int val) {
        if (val >= 0)
            return val;
        return -val;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr1 = ml.stringToIntArray(flds[0]);
        int[] arr2 = ml.stringToIntArray(flds[1]);
        int d = Integer.parseInt(flds[2]);

        System.out.println("arr1 = " + ml.intArrayToString(arr1) + ", arr2 = " + ml.intArrayToString(arr2) + ", d = " + Integer.toString(d));

        long start = System.currentTimeMillis();

        int result = findTheDistanceValue(arr1, arr2, d);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
