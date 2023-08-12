import java.util.*;

public class Solution {
    // 1ms
    List<Integer> res;
    int k;

    public int[] numsSameConsecDiff(int n, int k) {
        res = new ArrayList<>();
        this.k = k;
        for (int i = 1; i < 10; i++) {
            df(i, n - 1, i);
        }
        int[] ans = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }
        return ans;
    }

    private void df(int i, int n, int val) {
        if (n == 0) {
            res.add(val);
            return;
        }
        if (i - k >= 0) {
            df(i - k, n - 1, val*10 + i - k);
        }
        if (k != 0 && (i + k <= 9)) {
            df(i + k, n - 1, val*10 + i + k);
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int[] result = numsSameConsecDiff(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
