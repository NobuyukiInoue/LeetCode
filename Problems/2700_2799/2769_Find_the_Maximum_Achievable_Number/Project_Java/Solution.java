import java.util.*;

public class Solution {
    public int theMaximumAchievableX(int num, int t) {
        // 2ms
        return num + 2*t;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int num = Integer.parseInt(flds[0]);
        int t = Integer.parseInt(flds[1]);
        System.out.println("num = " + num + ", t = " + t);
 
        long start = System.currentTimeMillis();

        int result = theMaximumAchievableX(num, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
