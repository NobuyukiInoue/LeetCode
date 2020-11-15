import java.util.*;

public class Solution {
    public int findLongestChain(int[][] pairs) {
        // 3ms
        if (pairs == null)
            return 0;
        int len = pairs.length;
        if (len < 2)
            return len;

        qsort(pairs, 0, len - 1);

        int cur = pairs[0][1];
        int res = 1;

        for (int i = 1; i < len; i++) {
            if (pairs[i][0] > cur) {
                res++;
                cur = pairs[i][1];
            }
        }
        return res;
    }

    private void qsort(int[][] pairs, int begin, int end) {
        if (begin >= end)
            return;
        int key = pairs[begin][1];
        int[] keyPair = pairs[begin];
        int i = begin, j = end;
        while (i < j) {
            while (i < j && key <= pairs[j][1])
                --j;
            pairs[i] = pairs[j];
            while (i < j && key >= pairs[i][1])
                ++i;
            pairs[j] = pairs[i];
        }
        pairs[i] = keyPair;
        qsort(pairs, begin, i - 1);
        qsort(pairs, i + 1, end);
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim();

        String[] str_pairs = flds.replace("[[", "").replace("]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] pairs = ml.stringToIntIntArray(str_pairs);
        System.out.println("pairs = " + ml.intIntArrayToString(pairs));

        long start = System.currentTimeMillis();

        int result = findLongestChain(pairs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
