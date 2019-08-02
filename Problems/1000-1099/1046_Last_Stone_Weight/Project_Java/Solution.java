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

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        int[] stones = new int[flds.length];
        for (int i = 0; i < flds.length; i++) {
            stones[i] = Integer.parseInt(flds[i]);
        }
        System.out.println("stones = " + Int_array_to_String(stones));

        long start = System.currentTimeMillis();
        
        int result = lastStoneWeight(stones);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
