import java.util.*;

public class Solution {

    private void Trie_Main(String[] ope, String[] params) {
        if (ope.length != params.length)
            return;
        if (ope.length <= 0 || params.length <= 0)
            return;

        Trie trie = new Trie();

        for (int i = 0; i < ope.length; i++) {
            if (ope[i].equals("Trie")) {
                System.out.println("trie = new Trie()");

            } else if (ope[i].equals("insert")) {
                trie.insert(params[i]);
                System.out.println("trie.insert(" +  params[i] + ")");

            } else if (ope[i].equals("search")) {
                boolean res = trie.search(params[i]);
                System.out.println("trie.search(" +  params[i] + ") ... " + Boolean.toString(res));

            } else if (ope[i].equals("startsWith")) {
                boolean res = trie.startsWith(params[i]);
                System.out.println("trie.startsWith(" +  params[i] + ") ... " + Boolean.toString(res));

            }
        }
    }

    public void Main(String arg) {
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[");
        String[] ope = flds[0].replace("[", "").replace("]", "").split(",");
        String[] params = flds[1].replace("]]]", "").split("\\],\\[");

    	Mylib ml = new Mylib();
        System.out.println("ope[] = " + ml.stringArrayToString(ope));
        System.out.println("params[] = " + ml.stringArrayToString(params));

        long start = System.currentTimeMillis();

        Trie_Main(ope, params);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
