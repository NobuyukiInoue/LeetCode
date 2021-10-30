import java.util.*;

public class Solution {
    public int minMovesToSeat(int[] seats, int[] students) {
        // 2ms
        Arrays.sort(seats);
        Arrays.sort(students);
        int ans = 0;
        for (int i = 0; i < seats.length; i++) {
            ans += Math.abs(seats[i] - students[i]);
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] seats = ml.stringToIntArray(flds[0]);
        int[] students = ml.stringToIntArray(flds[1]);
        System.out.println("seats = " + ml.intArrayToString(seats) 
                       + ", students = " + ml.intArrayToString(students));

        long start = System.currentTimeMillis();

        int result = minMovesToSeat(seats, students);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
