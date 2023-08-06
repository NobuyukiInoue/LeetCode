import java.util.*;

public class Solution {
    int mod = 1000000000 + 7;
    Long[][][][] dp;
        
    public int countSteppingNumbers(String low, String high) {
        dp = new Long[high.length()][2][2][10];
        long x = sol(0, 0, 0, 0, high);
        dp = new Long[high.length()][2][2][10];
        long y = sol(0, 0, 0, 0, low);
        long z = check(low) ? 1 : 0;
        return (int)((x - y + mod + z) % mod);
    }
    
    boolean check(String num) {
        for (int i = 0; i < num.length() - 1; i++) {
            int x = num.charAt(i) - '0';
            int y = num.charAt(i + 1) - '0';
            if (Math.abs(x - y) != 1)
                return false;
        }
        return true;
    }
    
    long sol(int idx, int f, int c, int p, String s) {
        if (idx == s.length()) {
            return 1;
        }
        if (dp[idx][f][c][p] != null)
            return dp[idx][f][c][p];

        int l = s.charAt(idx) - '0';
        if (f == 1)
            l = 9;

        long ans = 0;
        for (int d = 0; d <= l; d++) {
            if (c == 0 || Math.abs(p - d) == 1) {
                if (f == 1) {
                    ans = (ans + sol(idx + 1, 1, d == 0 ? c : 1, d, s)) % mod;
                } else {
                    if (d == l) {
                        ans = (ans + sol(idx + 1, 0, d == 0 ? c : 1, d, s))%mod;
                    } else {
                        ans = (ans + sol(idx + 1, 1, d == 0 ? c : 1, d, s))%mod;
                    }
                }
            }
        }
        return  dp[idx][f][c][p] = ans;
    }

    /*
    // Time Limite Exceeded. 2402/2522

    int mod = 1000000000 + 7;
    String g_low, g_high;
    public int countSteppingNumbers(String low, String high) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < high.length() - low.length(); i++) {
           sb.append("0");
        }
        g_low = sb.toString() + low;
        g_high = high;
        return dfs(0, false, false, -1, false);
    }

    private int dfs(int i, boolean is_greater_thn_low, boolean is_less_thn_high, int prev_digit, boolean nonzero) {
          if (i == g_high.length())
              return 1;
          int total = 0;
          int start = is_greater_thn_low == false ? (g_low.charAt(i) - '0') : 0;
          int end = is_less_thn_high == false ? (g_high.charAt(i) - '0' + 1) : 10;
          for (int nx_digit = start; nx_digit < end; nx_digit++) {
              if (!nonzero || Math.abs(prev_digit - nx_digit) == 1) {
                  total += dfs(i + 1, is_greater_thn_low || nx_digit > (g_low.charAt(i) - '0'), is_less_thn_high || nx_digit < (g_high.charAt(i) - '0'), nx_digit, nonzero || nx_digit != 0);
              }
          }
          return total%mod;
    }
    */

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String low = flds[0];
        String high = flds[1];
        System.out.println("low = " + low + ", high = " + high);

        long start = System.currentTimeMillis();

        int result = countSteppingNumbers(low, high);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
