import java.util.*;

public class Solution {
    public ArrayList<String> ExecLRUCache(String[] cmds, String[] args) {
        LRUCache LRUCache = new LRUCache(Integer.parseInt(args[0]));
        ArrayList<String> res = new ArrayList<String>();
        Boolean created_LRUCache = false;
        Mylib ml = new Mylib();

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("LRUCache")) {
                created_LRUCache = true;
                res.add(null);
            } else if (created_LRUCache == false) {
                System.out.println("LRUCache is not created.");
                System.exit(1);
            } else if (cmds[i].equals("put")) {
                int[] flds = ml.stringToIntArray(args[i]);
                LRUCache.put(flds[0], flds[1]);
                System.out.println("put(" + flds[0] + ", " + flds[1] + ")");
                res.add("null");
                System.out.println(res.get(res.size() - 1));
            } else if (cmds[i].equals("get")) {
                res.add(Integer.toString(LRUCache.get(Integer.parseInt(args[i]))));
                System.out.println(res.get(res.size() - 1));
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

        ArrayList<String> result = ExecLRUCache(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
