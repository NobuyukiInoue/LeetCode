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

    public String listArrayToString(List<Boolean> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr;

        if (list.get(0) == null) {
            resultStr = "[null";
        } else {
            resultStr = "[" + Boolean.toString(list.get(0));
        }

        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Boolean.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] args = flds[1].replace("]]]", "").split("\\],\\[");

        System.out.println("cmds[] = " + StringArray2String(cmds));
        System.out.println("args[] = " + StringArray2String(args));

        long start = System.currentTimeMillis();

        ArrayList<Boolean> result = ExecParkingSystem(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
