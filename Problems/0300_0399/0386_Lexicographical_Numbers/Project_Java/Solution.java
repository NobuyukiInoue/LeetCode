import java.util.*;

public class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<>();
        dfs(res, n, 1);
        return res;
    }
    
    private void dfs(List<Integer> res, int n, int cur) {
        if(cur > n)
            return;
        res.add(cur);
        dfs(res, n, cur * 10);
        if (cur % 10 < 9)
            dfs(res, n, cur + 1);
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[";
        for (int i = 0; i < list.size(); i++) {
            if (i == 0)
                resultStr += Integer.toString(list.get(i));
            else
                resultStr += "," + Integer.toString(list.get(i));
        }
        return resultStr + "]";
    }

    public void Main(String temp) {
        String fld = temp.replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        List<Integer> result = lexicalOrder(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
