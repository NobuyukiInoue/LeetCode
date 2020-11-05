import java.util.*;

public class Solution {
    public List<String> buildArray(int[] target, int n) {
        // 0ms
        List<String> res = new ArrayList<>();
        int pos = 1, i = 0;

        while (i < target.length) {
            if (target[i] == pos) {
                res.add("Push");
                i++;
            } else {
                res.add("Push");
                res.add("Pop");
            }
            pos++;
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] target = ml.stringToIntArray(flds[0]);
        int n = Integer.parseInt(flds[1]);

        System.out.println("target = " + ml.intArrayToString(target));
        System.out.println("n = " + String.valueOf(n));

        long start = System.currentTimeMillis();

        List<String> result = buildArray(target, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
