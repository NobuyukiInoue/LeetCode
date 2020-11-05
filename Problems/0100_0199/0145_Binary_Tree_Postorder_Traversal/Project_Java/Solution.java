import java.util.*;

public class Solution {
    List<Integer> res;

    public List<Integer> postorderTraversal(TreeNode root) {
        // 0ms
        res = new ArrayList<>();
        helper(root);
        return res;
    }

    private void helper(TreeNode node) {
        if (node == null)
            return;
        res.add(0, node.val);
        if (node.right != null)
            helper(node.right);
        if (node.left != null)
            helper(node.left);
        return;
    }

    public List<Integer> postorderTraversal2(TreeNode root) {
        // 0ms
        List<Integer> res = new ArrayList<>();

        if (root == null)
            return res;

        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);

        while (stack.size() > 0) {
            TreeNode node = stack.pop();
            res.add(0, node.val);
            if (node.left != null)
                stack.add(node.left);
            if (node.right != null)
                stack.add(node.right);
        }
    
        return res;
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

        List<Integer> result = postorderTraversal(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
