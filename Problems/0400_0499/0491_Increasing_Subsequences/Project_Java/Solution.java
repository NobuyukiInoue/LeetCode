import java.util.*;

public class Solution {
    List<List<Integer>> ans;
    int[] nums;
    public List<List<Integer>> findSubsequences(int[] nums) {
        // 3ms
        ans = new ArrayList<>();
        this.nums = nums;
        dfs(-1, new ArrayList<>());
        return ans;
    }

    private void dfs(int i, List<Integer> curr) {
        if (curr.size() > 1) {
            ans.add(curr);
        }
        List<Integer> found = new ArrayList<>();
        for (int j = i + 1; j < nums.length; j++) {
            if ((i >= 0 && nums[j] < nums[i]) ||  found.contains(nums[j])) {
                continue;
            }
            List<Integer> temp = new ArrayList<Integer>(curr);
            temp.add(nums[j]);
            dfs(j, temp);
            found.add(nums[j]);
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = findSubsequences(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
