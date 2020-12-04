import java.util.*;

public class Solution {
    public List<List<String>> ExecOrderedStream(String[] cmds, String[] args) {
        OrderedStream orderedStream = new OrderedStream(Integer.parseInt(args[0]));
        List<List<String>> res = new ArrayList<List<String>>();
        Boolean created_orderedStream = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("OrderedStream")) {
                created_orderedStream = true;
                res.add(null);
            } else if (created_orderedStream == false) {
                System.out.println("OrderedStream is not created.");
                System.exit(1);
            } else if (cmds[i].equals("insert")) {
                String[] flds = args[i].split(",");
                res.add(orderedStream.insert(Integer.parseInt(flds[0]), flds[1]));
                System.out.println("insert(" + args[i] + ") ... " + res.get(res.size() - 1));
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

        List<List<String>> result = ExecOrderedStream(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
