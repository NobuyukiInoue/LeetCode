import java.util.*;

public class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        // 0ms
        if (start == destination)
            return 0;

        int r = 0, l = 0;
        int p1, p2;
        if (destination > start) {
            p1 = start;
            p2 = destination;
        } else {
            p1 = destination;
            p2 = start;
        }

        for (int i = p1; i < p2; ++i) {
            r += distance[i];
        }
        for (int i = p2; i < distance.length; ++i) {
            l += distance[i];
        }
        for (int i = 0; i < p1; ++i) {
            l += distance[i];
        }

        if (l < r)
            return l;
        else
            return r;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] distance = ml.stringTointArray(flds[0]);
        String []flds2 = flds[1].split(",");
        int start = Integer.parseInt(flds2[0]);
        int destination = Integer.parseInt(flds2[1]);

        System.out.println("distance = " + ml.intArrayToString(distance) +
                           ", start = " + Integer.toString(start) +
                           ", destination = " + Integer.toString(destination));

        long t_start = System.currentTimeMillis();

        int result = distanceBetweenBusStops(distance, start, destination);

        long t_end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((t_end - t_start)  + "ms\n");
    }
}
