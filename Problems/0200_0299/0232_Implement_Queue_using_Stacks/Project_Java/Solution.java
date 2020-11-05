import java.util.*;

public class Solution {
    public void calc(String[] cmds, String[] args) {
        Boolean createdMyQueue = false;
        MyQueue ms = new MyQueue();

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("MyQueue")) {
                createdMyQueue = true;
            } else {
                if (createdMyQueue != true) {
                    System.out.println("MyQueue() is not executed.");
                    System.exit(1);
                } else if (cmds[i].equals("push")) {
                    ms.push(Integer.parseInt(args[i]));
                    System.out.println("Execute push(" + Integer.parseInt(args[i]) + ")");
                } else if (cmds[i].equals("pop")) {
                    Integer result = ms.pop();
                    System.out.println("pop() ... " + Integer.toString(result));
                } else if (cmds[i].equals("peek")) {
                    Integer result = ms.peek();
                    System.out.println("peek() ... " + Integer.toString(result));
                } else if (cmds[i].equals("empty")) {
                    Boolean result = ms.empty();
                    System.out.println("empty() ... " + Boolean.toString(result));
                }
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\]");
        String[] cmds = flds[0].split(",");
        String[] args = flds[1].replace("[", "").replace("]", "").split(",");

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        calc(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
