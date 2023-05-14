import java.util.*;

public class Solution {
    public int countSeniors(String[] details) {
        // 0ms
        int ans = 0;
        for (String detail : details) {
            int age = (detail.charAt(11) - '0') * 10 + (detail.charAt(12) - '0');
            if (age > 60) {
                ans++;
            }
        }
        return ans;
    }

    public int countSeniors2(String[] details) {
        // 2ms
        int ans = 0;
        for (String detail : details) {
            String tail = detail.substring(11);
            tail = tail.substring(0, tail.length() - 2);
            if (Integer.parseInt(tail) > 60) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] details = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        Mylib ml = new Mylib();
        System.out.println("details = " + ml.stringArrayToString(details));
        long start = System.currentTimeMillis();

        int result = countSeniors(details);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
