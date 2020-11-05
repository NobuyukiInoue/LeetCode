import java.util.*;

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 26ms
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1;
            int r = nums.length - 1;
            while (l < r) {
                int s = nums[l] + nums[i] + nums[r];
                if (s > 0) {
                    r--;
                } else if (s < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[l], nums[i], nums[r]));
                    while (l < r && nums[l] == nums[l+1])
                        l++;
                    while (l < r && nums[r] == nums[r-1])
                        r--;
                    l = l + 1;
                    r = r - 1;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = threeSum(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
