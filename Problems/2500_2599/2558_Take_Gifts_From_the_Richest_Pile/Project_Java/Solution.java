import java.util.*;

public class Solution {
    public long pickGifts(int[] gifts, int k) {
        // 6ms
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int gift : gifts) {
            pq.add(gift);
        }
        for (int i = 0; i < k; i++) {
            pq.add((int)Math.sqrt(pq.poll()));
        }
        long ans = 0;
        for (int i = 0; i < gifts.length; i++) {
            ans += pq.poll();
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] gifts = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("gifts = " + ml.intArrayToString(gifts) + ", k = " + k);
 
        long start = System.currentTimeMillis();

        long result = pickGifts(gifts, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
