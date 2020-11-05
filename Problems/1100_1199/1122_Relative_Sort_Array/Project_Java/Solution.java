import java.util.*;

public class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int k = 0;
        int[] cnt = new int[1001], ans = new int[arr1.length];
        for (int i : arr1)
            ++cnt[i];
        for (int i : arr2)
            while (cnt[i]-- > 0)
                ans[k++] = i;
        for (int i = 0; i < 1001; ++i)
            while (cnt[i]-- > 0)
                ans[k++] = i;
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr1 = ml.stringToIntArray(flds[0]);
        int[] arr2 = ml.stringToIntArray(flds[1]);

        System.out.println("arr1 = " + ml.intArrayToString(arr1) + ", arr2 = " + ml.intArrayToString(arr2));

        long start = System.currentTimeMillis();

        int[] result = relativeSortArray(arr1, arr2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
