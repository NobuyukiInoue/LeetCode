import java.util.*;

public class Solution {
    public String addSpaces(String s, int[] spaces) {
        // 50ms - 51ms
        StringBuilder sb = new StringBuilder();
        int pre = 0;
        for (int pos : spaces) {
            sb.append(s.substring(pre, pos) + " ");
            pre = pos;
        }
        sb.append(s.substring(pre));
        return sb.toString();
    }

    public String addSpaces2(String s, int[] spaces) {
        // 1176ms
        StringBuilder sb = new StringBuilder(s);
        int step = 0;
        for (int pos: spaces) {
            sb.insert(pos + step, " ");
            step++;
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        int[] spaces = ml.stringToIntArray(flds[1]);

        System.out.println("s = \"" + s + "\", spaces = " + ml.intArrayToString(spaces));
        long start = System.currentTimeMillis();

        String result = addSpaces(s, spaces);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
