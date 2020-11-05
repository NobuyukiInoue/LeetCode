import java.util.*;

public class Solution {
    /*
    static public void calc() {
        long start = System.currentTimeMillis();

        MyStack obj = new MyStack();

        obj.push(1);
        System.out.println("push(1)");

        obj.push(2);
        System.out.println("push(2)");

        int param_2 = obj.pop();
        System.out.println("pop() ... " + Integer.toString(param_2));

        int param_3 = obj.top();
        System.out.println("top() ... " + Integer.toString(param_3));

        boolean param_4 = obj.empty();
        System.out.println("empty() ... " + Boolean.toString(param_4));

        long end = System.currentTimeMillis();
        System.out.println((end - start)  + "ms\n");
    }
    */

    public void calc(String[] cmds, String[] args) {
        Boolean createdMyStack = false;
        MyStack ms = new MyStack();

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("MyStack")) {
                createdMyStack = true;
            } else {
                if (createdMyStack != true) {
                    System.out.println("MyStack() is not executed.");
                    System.exit(1);
                } else if (cmds[i].equals("push")) {
                    ms.push(Integer.parseInt(args[i]));
                    System.out.println("Execute push(" + Integer.parseInt(args[i]) + ")");
                } else if (cmds[i].equals("pop")) {
                    Integer result = ms.pop();
                    System.out.println("pop() ... " + Integer.toString(result));
                } else if (cmds[i].equals("top")) {
                    Integer result = ms.top();
                    System.out.println("top() ... " + Integer.toString(result));
                } else if (cmds[i].equals("empty")) {
                    Boolean result = ms.empty();
                    System.out.println("empty() ... " + Boolean.toString(result));
                }
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] vals = flds[1].replace("[", "").replace("]", "").split(",");

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("vals[] = " + ml.stringArrayToString(vals));

        long start = System.currentTimeMillis();

        calc(cmds, vals);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
