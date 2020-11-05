import java.util.*;
import java.time.LocalDate;
import java.time.temporal.*;

public class Solution {
    public int daysBetweenDates(String date1, String date2) {
        // 2ms
        String[] d1= date1.split("-"); String[] d2= date2.split("-");
        LocalDate from = LocalDate.of(Integer.parseInt(d1[0]), Integer.parseInt(d1[1]), Integer.parseInt(d1[2]));
        LocalDate to = LocalDate.of(Integer.parseInt(d2[0]), Integer.parseInt(d2[1]), Integer.parseInt(d2[2]));
        return Math.abs((int)ChronoUnit.DAYS.between(from, to));
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String date1 = flds[0];
        String date2 = flds[1];
        System.out.println("date1 = " + date1 + ", date2 = " + date2);

        long start = System.currentTimeMillis();

        int result = daysBetweenDates(date1, date2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
