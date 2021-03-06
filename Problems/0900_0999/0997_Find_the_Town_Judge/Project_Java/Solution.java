import java.util.*;

public class Solution {
    public int findJudge(int N, int[][] trust) {
        int[] l = new int[N + 1];
        for (int i = 0; i < trust.length; i++) {
            l[trust[i][1]]++;
            l[trust[i][0]]--;
        }
        for (int i = 1; i < N + 1; i++) {
            if (l[i] == N - 1)
                return i;
        }
        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").trim().split("\\],\\[\\[");

        int N = Integer.parseInt(flds[0].replace("[", "").replace("]", ""));
        System.out.println("N = " + Integer.toString(N));

        String[] flds1 = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] trust = ml.stringToIntIntArray(flds1);
        System.out.println("trust = " + ml.intIntArrayToString(trust));

        long start = System.currentTimeMillis();

        int result = findJudge(N, trust);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
