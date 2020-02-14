import java.util.*;

public class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        // 3ms
        int[] res = new int[n];
        for (int[] flds : bookings) {
            res[flds[0] - 1] += flds[2];
            if (flds[1] < n) {
                res[flds[1]] -= flds[2];
            }
        }
        for (int i = 1; i < n; i++) {
            res[i] += res[i - 1];
        }
        return res;
    }

    public int[] corpFlightBookings2(int[][] bookings, int n) {
        // 844ms
        int[] counts = new int[n];

        for (int[] cur : bookings) {
            int flights_start = cur[0];
            int flights_end = cur[1];
            int seats_count = cur[2];
            for (int i = flights_start; i <= flights_end; i++) {
                counts[i - 1] += seats_count;
            }
        }
        
        return counts;
    }

    public int[] corpFlightBookings3(int[][] bookings, int n) {
        // 1325ms
        int[] counts = new int[n];

        for (int[] flds : bookings) {
            for (int i = flds[0]; i <= flds[1]; i++) {
                counts[i - 1] += flds[2];
            }
        }
        
        return counts;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[[", "").trim().split("\\]],\\[");

        Mylib ml = new Mylib();

        String[] bookings_str = flds[0].split("\\],\\[");
        int[][] bookings = new int[bookings_str.length][];
    
        for (int i = 0; i < bookings_str.length; i++) {
            bookings[i] = ml.stringTointArray(bookings_str[i]);
        }

        int n = Integer.parseInt(flds[1].replace("]]", ""));

        System.out.print("bookings = [");
        for (int i = 0; i < bookings.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(bookings[i]));
            else
                System.out.print("," + ml.intArrayToString(bookings[i]));
        }
        System.out.println("]");
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        int[] result = corpFlightBookings(bookings, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
