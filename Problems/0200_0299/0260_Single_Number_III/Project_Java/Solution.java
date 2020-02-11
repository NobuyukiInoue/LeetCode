import java.util.*;

public class Solution {
    public int[] singleNumber(int[] nums) {
        // 1ms
        int diff = 0;
        for (int num : nums) {
            diff ^= num;
        }
        diff &= -diff;
        
        int[] rets = {0, 0};
        for (int num : nums) {
            if ((num & diff) == 0) {
                rets[0] ^= num;
            } else {
                rets[1] ^= num;
            }
        }
        return rets;
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
        System.out.println("nums = [" + intArrayToString(nums) + "]");

        long start = System.currentTimeMillis();
        
        int[] result = singleNumber(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + intArrayToString(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
