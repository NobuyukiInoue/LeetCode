import java.util.*;

public class Solution {
    public int minOperations(String[] logs) {
        // 1ms
        int depth = 0;
        for (String log : logs) {
            if (log.equals("../")) {
                if (depth > 0) {
                    depth--;
                }
            } else if (log.indexOf("./") < 0) {
                depth++;
            }
        }

        return depth;
    }

    public void Main(String temp) {
        String[] logs = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("logs = " + ml.stringArrayToString(logs));

        long start = System.currentTimeMillis();

        int result = minOperations(logs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
