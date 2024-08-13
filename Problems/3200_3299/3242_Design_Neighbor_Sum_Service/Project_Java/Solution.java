import java.util.*;

public class Solution {
    public List<String> NeighborSum(String[] cmds, String[] args) {
        Mylib ml = new Mylib();
        int args0[][] = ml.stringToIntIntArray(args[0].split("\\],\\["));
        NeighborSum neighborSum = new NeighborSum(args0);
        List<String> res = new ArrayList<String>();
        Boolean created_NeighborSum = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("NeighborSum")) {
                created_NeighborSum = true;
                res.add(null);
            } else if (created_NeighborSum == false) {
                System.out.println("NeighborSum is not created.");
                System.exit(1);
            } else if (cmds[i].equals("adjacentSum")) {
                res.add(Integer.toString(neighborSum.adjacentSum(Integer.parseInt(args[i]))));
                System.out.println("adjacentSum(" + args[i] + ") ... " + res.get(res.size() - 1));
            } else if (cmds[i].equals("diagonalSum")) {
                res.add(Integer.toString(neighborSum.diagonalSum(Integer.parseInt(args[i]))));
                System.out.println("diagonalSum(" + args[i] + ") ... " + res.get(res.size() - 1));
            } else {
                System.out.println("Error..." + args[i]);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[\\[\\[");
        String[] cmds = flds[0].replace("[", "").replace("]", "").split(",");
        String[] flds1 = flds[1].replace("[[", "").replace("]]]]", "").split("\\]\\]\\],\\[");
        String[] flds11 = flds1[1].split("\\],\\[");
        String[] args = new String[cmds.length];
        args[0] = flds1[0];
        for (int i = 1; i < args.length; i++) {
            args[i] = flds11[i - 1];
        }

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        List<String> result = NeighborSum(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
