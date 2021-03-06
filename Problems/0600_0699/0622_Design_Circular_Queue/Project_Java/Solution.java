import java.util.*;

public class Solution {
    public ArrayList<String> ExecCircularQueue(String[] cmds, String[] args) {
        MyCircularQueue circularQueue = new MyCircularQueue(Integer.parseInt(args[0]));
        ArrayList<String> ans = new ArrayList<String>();
        Boolean created_circularQueue = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("MyCircularQueue")) {
                created_circularQueue = true;
                System.out.println("MyCircularQueue circlularQueue = new MyCircular(" + args[i] + ")");
                ans.add("null");
            } else if (created_circularQueue == false) {
                System.out.println("circularQueue is not created.");
                System.exit(1);
            } else if (cmds[i].equals("enQueue")) {
                boolean res = circularQueue.enQueue(Integer.parseInt(args[i]));
                System.out.println("circularQueue.enQueue(" + Integer.parseInt(args[i]) + ") ... " + Boolean.toString(res));
                ans.add(Boolean.toString(res));
            } else if (cmds[i].equals("deQueue")) {
                boolean res = circularQueue.deQueue();
                System.out.println("circularQueue.deQueue() ... " + Boolean.toString(res));
                ans.add(Boolean.toString(res));
            } else if (cmds[i].equals("Front")) {
                int res = circularQueue.Front();
                System.out.println("circularQueue.Front() ... " + Integer.toString(res));
                ans.add(Integer.toString(res));
            } else if (cmds[i].equals("Rear")) {
                int res = circularQueue.Rear();
                System.out.println("circularQueue.Rear() ... " + Integer.toString(res));
                ans.add(Integer.toString(res));
            } else if (cmds[i].equals("isEmpty")) {
                boolean res = circularQueue.isEmpty();
                System.out.println("circularQueue.isEmpty() ... " + Boolean.toString(res));
                ans.add(Boolean.toString(res));
            } else if (cmds[i].equals("isFull")) {
                boolean res = circularQueue.isFull();
                System.out.println("circularQueue.isFull() ... " + Boolean.toString(res));
                ans.add(Boolean.toString(res));
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] args = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        ArrayList<String> result = ExecCircularQueue(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
