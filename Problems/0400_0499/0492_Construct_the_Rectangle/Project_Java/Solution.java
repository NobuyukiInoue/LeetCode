import java.util.*;

public class Solution {
    public int[] constructRectangle(int area) {
        int[] result = new int[2];
        if (area == 0) {
            return result;
        }
        int a = (int)Math.sqrt(area);
        while(area%a != 0){
            a--;
        }
        int b = area/a;
        result[0] = b;
        result[1] = a;
        return result;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int area = Integer.parseInt(flds);

        System.out.println("area = " + Integer.toString(area));

        long start = System.currentTimeMillis();

        int[] result = constructRectangle(area);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " +  ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
