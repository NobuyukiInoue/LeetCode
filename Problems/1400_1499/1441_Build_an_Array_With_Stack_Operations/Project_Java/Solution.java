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

    private String listArrayToString(List<String> data) {
        if (data.size() <= 0)
            return "";

        StringBuilder sb = new StringBuilder("[" + data.get(0));
        for (int i = 1; i < data.size(); i++) {
            sb.append(", " + data.get(i));
        }

        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] target = mc.stringTointArray(flds[0]);
        int n = Integer.parseInt(flds[1]);

        System.out.println("target = " + mc.intArrayToString(target));
        System.out.println("n = " + String.valueOf(n));

        long start = System.currentTimeMillis();
        
        List<String> result = buildArray(target, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
