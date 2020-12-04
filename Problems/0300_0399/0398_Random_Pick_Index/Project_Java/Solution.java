import java.util.*;

public class Solution {
    public List<String> ExecRandomPickIndex(String[] cmds, int[][] args) {
        RandomPickIndex randomPickIndex = new RandomPickIndex(args[0]);
        List<String> res = new ArrayList<>();
        Boolean created_randomPickIndex = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("Solution")) {
                created_randomPickIndex = true;
                res.add(null);
            } else if (created_randomPickIndex == false) {
                System.out.println("RandomPickIndex is not created.");
                System.exit(1);
            } else if (cmds[i].equals("pick")) {
                res.add(Integer.toString(randomPickIndex.pick(args[i][0])));
                System.out.println("insert(" + Integer.toString(args[i][0]) + ") ... " + res.get(res.size() - 1));
            }
        }
        return res;
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

        List<String> result = ExecRandomPickIndex(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
