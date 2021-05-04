import java.util.*;

public class Solution {
    public int[] xorListsQueries(int[] arr, int[][] queries) {
        // 1ms
        if (queries.length == 0) {
            return new int[0];
        }

        int n = arr.length;
        int[] xorLists = new int[n];
        xorLists[0] = arr[0];
        for (int i = 1; i < n; i++) {
            xorLists[i] = xorLists[i - 1]^arr[i];
        }

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            if (l == 0) {
                ans[i] = xorLists[r];
            } else {
                ans[i] = xorLists[r]^xorLists[l - 1];
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("]]]", "").trim().split("\\],\\[\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0].replace("[[", ""));

        int[][] queries = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("arr = " + ml.intArrayToString(arr) + ", queries = " + ml.intIntArrayToString(queries));

        long start = System.currentTimeMillis();

        int[] result = xorListsQueries(arr, queries);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
