import java.util.*;

public class Solution {
    public int bagOfTokensScore(int[] tokens, int P) {
        // 3ms
        Arrays.sort(tokens);
        int res = 0, points = 0, i = 0, j = tokens.length - 1;
        while (i <= j) {
            if (P >= tokens[i]) {
                P -= tokens[i++];
                res = Math.max(res, ++points);
            } else if (points > 0) {
                points--;
                P += tokens[j--];
            } else {
                break;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Mylib ml = new Mylib();
        int[] tokens = ml.stringToIntArray(flds[0]);
        int P = Integer.parseInt(flds[1]);
        System.out.println("tokens = " + ml.intArrayToString(tokens) + ", P = " + Integer.toString(P));

        long start = System.currentTimeMillis();

        int result = bagOfTokensScore(tokens, P);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
