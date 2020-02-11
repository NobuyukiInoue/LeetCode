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

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] candidates = mc.stringTointArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("candidates = " + mc.intArrayToString(candidates) + ", target = " + String.valueOf(target));
        
        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = combinationSum(candidates, target);

        long end = System.currentTimeMillis();

        System.out.print("result = [");
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.print(List_array_to_String(result.get(i)));
            else
                System.out.print("," + List_array_to_String(result.get(i)));
        }
        System.out.println("]");

        System.out.println((end - start)  + "ms\n");
    }
}
