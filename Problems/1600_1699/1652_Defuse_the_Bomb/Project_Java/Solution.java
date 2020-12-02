import java.util.*;

public class Solution {
    public int[] decrypt(int[] code, int k) {
        // 0ms
        int[] res = new int[code.length];

        if (k == 0)
            return res;

        int start = 1, end = k, sum = 0;

        if (k < 0) {
            k = -k;
            start = code.length - k;
            end = code.length - 1;
        }

        for (int i = start; i <= end; i++)
            sum += code[i];

        for (int i = 0; i < code.length; i++) {
            res[i] = sum;
            sum -= code[(start++) % code.length];
            sum += code[(++end) % code.length];
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] code = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("code = " + ml.intArrayToString(code) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int[] result = decrypt(code, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
