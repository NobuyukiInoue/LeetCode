import java.util.*;

public class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        // 0ms
        for (int[] piece : pieces) {
            if (indexOf(arr, piece[0]) < 0)
                return false;
            int idx = indexOf(arr, piece[0]);
            if (arrayDiff(arr, idx, piece) == false)
                return false;
        }
        return true;
    }

    private int indexOf(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++)
            if (arr[i] == target)
                return i;
        return -1;
    }

    private boolean arrayDiff(int[] arr, int start, int[] targetArr) {
        for (int i = 0; i < targetArr.length; i++) {
            if (i + start > arr.length - 1)
                return false;
            if (arr[i + start] != targetArr[i])
                return false;
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0].replace("[[",""));
        System.out.println("arr = " + ml.intArrayToString(arr));

        String[] piecesStr = flds[1].replace("]]]", "").split("\\],\\[");
        int[][] pieces = ml.stringToIntIntArray(piecesStr);
        System.out.println("pieces = " + ml.intIntArrayToString(pieces));

        long start = System.currentTimeMillis();

        boolean result = canFormArray(arr, pieces);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
