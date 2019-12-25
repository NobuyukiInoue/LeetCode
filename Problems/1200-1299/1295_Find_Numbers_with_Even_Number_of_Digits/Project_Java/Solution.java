public class Solution {

    public int findNumbers(int[] nums) {
        // 1ms
        int result = 0;
        for (int target : nums) {
            if (Integer.toString(target).length() % 2 == 0)
                result++;
        }
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] nums = mc.str_to_int_array(flds);

        System.out.println("nums = " + mc.output_int_array(nums));

        long start = System.currentTimeMillis();

        int result = findNumbers(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
