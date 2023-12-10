import java.util.*;

public class Solution {
    public List<int[]> sol_main(String[] cmds, int[][] args) {
        Solution2 sol = new Solution2(args[0]);
        List<int[]> res = new ArrayList<>();
        Boolean created_sol = false;
        Mylib ml = new Mylib();
        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("Solution")) {
                created_sol = true;
                res.add(args[i]);
                System.out.println("Solution() ... " + ml.intArrayToString(res.get(res.size() - 1)));
            } else if (created_sol == false) {
                System.out.println("sol is not created.");
                System.exit(1);
            } else if (cmds[i].equals("reset")) {
                res.add(sol.reset());
                System.out.println("reset()    ... " + ml.intArrayToString(res.get(res.size() - 1)));
            } else if (cmds[i].equals("shuffle")) {
                res.add(sol.reset());
                System.out.println("shuffle()  ... " +  ml.intArrayToString(res.get(res.size() - 1)));
            } else {
                System.out.println("error. " + cmds[i] + " is not defined.");
                System.exit(1);
            }
        }
        return res;
    }


    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[", "").split(",");
        String[] args_str = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] args = new int[cmds.length][];
        for (int i = 0; i < args_str.length; i++) {
            if (!args_str[i].equals("")) {
                args[i] = ml.stringToIntArray(args_str[i].replace("[", "").replace("]", ""));
            } else {
                args[i] = null;
            }
        }

        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.intIntArrayToString(args));

        long start = System.currentTimeMillis();

        List<int[]> result = sol_main(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }

    public String listIntArrayToString(List<int[]> list) {
        if (list == null)
            return "";
        if (list.size() <= 0)
            return "[]";

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[" + ml.intArrayToString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + ml.intArrayToString(list.get(i)));
        }
        sb.append("]");

        return sb.toString();
    }
}
