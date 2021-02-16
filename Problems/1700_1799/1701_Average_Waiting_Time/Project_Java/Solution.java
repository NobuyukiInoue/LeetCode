import java.util.*;

public class Solution {
    public double averageWaitingTime(int[][] customers) {
        // 4ms
        double wait = 0.0, cur = 0.0;
        for (int i = 0; i < customers.length; i++) {
            cur = Math.max(cur, customers[i][0]) + customers[i][1];
            wait += cur - customers[i][0];
        }
        return wait / customers.length;
    }

    public double averageWaitingTime2(int[][] customers) {
        // 4ms
        int N = customers.length;
        int prevEnd = customers[0][0];
        long sum = 0;
        for (int[] customer : customers) {
            if (prevEnd <= customer[0]) {
                sum += customer[1];
                prevEnd = customer[0] + customer[1];
            } else {
                sum += (prevEnd - customer[0] + customer[1]);
                prevEnd += customer[1];
            }
        }
        return (double) sum / N;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] customers   = ml.stringToIntIntArray(flds);
        System.out.println("customers = " + ml.intIntArrayToString(customers));

        long start = System.currentTimeMillis();

        double result = averageWaitingTime(customers);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
