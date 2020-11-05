public class Solution {
    public boolean checkPossibility(int[] nums) {
        int count_dec = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i+1]) {
                count_dec++;
                if (i == 0)
                    nums[i] = nums[i+1];
                else if (nums[i-1] <= nums[i+1])
                    nums[i] = nums[i-1];
                else
                    nums[i+1] = nums[i];
            }
            if (count_dec > 1) {
                return false;
            }
        }
    
        return true;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums[] = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = checkPossibility(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
