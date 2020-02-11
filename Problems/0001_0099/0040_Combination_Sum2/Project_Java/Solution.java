import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        // 2ms
        List<List<Integer>> res = new ArrayList<>();
        if (candidates.length == 0) {
            return res;
        }
        int n = candidates.length;
        Arrays.sort(candidates);
        boolean[] visited = new boolean[n];
        helper(0, new ArrayList<>(), candidates, target, res, visited);
        return res;
    }

    void helper(int index, List<Integer> list, int[] candidates, int target, List<List<Integer>> res, boolean[] visited) {
        if (target == 0) {
            res.add(new ArrayList<>(list));
            return;
        }
        if (index == candidates.length) {
            return;
        }
        for (int i = index; i < candidates.length; i++) {
            if (i != index && !visited[i - 1] && candidates[i] == candidates[i - 1]) {
                continue;
            }
            if (target < candidates[i]) {
                break;
            }
            visited[i] = true;
            list.add(candidates[i]);
            helper(i + 1, list, candidates, target - candidates[i], res, visited);
            visited[i] = false;
            list.remove(list.size() - 1);
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
        
        List<List<Integer>> result = combinationSum2(candidates, target);

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
