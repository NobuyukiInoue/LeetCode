import java.util.*;

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int pos = Arrays.binarySearch(nums,target);
        if (pos < 0) {
            return new int[] {-1, -1};
        }
        
        int left = pos;
        for (int i = left; i >= 0; i = Arrays.binarySearch(nums, 0, i, target)) {
            left = i;
        }
        
        int right = pos;
        for(int i = right; i >= 0; i = Arrays.binarySearch(nums, i + 1, nums.length, target)) {
            right = i;
        }
        return new int[] {left, right};
    }

    public String int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        String[] data;
        
        int[] nums = ml.str_to_int_array(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.output_int_array(nums));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        int[] result = searchRange(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + int_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
