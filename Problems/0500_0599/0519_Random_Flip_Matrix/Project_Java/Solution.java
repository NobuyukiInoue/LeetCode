import java.util.*;

public class Solution {
    public List<int[]> ExecrandomFlipMatrix(String[] cmds, int[][] args) {
        RandomFlipMatrix randomFlipMatrix = new RandomFlipMatrix(args[0][0], args[0][1]);
        List<int[]> res = new ArrayList<>();
        Boolean created_randomFlipMatrix = false;
        Mylib ml = new Mylib();
        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("Solution")) {
                created_randomFlipMatrix = true;
                res.add(null);
            } else if (created_randomFlipMatrix == false) {
                System.out.println("randomFlipMatrix is not created.");
                System.exit(1);
            } else if (cmds[i].equals("flip")) {
                res.add(randomFlipMatrix.flip());
                System.out.println("flip() ... " + ml.intArrayToString(res.get(res.size() - 1)));
            } else if (cmds[i].equals("reset")) {
                randomFlipMatrix.reset();
                res.add(null);
                System.out.println("reset() ... " + ml.intArrayToString(res.get(res.size() - 1)));
            }
        }
        return res;
    }

    public String listIntArrayToString(List<int[]> flds) {
        if (flds == null)
            return "";
        if (flds.size() <= 0)
            return "[]";

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[" +  ml.intArrayToString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++) {
            sb.append(", [" + ml.intArrayToString(flds.get(i)) + "]");
        }

        return sb.append("]").toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");

        Mylib ml = new Mylib();
        String[] args_str = flds[1].replace("]]]", "").split("\\],\\[");
        int[][] args = new int[args_str.length][];
        for (int i = 0; i < args.length; i++)
            args[i] = ml.stringToIntArray(args_str[i].replace("[", "").replace("]", ""));

        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.intIntArrayToString(args));

        long start = System.currentTimeMillis();

        List<int[]> result = ExecrandomFlipMatrix(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
