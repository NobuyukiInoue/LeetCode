import java.util.*;

public class Solution {
    public ArrayList<String> ExecPeekingIterator(String[] cmds, String[] args) {
        List<Integer> flds = new ArrayList<>();
        for (String fld : args[0].replace("[", "").replace("]", "").split(",")) {
            flds.add(Integer.parseInt(fld));
        }

        PeekingIterator peekingIterator = new PeekingIterator(flds.iterator());
        ArrayList<String> res = new ArrayList<>();
        Boolean created_peekingIterator = false;

        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("PeekingIterator")) {
                created_peekingIterator = true;
                res.add(null);

            } else if (created_peekingIterator == false) {
                System.out.println("PeekingIterator is not created.");
                System.exit(1);

            } else if (cmds[i].equals("peek")) {
                Integer temp = peekingIterator.peek();
                if (temp != null)
                    res.add(Integer.toString(temp));
                else
                    res.add("null");
                System.out.println("peek() ... " + res.get(res.size() - 1));

            } else if (cmds[i].equals("next")) {
                Integer temp = peekingIterator.next();
                if (temp != null)
                    res.add(Integer.toString(temp));
                else
                    res.add("null");
                System.out.println("next() ... " + res.get(res.size() - 1));

            } else if (cmds[i].equals("hasNext")) {
                res.add(Boolean.toString(peekingIterator.hasNext()));
                System.out.println("hasNext() ... " + res.get(res.size() - 1));

            }
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[", "").split(",");
        String[] args = flds[1].replace("]]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.stringArrayToString(args));

        long start = System.currentTimeMillis();

        ArrayList<String> result = ExecPeekingIterator(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
