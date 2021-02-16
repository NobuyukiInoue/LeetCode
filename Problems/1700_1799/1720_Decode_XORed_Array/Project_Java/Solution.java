import java.util.*;

public class Solution {
    public int[] decode(int[] encoded, int first) {
        // 1ms
        int[] res = new int[encoded.length + 1];
        res[0] = first;

        for (int i = 0; i < encoded.length; i++) {
            res[i + 1] = encoded[i]^res[i];
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] encoded = ml.stringToIntArray(flds[0]);
        int first = Integer.parseInt(flds[1]);
        System.out.println("encoded = " + ml.intArrayToString(encoded) + ", first = " + Integer.toString(first));

        long start = System.currentTimeMillis();

        int[] result = decode(encoded, first);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
