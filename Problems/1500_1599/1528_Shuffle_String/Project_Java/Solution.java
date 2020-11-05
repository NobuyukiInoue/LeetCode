import java.util.*;

public class Solution {
    public String restoreString(String s, int[] indices) {
        // 1ms
        char[] res = new char[s.length()];
        for (int i = 0; i < indices.length; i++) {
            res[indices[i]] = s.charAt(i);
        }
        return new String(res);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String s = flds[0];
        Mylib ml = new Mylib();
        int[] indices = ml.stringToIntArray(flds[1]);
        System.out.println("s = " + s + ", indices = " + ml.intArrayToString(indices));

        long start = System.currentTimeMillis();

        String result = restoreString(s, indices);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
