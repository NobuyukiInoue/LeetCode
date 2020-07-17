import java.util.*;

public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        // 5ms
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> stack = new ArrayList<Integer>();
        int x = 1;
        while (true) {
            int stackLength = stack.size();
            if (stackLength == k) {
                List<Integer> temp = new ArrayList<Integer>(stack);
                ans.add(temp);
            }
            if (stackLength == k || x > n - k + stackLength + 1) {
                if (stack.size() == 0) {
                    return ans;
                }
                x = stack.get(stackLength - 1) + 1;
                stack.remove(stackLength - 1);
            } else {
                stack.add(x);
                x++;
            }
        }
    }

    public List<List<Integer>> combine2(int n, int k) {
        // 73ms
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        dfs(n, k, new ArrayList<Integer>(), 0, 1, ans);
        return ans;
    }

    public void dfs(int n, int count, List<Integer>cur, int i, int j, List<List<Integer>>ans) {
        if (i == count) {
            List<Integer> temp = new ArrayList<Integer>(cur);
            ans.add(temp);
        }
        for (int x = j; x <= n; x++) {
            List<Integer> temp = new ArrayList<Integer>(cur);
            temp.add(x);
            dfs(n, count, temp, i + 1, x + 1, ans);
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
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + Integer.toString(n) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = combine(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listListArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
