import java.util.*;

public class Solution {
    public String interpret(String command) {
        // 0ms
        return command.replace("()", "o").replace("(al)", "al");
    }

    public void Main(String temp) {
        String command = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("command = " + command);

        long start = System.currentTimeMillis();

        String result = interpret(command);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
