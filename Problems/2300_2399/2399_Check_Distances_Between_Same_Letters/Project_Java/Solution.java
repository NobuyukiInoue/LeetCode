import java.util.*;

public class Solution {
    public boolean checkDistances(String s, int[] distance) {
        // 1ms - 2ms
        for (int i = 0; i < 26; i++) {
            char ch = (char)('a' + i);
            int p1 = s.indexOf(ch);
            if (p1 == -1) {
                continue;
            }
            int p2 = s.lastIndexOf(ch);
            if (p2 == -1) {
                continue;
            }
            if (p2 - p1 != distance[i] + 1) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        Mylib ml = new Mylib();
        int[] distance = ml.stringToIntArray(flds[1]);
        System.out.println("s = " + s + ", distance = " + ml.intArrayToString(distance));

        long start = System.currentTimeMillis();

        Boolean result = checkDistances(s, distance);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
