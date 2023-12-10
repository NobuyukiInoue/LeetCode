import java.util.*;

public class Solution {
    public List<String> randmizedSet(String[] cmds, int[][] args) {
        RandomizedSet randomizedSet = new RandomizedSet();
        List<String> res = new ArrayList<>();
        Boolean created_randmizedSet = false;
        for (int i = 0; i < cmds.length; i++ ) {
            if (cmds[i].equals("RandomizedSet")) {
                created_randmizedSet = true;
                res.add("null");
                System.out.println("RandmizedSet() ... " + res.get(res.size() - 1));
            } else if (created_randmizedSet == false) {
                System.out.println("randmizedSet is not created.");
                System.exit(1);
            } else if (cmds[i].equals("insert")) {
                res.add(Boolean.toString(randomizedSet.insert(args[i][0])));
                System.out.println("insert(" +  Integer.toString(args[i][0]) + ") ... " + res.get(res.size() - 1));
            } else if (cmds[i].equals("remove")) {
                res.add(Boolean.toString(randomizedSet.remove(args[i][0])));
                System.out.println("remove(" +  Integer.toString(args[i][0]) + ") ... " + res.get(res.size() - 1));
            } else if (cmds[i].equals("getRandom")) {
                res.add(Integer.toString(randomizedSet.getRandom()));
                System.out.println("getRandome() ... " + res.get(res.size() - 1));
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
                args[i] = new int[] {Integer.parseInt(args_str[i].replace("[", "").replace("]", ""))};
            } else {
                args[i] = null;
            }
        }

        System.out.println("cmds[] = " + ml.stringArrayToString(cmds));
        System.out.println("args[] = " + ml.intIntArrayToString(args));

        long start = System.currentTimeMillis();

        List<String> result = randmizedSet(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
