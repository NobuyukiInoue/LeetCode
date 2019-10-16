public class Mylib {
    public int[] str_to_int_array(String s) {
        if (s.length() <= 0)
            return null;

        String[] flds = s.split(",");
        int[] nums = new int[flds.length];

        if (flds.length <= 0)
            return nums;

        for (int i = 0; i < nums.length; ++i) {
            nums[i] = Integer.parseInt(flds[i]);
        }

        return nums;
    }

    public String intArrayToString(int[] nums) {
        if (nums.length <= 0)
            return "";

        String resultStr = "[" +  Integer.toString(nums[0]);
    
        for (int i = 1; i < nums.length; ++i) {
            resultStr += "," + Integer.toString(nums[i]);
        }

        return resultStr + "]";
    }
}
