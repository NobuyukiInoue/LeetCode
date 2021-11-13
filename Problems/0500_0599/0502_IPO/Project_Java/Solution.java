import java.util.*;

public class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        // 87ms
        PriorityQueue<int[]> pqCap = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        PriorityQueue<int[]> pqPro = new PriorityQueue<>((a, b) -> (b[1] - a[1]));
        
        for (int i = 0; i < profits.length; i++) {
            pqCap.add(new int[] {capital[i], profits[i]});
        }
        
        for (int i = 0; i < k; i++) {
            while (!pqCap.isEmpty() && pqCap.peek()[0] <= w) {
                pqPro.add(pqCap.poll());
            }
            if (pqPro.isEmpty()) {
                break;
            }
            w += pqPro.poll()[1];
        }

        return w;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int k = Integer.parseInt(flds[0]);
        int w = Integer.parseInt(flds[1]);
        int[] profits = ml.stringToIntArray(flds[2]);
        int[] capital = ml.stringToIntArray(flds[3]);
        System.out.println("k = " + Integer.toString(k) 
                       + ", w = " + Integer.toString(w)
                       + ", profits = " + ml.intArrayToString(profits)
                       + ", capital = " + ml.intArrayToString(capital));

        long start = System.currentTimeMillis();

        int result = findMaximizedCapital(k, w, profits, capital);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
