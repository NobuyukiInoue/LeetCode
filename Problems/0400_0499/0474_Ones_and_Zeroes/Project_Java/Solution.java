import java.util.*;

public class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        // 32ms
        int [][] dp = new int [m + 1][n + 1];
        for(String curr: strs){
            int zeroCount = getCount(curr);
            int oneCount = curr.length() - zeroCount;
            for(int i = m; i >= zeroCount;i--) {
                for(int j = n; j >= oneCount; j--) {
                    dp[i][j] = Math.max(dp[i][j], 1 + dp[i - zeroCount][j - oneCount]);
                }
            } 
        }
        return dp[m][n];   
    }
        
    private int getCount(String curr){
        int res = 0;
        for (int i = 0; i < curr.length(); i++) {
            if (curr.charAt(i) == '0') {
                res++;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String[] strs = flds[0].split(",");
        int m = Integer.parseInt(flds[1]);
        int n = Integer.parseInt(flds[2]);

        System.out.println("strs = " + ml.stringArrayToString(strs) 
                       + ", m = " + Integer.toString(m)
                       + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = findMaxForm(strs, m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
