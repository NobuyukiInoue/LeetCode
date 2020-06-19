import java.util.*;

public class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        Stack<TreeNode> s1 = new Stack<>(), s2 = new Stack<>();
        s1.push(root1); s2.push(root2);
        while (!s1.empty() && !s2.empty())
            if (dfs(s1) != dfs(s2))
                return false;
        return s1.empty() && s2.empty();
    }

    public int dfs(Stack<TreeNode> s) {
        while (true) {
            TreeNode node = s.pop();
            if (node.right != null)
                s.push(node.right);
            if (node.left != null)
                s.push(node.left);
            if (node.left == null && node.right == null)
                return node.val;
        }
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root1 = ope_t.createTreeNode(flds[0]);
        TreeNode root2 = ope_t.createTreeNode(flds[1]);
    //  Codec codec = new Codec();
    //  TreeNode root1 = codec.deserialize(flds[0]);
    //  TreeNode root2 = codec.deserialize(flds[1]);
        System.out.print("root1 = \n" + ope_t.treeToStaircaseString(root1));
        System.out.print("root2 = \n" + ope_t.treeToStaircaseString(root2));
        System.out.println("root1 = " + ope_t.tree2str(root1));
        System.out.println("root2 = " + ope_t.tree2str(root2));

        long start = System.currentTimeMillis();

        boolean result = leafSimilar(root1, root2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
