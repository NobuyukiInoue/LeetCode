import java.util.*;

public class Solution {
    public int findKthPositive(int[] arr, int k) {
        // 0ms
        int count = 0, index = 0;
        for (int i = 1; i < arr[arr.length - 1]; i++) {
            if (i < arr[index]) {
                count++;
                if (count == k) {
                    return i;
                }
            } else {
                index++;
            }
        }
        return arr[arr.length - 1] + k - count;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringTointArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = findKthPositive(arr, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
