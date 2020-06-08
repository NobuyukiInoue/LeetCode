import java.util.*;

public class Solution {
    public boolean increasingTriplet(int[] nums) {
        // 0ms
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;
        for (int n :  nums) {
            if (n <= first)
                first = n;
            else if (n <= second)
                second = n;
            else
                return true;
        }   
        return false;
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] nums = mc.stringTointArray(flds);
        System.out.println("nums = " + mc.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = increasingTriplet(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
