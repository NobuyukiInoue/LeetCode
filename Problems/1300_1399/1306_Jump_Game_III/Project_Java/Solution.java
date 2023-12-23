import java.util.*;

public class Solution {
    public boolean canReach(int[] arr, int start) {
        // 2ms
        if (start < 0 || start >= arr.length || arr[start] < 0) {
            return false;
        }
        arr[start] *= -1;
        return arr[start] == 0 || canReach(arr, start + arr[start]) || canReach(arr, start - arr[start]);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int v_start = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", start = " + v_start);
 
        long start = System.currentTimeMillis();

        boolean result = canReach(arr, v_start);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
