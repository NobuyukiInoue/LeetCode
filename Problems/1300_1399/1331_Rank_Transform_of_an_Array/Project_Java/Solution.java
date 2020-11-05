import java.util.*;

public class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // 43ms
        if (arr == null)
            return null;

        int N = arr.length;
        int[] ranks = Arrays.copyOf(arr, N);
        Arrays.sort(ranks);
        int rank = 1;
        HashMap<Integer, Integer> m = new HashMap();
        for (int n : ranks) {
            if (!m.containsKey(n))
                m.put(n, rank++);
        }
        for (int i = 0; i < N; i++) 
            ranks[i] = m.get(arr[i]);
        return ranks;
    }

    public int[] decompressRLElist2(int[] nums) {
        // 3ms
		int len = 0;
        for (int i = 0; i < nums.length; i += 2)
            len += nums[i];
        int[] res = new int[len];
        int p = 0;
        for (int i = 0; i < nums.length; i += 2) {
			for (int j = 0; j < nums[i]; j++) {
                res[p++] = nums[i + 1];
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int[] result = arrayRankTransform(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
