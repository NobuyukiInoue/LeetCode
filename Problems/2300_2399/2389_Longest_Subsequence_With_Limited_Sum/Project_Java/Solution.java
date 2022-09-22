import java.util.*;

public class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        // 4ms - 16ms
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        int res[] = new int[queries.length];
        for (int i = 0; i < res.length; ++i) {
            int j = Arrays.binarySearch(nums, queries[i]);
            res[i] = Math.abs(j + 1);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int[] queries = ml.stringToIntArray(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + ml.intArrayToString(queries));

        long start = System.currentTimeMillis();

        int[] result = answerQueries(nums, queries);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
