import java.util.*;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        return 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int target = Integer.parseInt(flds[0].replace("[[", ""));
        int[] position = ml.stringToIntArray(flds[1]);
        int[] speed = ml.stringToIntArray(flds[2].replace("]]", ""));
        System.out.println("target = " + Integer.toString(target)
                         + ", position = " + ml.intArrayToString(position)
                         + ", speed = " + ml.intArrayToString(speed));

        long start = System.currentTimeMillis();

        int result = carFleet(target, position, speed);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
