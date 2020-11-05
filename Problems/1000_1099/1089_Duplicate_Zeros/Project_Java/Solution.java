import java.util.*;

public class Solution {
    public void duplicateZeros(int[] arr) {
        int countZero = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) countZero++;
        }

        int len = arr.length + countZero;
        for (int i = arr.length - 1, j = len - 1; i < j; i--, j--) {
            if (arr[i] != 0) {
                if (j < arr.length)
                    arr[j] = arr[i];
            } else {
                if (j < arr.length)
                    arr[j] = arr[i];
                j--;
                if (j < arr.length)
                    arr[j] = arr[i];
            }
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        duplicateZeros(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(arr));
        System.out.println((end - start)  + "ms\n");
    }
}
