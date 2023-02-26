import java.util.*;

public class Solution {
    public int hIndex(int[] citations) {
        // 0ms
        int len = citations.length;
        int low = 0;
        int high = len;
        while (low < high) {
            int mid = (low + high) >>> 1;
            int k = len - mid;
            if (k > citations[mid]) {
                low = mid + 1;
            } else if (mid == 0 || k < citations[mid - 1]) {
                high = mid;
            } else {
                return k;
            }
        }
        return len - low;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] citations = ml.stringToIntArray(flds);
        System.out.println("citations = " + ml.intArrayToString(citations));

        long start = System.currentTimeMillis();

        int result = hIndex(citations);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
