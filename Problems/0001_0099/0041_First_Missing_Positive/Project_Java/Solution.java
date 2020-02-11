import java.util.*;

public class Solution {
    public int firstMissingPositive(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int index = nums[start] - 1;
            if (index == start)
                start++;
            else if (index < 0 || index > end || nums[start] == nums[index])
                nums[start] = nums[end--];
            else {
                nums[start] = nums[index];
                nums[index] = index + 1;
            }
        }
        return start + 1;
    }

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + Int_array_to_String(nums));

        long start = System.currentTimeMillis();
        
        int result = firstMissingPositive(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
