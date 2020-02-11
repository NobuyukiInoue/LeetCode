public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int maxLoc = 0;
        int start = 0;
        int end = 0;
        int counter = 1;
        while (counter < nums.length) {
            int curr = nums[counter];
            if (curr >= nums[maxLoc]) {
                if(start == end) {
                    start = counter;
                    end = counter;
                }
                maxLoc = counter;
            } else if(curr < nums[maxLoc] && curr > nums[start]) {
                end = counter;
            } else {
                while (start > 0 && nums[start - 1] > curr) {
                    start--;
                }
                end = counter;
            }
            counter++;
        }
        if (end == start) {
            return 0;
        }
        return end - start + 1;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);

        long start = System.currentTimeMillis();

        int result = findUnsortedSubarray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
