public class Mylib {
    public int[] stringTointArray(String s) {
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
        if (nums == null)
            return "";
        if (nums.length <= 0)
            return "";

        StringBuilder resultStr = new StringBuilder("[" +  Integer.toString(nums[0]));

        for (int i = 1; i < nums.length; ++i)
            resultStr.append("," + Integer.toString(nums[i]));

        return resultStr.append("]").toString();
    }
}
