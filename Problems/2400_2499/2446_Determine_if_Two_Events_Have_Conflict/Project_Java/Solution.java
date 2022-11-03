import java.util.*;

public class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        // 0ms - 1ms
        return event1[0].compareTo(event2[1]) <= 0 && event2[0].compareTo(event1[1]) <= 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");
        String[] event1 = flds[0].split(",");
        String[] event2 = flds[1].split(",");
        Mylib ml = new Mylib();
        System.out.println("event1 = " + ml.stringArrayToString(event1) + ", event2 = " + ml.stringArrayToString(event2));

        long start = System.currentTimeMillis();

        boolean result = haveConflict(event1, event2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
