import java.util.*;

public class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        // 44ms - 45ms
        int s_len = s.length();
        int[] ans = new int[s_len];
        for (int i = 0; i < s_len; i++) {
            ans[i] = helper(n, startPos[1], startPos[0], s.substring(i));
        }
        return ans;
    }

    private int helper(int n, int x, int y, String s) {
        int cnt = 0;
        for (char inst : s.toCharArray()) {
            if (inst == 'L')
                x--;
            else if (inst == 'R')
                x++;
            else if (inst == 'U')
                y--;
            else if (inst == 'D')
                y++;
            if (x < 0 || y < 0 || x == n || y == n)
                break;
            cnt++;
        }
        return cnt;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);
        int[] startPos = ml.stringToIntArray(flds[1]);
        String s = flds[2];
        System.out.println("n = " + n + ", startPos = " + ml.intArrayToString(startPos) + ", s = \"" + s + "\"");
 
        long start = System.currentTimeMillis();

        int[] result = executeInstructions(n, startPos, s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
