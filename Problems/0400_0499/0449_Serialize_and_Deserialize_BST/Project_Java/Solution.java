import java.util.*;

public class Solution {
    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr.append("," + Integer.toString(list.get(i)));
        }

        return resultStr.append("]").toString();
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        Codec2 cd = new Codec2();
        TreeNode root;

        if (flds.length() > 0) {
          //root = ope_t.createTreeNode(flds);
            root = cd.deserialize(flds);
        } else {
            root = null;
        }

        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        String tree = cd.serialize(root);
        TreeNode result = cd.deserialize(tree);

        long end = System.currentTimeMillis();

        System.out.println("String result = " + tree);
        System.out.print("TreeNode result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("TreeNode result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
