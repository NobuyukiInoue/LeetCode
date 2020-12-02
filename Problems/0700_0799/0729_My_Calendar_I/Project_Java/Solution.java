import java.util.*;

public class Solution {
    public ArrayList<Boolean> ExecMyCalender(String[] cmds, String[] args) {
        MyCalendar mycalendar = new MyCalendar();
        ArrayList<Boolean> res = new ArrayList<Boolean>();
        Boolean created_mycalendar = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("MyCalendar")) {
                created_mycalendar = true;
                res.add(null);
            } else if (created_mycalendar == false) {
                System.out.println("MyCalendar is not created.");
                System.exit(1);
            } else if (cmds[i].equals("book")) {
                String[] flds = args[i].split(",");
                res.add(mycalendar.book(Integer.parseInt(flds[0]), Integer.parseInt(flds[1])));
                System.out.println("book(" + flds[0] + ", " + flds[1] + ") ... " + Boolean.toString(res.get(res.size() - 1)));
            }
        }
        return res;
    }


    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] args = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        ArrayList<Boolean> result = ExecMyCalender(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listBooleanArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
