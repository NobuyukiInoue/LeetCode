import java.util.*;

public class Solution {
    int ans;
    public int goodNodes(TreeNode root) {
        ans = 0;
        dfs(root, root.val);
        return ans;
    }

    private void dfs(TreeNode node, int curMax) {
        // 2ms
        if (node == null)
            return;
        if (node.val >= curMax) {
            ans++;
            curMax = node.val;
        }
        dfs(node.left, curMax);
        dfs(node.right, curMax);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        int result = goodNodes(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
