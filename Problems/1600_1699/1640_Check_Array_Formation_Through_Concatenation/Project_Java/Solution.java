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
        int[] arr = ml.stringTointArray(flds[0].replace("[[",""));
        System.out.println("arr = " + ml.intArrayToString(arr));

        String[] piecesStr = flds[1].replace("]]]", "").split("\\],\\[");
        int[][] pieces = new int[piecesStr.length][];
        System.out.print("pieces = [");
        for (int i = 0; i < pieces.length; i++) {
            pieces[i] = ml.stringTointArray(piecesStr[i]);
            if (i == 0)
                System.out.print(ml.intArrayToString(pieces[i]));
            else
                System.out.print(", " + ml.intArrayToString(pieces[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        boolean result = canFormArray(arr, pieces);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
