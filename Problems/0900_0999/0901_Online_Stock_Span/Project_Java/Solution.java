import java.util.*;

public class Solution {
    public ArrayList<String> ExecStockSpanner(String[] cmds, String[] args) {
        String flds[] = args[0].split(",");
        StockSpanner stockSpanner = new StockSpanner();
        ArrayList<String> res = new ArrayList<>();
        Boolean created_stockSpanner = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("StockSpanner")) {
                created_stockSpanner = true;
                res.add("null");
            } else if (created_stockSpanner == false) {
                System.out.println("StockSpanner is not created.");
                System.exit(1);
            } else if (cmds[i].equals("next")) {
                int nextRes = stockSpanner.next(Integer.parseInt(args[i]));
                res.add(Integer.toString(nextRes ));
                System.out.println("next(" + Integer.parseInt(args[i]) + ") ... " + res.get(res.size() - 1));
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

        ArrayList<String> result = ExecStockSpanner(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
