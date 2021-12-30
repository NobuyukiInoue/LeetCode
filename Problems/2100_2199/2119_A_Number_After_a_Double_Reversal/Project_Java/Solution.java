import java.util.*;

public class Solution {
    public boolean isSameAfterReversals(int num) {
        // 0ms
        return num == 0 || num % 10 != 0;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        boolean result = isSameAfterReversals(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
