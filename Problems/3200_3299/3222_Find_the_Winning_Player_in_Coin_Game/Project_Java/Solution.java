import java.util.*;

public class Solution {
    public String losingPlayer(int x, int y) {
        // 0ms
        int cnt = 0;
        while (x > 0 && y > 3) {
            x -= 1;
            y -= 4;
            cnt++;
        }
        return (cnt%2 == 1)? "Alice" : "Bob";
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int x = Integer.parseInt(flds[0]);
        int y = Integer.parseInt(flds[1]);
        System.out.println("x = " + x + ", y = " + y);

        long start = System.currentTimeMillis();

        String result = losingPlayer(x, y);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
