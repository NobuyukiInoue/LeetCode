import java.util.*;

public class Solution {
    public int finalValueAfterOperations(String[] operations) {
        // 0ms
        int ans = 0;
        for (String op : operations) {
            if (op.charAt(1) == '+') {
                ans++;
            } else {
                ans--;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] operations = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("operations = " + ml.stringArrayToString(operations));

        long start = System.currentTimeMillis();

        int result = finalValueAfterOperations(operations);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
