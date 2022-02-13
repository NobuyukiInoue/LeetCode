import java.util.*;

public class Solution {
    public int eatenApples(int[] apples, int[] days) {
        // 31ms
        int lastday = apples.length;
        int day = 0, res = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        while (day < lastday) {
            if (apples[day] > 0) {
                pq.add(new int[] {day + days[day], apples[day]});
            }
            if (!pq.isEmpty() && pq.peek()[0] > day) {
                res++;
                pq.peek()[1]--;
                if (pq.peek()[1] == 0) {
                    pq.poll();
                }
            }
            day++;
            while (!pq.isEmpty() && pq.peek()[0] <= day) {
                pq.poll();
            }
        }
        while (!pq.isEmpty()) {
            int[] temp = pq.poll();
            int expire = temp[0], counts = temp[1];
            if (day < expire) {
                int jump_to = Math.min(expire, day + counts);
                res += jump_to - day;
                day = jump_to;
            }
        }
        return res;
    }

    public int eatenApples2(int[] apples, int[] days) {
        // 76ms
        int i = 0, res = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        while (i < apples.length || !pq.isEmpty()) {
            if (i < apples.length && apples[i] > 0) {
                pq.add(new int[]{i + days[i], apples[i]});
            }
            while (!pq.isEmpty() && (pq.peek()[0] <= i || pq.peek()[1] == 0)) {
                pq.poll();
            }
            if (!pq.isEmpty()) {
                res++;
                pq.peek()[1]--;
            }
            i++;
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] apples = ml.stringToIntArray(flds[0]);
        int[] days = ml.stringToIntArray(flds[1]);
        System.out.println("apples = " + ml.intArrayToString(apples) + ", days = " + ml.intArrayToString(days));

        long start = System.currentTimeMillis();

        int result = eatenApples(apples, days);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
