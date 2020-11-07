import java.util.*;

public class Solution {
    public int getWinner(int[] arr, int k) {
        // 0ms
        int cur = arr[0];
        int win = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > cur) {
                cur = arr[i];
                win = 0;
            }
            win++;
            if (win == k)
                break;
        }
        return cur;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = getWinner(arr, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
