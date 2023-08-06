import java.util.*;

public class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int ans = 0;
        for (int h : hours) {
            if (h >= target) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] hours = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);
        System.out.println("hours = " + ml.intArrayToString(hours) + ", target = " + target);
 
        long start = System.currentTimeMillis();

        int result = numberOfEmployeesWhoMetTarget(hours, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
