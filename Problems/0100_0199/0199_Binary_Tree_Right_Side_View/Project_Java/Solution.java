import java.util.*;

public class Solution {
    List<Integer> res;
    public List<Integer> rightSideView(TreeNode root) {
        // 0ms
        res = new ArrayList<>();
        helper(root, 1);
        return res;
    }

    private void helper(TreeNode node, int level) {
        if (node == null)
            return;
        if (res.size() < level)
            res.add(node.val);
        if (node.right != null)
            helper(node.right, level + 1);
        if (node.left != null)
            helper(node.left, level + 1);
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (Integer i = 1; i < list.size(); i++)
            resultStr.append("," + Integer.toString(list.get(i)));

        resultStr.append("]");

        return resultStr.toString();
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
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        List<Integer> result = rightSideView(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
