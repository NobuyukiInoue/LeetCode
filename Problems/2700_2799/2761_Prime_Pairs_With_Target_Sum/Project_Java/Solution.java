import java.util.*;

public class Solution {
    public List<List<Integer>> findPrimePairs(int n) {
        // 125ms - 133ms
        boolean[] lst = new boolean[n + 1];
        for (int i = 2; i < (int)Math.sqrt(lst.length) + 1; i++) {
            if (!lst[i]) {
                for (int j = 2*i; j < lst.length; j += i) {
                    lst[j] = true;
                }
            }
        }
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 2; i < n/2 + 1; i++) {
            int x = i, y = n - i;
            if (!lst[x] &&  !lst[y] && x <= y) {
                ans.add(new ArrayList<Integer>(Arrays.asList(x, y)));
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        List<List<Integer>> result = findPrimePairs(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
