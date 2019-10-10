import java.util.*;

public class Solution {
    String[] days = new String[]{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    public String dayOfTheWeek(int day, int month, int year) {
        // 0ms
        if (month < 3) {
            month += 12;
            year -= 1;
        }
        int c = year / 100;
        year = year % 100;
        int w = (c / 4 - 2 * c + year + year / 4 + 13 * (month + 1) / 5 + day - 1) % 7;
        return days[(w + 7) % 7];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int day = Integer.parseInt(flds[0]);
        int month = Integer.parseInt(flds[1]);
        int year = Integer.parseInt(flds[2]);
        System.out.println("day = " + Integer.toString(day) + ", month = " + Integer.toString(month) + ", year = " + Integer.toString(year));

        long start = System.currentTimeMillis();
        
        String result = dayOfTheWeek(day, month, year);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
