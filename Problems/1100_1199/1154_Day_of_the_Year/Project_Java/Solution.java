import java.util.*;

public class Solution {
    public int dayOfYear(String date) {
        int[] days = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 };
        String[] flds = date.split("-");
        int year = Integer.parseInt(flds[0]);
        int month = Integer.parseInt(flds[1]);
        int day = Integer.parseInt(flds[2]);
        if (month <= 2) {
            return days[month - 1] + day;
        } else {
            if ( !(year % 100 == 0 && year % 400 != 0) && year % 4 == 0) {
                return days[month - 1] + day + 1;
            } else {
                return days[month - 1] + day;
            }
        }
    }

    public void Main(String temp) {
        String date = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("date = " + date);

        long start = System.currentTimeMillis();

        int result = dayOfYear(date);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
