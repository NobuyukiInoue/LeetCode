import java.util.*;

public class Solution {
    public int maxProduct(int[] nums) {
        // 2ms
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int[] maxP = new int[nums.length];
        int[] minP = new int[nums.length];
        maxP[0] = nums[0];
        minP[0] = nums[0];
        int res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            maxP[i] = Math.max(Math.max(maxP[i - 1] * nums[i], minP[i - 1]*nums[i]), nums[i]);
            minP[i] = Math.min(Math.min(maxP[i - 1] * nums[i], minP[i - 1]*nums[i]), nums[i]);
            res = Math.max(res, maxP[i]);
        }
        return res;
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public String listArrayToString(List<Integer> list) {
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

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        int result = maxProduct(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
