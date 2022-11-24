import java.util.*;

public class Solution {
    public List<String> execExamRoom(String[] cmds, String[] args) {
        Boolean createdExamRoom = false;
        ExamRoom examRoom = new ExamRoom(Integer.parseInt(args[0]));
        List<String> res = new ArrayList<>();

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("ExamRoom")) {
                createdExamRoom = true;
                res.add("0");
            } else {
                if (createdExamRoom != true) {
                    System.out.println("ExamRoom() is not executed.");
                    System.exit(1);

                } else if (cmds[i].equals("seat")) {
                    int result = examRoom.seat();
                    System.out.println("seat()  ... " + Integer.toString(result));
                    res.add(Integer.toString(result));

                } else if (cmds[i].equals("leave")) {
                    examRoom.leave(Integer.parseInt(args[i]));
                    System.out.println("leave() ... null");
                    res.add("null");
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] args = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();

        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        List<String> result = execExamRoom(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
