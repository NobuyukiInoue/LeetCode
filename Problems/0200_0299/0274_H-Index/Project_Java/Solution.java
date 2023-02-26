import java.lang.reflect.Array;
import java.util.*;

public class Solution {
    public int hIndex(int[] citations) {
        // 2ms
        Arrays.sort(citations);
        int n = citations.length;
        int i = 0;
        while (i < n && n - i > citations[i]){
            i++;
        }
        return n - i;
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
