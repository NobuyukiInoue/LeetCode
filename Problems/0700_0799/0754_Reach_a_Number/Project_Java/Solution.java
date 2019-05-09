import java.util.*;

public class Solution {
    public int reachNumber(int target) {
        target = Math.abs(target);
        int sqrt = (int) Math.sqrt(2*target);

        if (sqrt*(sqrt+1) < 2*target)
            sqrt++;
        if (target%2 == 0) {
            while (sqrt % 4 != 0 && (sqrt + 1) % 4 != 0 )
                sqrt++;
        } else {
            while (sqrt % 4 == 0 || (sqrt + 1) % 4 == 0 )
                sqrt++;
        }
        return sqrt;
    }

    public String strarray2string(String[] list) {
        if (list.length < 0)
            return "";

        String result = list[0];
        for (int i = 1; i < list.length; i++) {
            result += "," + list[i];
        }

        return result.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int target = Integer.parseInt(flds);
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();
        
        int result = reachNumber(target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
