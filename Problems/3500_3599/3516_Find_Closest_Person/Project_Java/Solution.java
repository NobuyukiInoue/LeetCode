import java.util.*;

public class Solution {
    public int findClosest(int x, int y, int z) {
        // 0ms
        int d = (x - y) * (x + y - 2*z);
        return (d != 0 ? 1 : 0) << (d > 0 ? 1 : 0);
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int x = Integer.parseInt(flds[0]);
        int y = Integer.parseInt(flds[1]);
        int z = Integer.parseInt(flds[2]);
        System.out.println("x = " + x + ", y = " + y + ", z = " + z);

        long start = System.currentTimeMillis();

        int result = findClosest(x, y, z);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
