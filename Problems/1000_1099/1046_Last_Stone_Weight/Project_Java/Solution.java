import java.util.*;

public class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b)-> b - a);
        for (int a : stones)
            pq.offer(a);
        for (int i = 0; i < stones.length - 1; ++i)
            pq.offer(pq.poll() - pq.poll());
        return pq.poll();
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] stones = ml.stringToIntArray(flds);
        System.out.println("stones = " + ml.intArrayToString(stones));

        long start = System.currentTimeMillis();

        int result = lastStoneWeight(stones);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
