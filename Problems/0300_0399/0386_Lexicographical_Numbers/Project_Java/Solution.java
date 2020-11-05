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

    public void Main(String temp) {
        String fld = temp.replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        List<Integer> result = lexicalOrder(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
