import java.util.*;

public class Solution {
    public int maximizeSum(int[] nums, int k) {
        // 3ms
        return myMax(nums)*k+(k - 1)*k/2;
    }

    private int myMax(int []nums) {
        int res = Integer.MIN_VALUE;
        for (int n : nums) {
            if (n > res) {
                res = n;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = maximizeSum(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
