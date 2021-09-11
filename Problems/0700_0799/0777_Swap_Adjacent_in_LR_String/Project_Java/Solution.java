import java.util.*;

public class Solution {
    public boolean canTransform(String start, String end) {
        // 5ms
        if (!start.replace("X", "").equals(end.replace("X", ""))) {
            return false;
        }
        int pointer1 = 0;
        int pointer2 = 0;
        int m = start.length(), n = end.length();
        while (pointer1 < m && pointer2 < n) {
            while (pointer1 < m && start.charAt(pointer1) == 'X') {
                pointer1 += 1;
            }
            while (pointer2 < n && end.charAt(pointer2) == 'X') {
                pointer2 += 1;
            }
            if (pointer1 == m && pointer2 == n) {
                return true;
            }
            if (pointer1 == m || pointer2 == n) {
                return false;
            }
            if (start.charAt(pointer1) != end.charAt(pointer2)) {
                return false;
            }
            if (start.charAt(pointer1) == 'L' && pointer2 > pointer1) {
                return false;
            }
            if (end.charAt(pointer2) == 'R' && pointer1 > pointer2) {
                return false;
            }
            pointer1 += 1;
            pointer2 += 1;
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String v_start = flds[0];
        String v_end = flds[1];
        System.out.println("v_start = " + v_start + ", v_end = " + v_end);

        long start = System.currentTimeMillis();

        boolean result = canTransform(v_start, v_end);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
