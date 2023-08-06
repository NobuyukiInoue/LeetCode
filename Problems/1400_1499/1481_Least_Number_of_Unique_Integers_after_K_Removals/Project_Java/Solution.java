import java.util.*;

public class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        // 37ms - 40ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        for (int num : arr) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
        }

        int[] sorted_cnts = new int[cnts.size()];
        int i = 0;
        for (int val : cnts.values()) {
            sorted_cnts[i++] = val;
        }
        Arrays.sort(sorted_cnts);

        int removed_cnts = 0;
        for (int v : sorted_cnts) {
            if (k - v < 0) {
                break;
            }
            k -= v;
            removed_cnts++;
        }

        return sorted_cnts.length - removed_cnts;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        int result = findLeastNumOfUniqueInts(arr, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
