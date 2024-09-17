import java.util.*;

public class Solution {
    public String convertDateToBinary(String date) {
        // 4ms
        String[] flds = date.split("-");
        String[] ans = new String[flds.length];
        for (int i = 0; i < flds.length; i++) {
            ans[i] = Integer.toBinaryString((Integer.parseInt(flds[i])));
        }
        return String.join("-", ans);
    }

    public void Main(String temp) {
        String date = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + date + "\"");

        long start = System.currentTimeMillis();

        String result = convertDateToBinary(date);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
