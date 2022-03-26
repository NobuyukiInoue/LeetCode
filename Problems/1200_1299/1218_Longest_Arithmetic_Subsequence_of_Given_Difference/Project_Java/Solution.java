import java.util.*;

public class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        // 40ms
        HashMap<Integer, Integer> dp = new HashMap<>();
        int ans = 0;
        for (int x : arr) {
            dp.put(x, dp.getOrDefault(x - difference, 0) + 1);
            ans = Math.max(ans, dp.get(x));
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int dirrerence = Integer.parseInt(flds[1]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", dirrerence = " + Integer.toString(dirrerence));

        long start = System.currentTimeMillis();

        int result = longestSubsequence(arr, dirrerence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
