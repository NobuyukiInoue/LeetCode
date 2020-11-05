import java.util.*;

public class Solution {
    public ArrayList<Boolean> ExecParkingSystem(String[] cmds, String[] args) {
        String flds[] = args[0].split(",");
        ParkingSystem parkingsystem = new ParkingSystem(Integer.parseInt(flds[0]), Integer.parseInt(flds[1]), Integer.parseInt(flds[2]));
        ArrayList<Boolean> res = new ArrayList<Boolean>();
        Boolean created_parkingsystem = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("ParkingSystem")) {
                created_parkingsystem = true;
                res.add(null);
            } else if (created_parkingsystem == false) {
                System.out.println("ParkingSystem is not created.");
                System.exit(1);
            } else if (cmds[i].equals("addCar")) {
                res.add(parkingsystem.addCar(Integer.parseInt(args[i])));
                System.out.println("addCar(" + Integer.parseInt(args[i]) + ") ... " + Boolean.toString(res.get(res.size() - 1)));
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

        ArrayList<Boolean> result = ExecParkingSystem(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listBooleanArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
