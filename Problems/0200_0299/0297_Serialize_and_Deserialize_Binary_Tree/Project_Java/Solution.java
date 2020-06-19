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
        TreeNode root = ope_t.createTreeNode(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        Codec codec = new Codec();
        root = codec.deserialize(flds);
        String result = codec.serialize(root);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + result + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
