import java.util.*;

public class Solution {
    public int[] decompressRLElist(int[] nums) {
        // 1ms
        int count = 0;
        for(int i = 0; i < nums.length; i += 2){
            count += nums[i];
        }
        int[] ans = new int[count];
        int st = 0;
        for(int j = 1; j < nums.length; j += 2){
            Arrays.fill(ans, st, st + nums[j - 1], nums[j]);
            st += nums[j - 1];
        }
        return ans;
    }

    public int[] decompressRLElist2(int[] nums) {
        // 3ms
		int len = 0;
        for (int i = 0; i < nums.length; i += 2)
            len += nums[i];
        int[] res = new int[len];
        int p = 0;
        for (int i = 0; i < nums.length; i += 2) {
			for (int j = 0; j < nums[i]; j++) {
                res[p++] = nums[i + 1];
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = decompressRLElist(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
