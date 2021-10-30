import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        // 3ms
        int even_sum = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                even_sum += num;
            }
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int val = queries[i][0];
            int index = queries[i][1];
			even_sum -= (((nums[index]+1)&1) * nums[index]);
            nums[index] = (nums[index] + val);
			even_sum += (((nums[index]+1)&1) * nums[index]);
            ans[i] = even_sum;
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        String flds0 = flds[0].replace("[", "");
        int[] nums = ml.stringToIntArray(flds0);

        String[] flds1 = flds[1].split("\\]\\]\\]");
        int[][] queries;
        if (flds1[0].length() == 0) {
            queries = new int[][]{};
        } else {
            queries = ml.stringToIntIntArray(flds1[0].split("\\],\\["));
        }
        System.out.println("nums = " + ml.intArrayToString(nums) + ", queries = " + ml.intIntArrayToString(queries));

        long start = System.currentTimeMillis();

        int[] result = sumEvenAfterQueries(nums, queries);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
