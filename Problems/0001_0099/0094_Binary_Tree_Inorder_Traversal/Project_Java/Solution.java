import java.util.*;

public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // 0ms
        List<Integer> resultList = new ArrayList<Integer>();
        helper(root, resultList);
        return resultList;
    }

    private void helper(TreeNode node, List<Integer> resultList) {
        if (node == null)
            return;
        helper(node.left, resultList);
        resultList.add(node.val);
        helper(node.right, resultList);
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

        List<Integer> result = inorderTraversal(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
