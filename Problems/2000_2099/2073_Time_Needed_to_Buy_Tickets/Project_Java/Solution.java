import java.util.*;

public class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        // 0ms
        int ans = 0;
        for (int i = 0; i < tickets.length; i++) {
            if (i > k) {
                ans += Math.min(tickets[k] - 1,  tickets[i]);
            } else {
                ans += Math.min(tickets[k],  tickets[i]);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] tickets = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("tickets = " + ml.intArrayToString(tickets) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = timeRequiredToBuy(tickets, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
