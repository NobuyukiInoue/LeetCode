import java.util.*;

class RecentCounter {
    Queue<Integer> q;

    public RecentCounter() {
        q = new LinkedList<>();
    }

    public int ping(int t) {
        q.offer(t);
        while (q.peek() < t - 3000) { q.poll(); }
        return q.size();        
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */

class Cmds {
    public String cmd;
    public String arg;

    public Cmds(String val1, String val2) {
        cmd = val1;
        arg = val2;
    }
}

public class Solution {
    public String output_int_array(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.trim().split("\\],\\[\\[");
        String[] flds1 = flds[0].replace("\"", "").replace("[", "").replace("]", "").split(",");
        String[] flds2 = flds[1].replace("\"", "").replace("[", "").replace("]", "").split(",");

        if (flds1.length != flds2.length) {
            System.out.println("cmds count is not equal args count.");
            System.exit(1);
        }

        Cmds[] exec_list = new Cmds[flds1.length];

        for (int i = 0; i < flds1.length; i++) {
            System.out.println("cmd[" + Integer.toString(i) +  "] = " + flds1[i] + "(" + flds2[i] + ")");
            exec_list[i] = new Cmds(flds1[i], flds2[i]);
        }

        System.out.println();

        long start = System.currentTimeMillis();
        RecentCounter rc = new RecentCounter();
        int[] result = new int[exec_list.length];

        for (int i = 0; i < exec_list.length; i++) {
            if (exec_list[i].cmd.equals("RecentCounter")) {
                //rc = new RecentCounter();
                result[i] = -1;
                System.out.println("Execute ... " + exec_list[i].cmd + "()");
            } else if (exec_list[i].cmd.equals("ping")) {
                result[i] = rc.ping(Integer.parseInt(exec_list[i].arg));
                System.out.println("Execute ... " + exec_list[i].cmd + "(" + exec_list[i].arg + ")");
            } else {
                System.out.println(exec_list[i].cmd + " is not found.");
                System.exit(1);
            }
        }

        long end = System.currentTimeMillis();

        System.out.println("result = [" + output_int_array(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
