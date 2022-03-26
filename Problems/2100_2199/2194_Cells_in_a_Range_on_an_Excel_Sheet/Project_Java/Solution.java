import java.util.*;

public class Solution {
    public List<String> cellsInRange(String s) {
        // 9ms
        char col1 = s.charAt(0), col2 = s.charAt(3);
        char row1 = s.charAt(1), row2 = s.charAt(4);
        List<String> ans = new ArrayList<>();
        for (char col = col1; col <= col2; col++) {
            for (char row = row1; row <= row2; row++) {
                ans.add("" + col + row);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        List<String> result = cellsInRange(s);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
