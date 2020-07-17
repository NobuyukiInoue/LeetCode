import java.util.*;

public class Solution {
    public String reformatDate(String date) {
        // 15ms
        String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        String[] dates = date.split(" ");
        String d = dates[0].replace("th", "").replace("rd", "").replace("nd", "").replace("st", "");
        int m = 0;
        for (int i = 0; i < months.length; i++) {
            if (dates[1].equals(months[i])) {
                m = i + 1;
            }
        }
        return String.format("%s-%s-%s", dates[2], m < 10 ? ("0" + m) : m + "", Integer.parseInt(d) < 10 ? ("0" + d) : d);
    }

    public void Main(String temp) {
        String date = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("path = " + date);

        long start = System.currentTimeMillis();

        String result = reformatDate(date);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
