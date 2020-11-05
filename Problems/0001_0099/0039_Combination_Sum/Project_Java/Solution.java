import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // 2ms
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();

        Arrays.sort(candidates);
        dfs(candidates, target, 0, ans, path);

        return ans;
    }
    
    private void dfs(int[] c, int target, int pos, List<List<Integer>> ans, List<Integer> path) {
        if (target == 0) {
            ans.add(new ArrayList<Integer>(path));
            return;
        }

        for (int i = pos; i < c.length && c[i] <= target; i++) {
            path.add(c[i]);
            dfs(c, target - c[i], i, ans, path);
            path.remove(path.size() - 1);
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] candidates = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("candidates = " + ml.intArrayToString(candidates) + ", target = " + String.valueOf(target));
        
        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = combinationSum(candidates, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
