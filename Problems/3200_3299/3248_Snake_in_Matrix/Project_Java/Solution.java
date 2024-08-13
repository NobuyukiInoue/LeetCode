import java.util.*;

public class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        // 2ms
        int x = 0, y = 0;
        for (String cmd : commands) {
            switch (cmd) {
            case "LEFT":
                y--;
                break;
            case "RIGHT":
                y++;
                break;
            case "UP":
                x--;
                break;
            default:
                x++;
                break;
            }
        }
        return x*n + y;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);
        List<String> commands = ml.stringArrayToListStringArray(flds[1].replace("\"", "").split(","));
        System.out.println("n = " + n + ", commands = " + ml.listStringArrayToString(commands));

        long start = System.currentTimeMillis();

        int result = finalPositionOfSnake(n, commands);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
