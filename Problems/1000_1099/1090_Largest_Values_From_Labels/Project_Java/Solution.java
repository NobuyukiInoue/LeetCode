import java.util.*;

public class Solution {
    public int largestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        // 16ms - 19ms
        int n = values.length, hash[][] = new int[n][2];
        for (int i = 0; i < n; i++) {
            hash[i] = new int[] {values[i], labels[i]};
        }
        int[] cnt = new int[20001];
        int ans = 0;
        Arrays.sort(hash, (a, b) -> b[0] - a[0]);
        for (int[] h : hash) {
            int value = h[0], label = h[1];
            if (++cnt[label] <= useLimit) {
                ans += value;
                numWanted--;
                if (numWanted == 0) {
                    break;
                }
            }
        }
        return ans;
   }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] values = ml.stringToIntArray(flds[0]);
        int[] labels = ml.stringToIntArray(flds[1]);
        int numWanted = Integer.parseInt(flds[2]);
        int useLimit = Integer.parseInt(flds[3]);
        System.out.println("values = " + ml.intArrayToString(values) + ", labels = " + ml.intArrayToString(labels) + ", numWanted = " + numWanted + ", useLimit = " + useLimit);

        long start = System.currentTimeMillis();

        int result = largestValsFromLabels(values, labels, numWanted, useLimit);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
