import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        // 0ms
        List<List<Integer>> ans = new ArrayList<>();
        combination(ans, new ArrayList<Integer>(), k, 1, n);
        return ans;
    }
    
    private void combination(List<List<Integer>> ans, List<Integer> comb, int k,  int start, int n) {
        if (comb.size() == k && n == 0) {
            List<Integer> li = new ArrayList<Integer>(comb);
            ans.add(li);
            return;
        }
        for (int i = start; i <= 9; i++) {
            comb.add(i);
            combination(ans, comb, k, i + 1, n - i);
            comb.remove(comb.size() - 1);
        }
    }

    public String listListArrayToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + listArrayToString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + listArrayToString(list.get(i));
        }

        return resultStr + "]";
    }

    
    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        int k = Integer.parseInt(flds[0]);
        int n = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        List<List<Integer>> result = combinationSum3(k, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listListArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
