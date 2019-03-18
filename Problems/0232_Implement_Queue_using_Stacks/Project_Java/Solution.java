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

    public String StringArray2String(String[] data) {
        if (data.length <= 0)
            return "";

        String resultStr;
        if (data[0].length() == 0) {
            resultStr = "null";
        } else {
            resultStr = data[0];
        }

        for (int i = 1; i < data.length; i++) {
            if (data[i].length() == 0) {
                resultStr += ", null";
            } else {
                resultStr += ", " + data[i];
            }

        }

        return resultStr;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\]");
        String[] cmds = flds[0].split(",");
        String[] args = flds[1].replace("[", "").replace("]", "").split(",");

        System.out.println("cmds[] = " + StringArray2String(cmds));
        System.out.println("args[] = " + StringArray2String(args));

        long start = System.currentTimeMillis();
        
        calc(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
