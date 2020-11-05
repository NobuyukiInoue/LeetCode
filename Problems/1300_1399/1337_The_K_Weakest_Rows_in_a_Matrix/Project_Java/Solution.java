import java.util.*;

public class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        // 1ms
        int le = mat.length;
        int[][] soldierList = new int[le][2];
        
        for (int i = 0; i < le; i++) {
            soldierList[i][1] = countSoldier(mat[i]);
            soldierList[i][0] = i;
        }

        Arrays.sort(soldierList, (a, b) -> a[1] - b[1]);
        int[] res = new int[k];
        for(int i = 0; i < k; i++) {
            res[i] = soldierList[i][0];
        }
        return res;
    }

    public int countSoldier(int[] arr) {
        int res = 0;
        for(int i: arr)
            if (i == 1)
                res++;
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        String[] str_mat = flds[0].split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(str_mat);
        System.out.println("mat = " + ml.matrixToString(mat));

        int k = Integer.parseInt(flds[1].replace("]]", ""));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int[] result = kWeakestRows(mat, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
