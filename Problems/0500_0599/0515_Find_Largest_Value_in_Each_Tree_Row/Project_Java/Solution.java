import java.util.*;

public class Solution {
    // 0ms
    List<Integer> res;

    public List<Integer> largestValues(TreeNode root) {
        res = new ArrayList<>();
        dfs(root, 0);
        return res;
    }

    private void dfs(TreeNode node, int level) {
        if (node == null) {
            return;
        }
        if (level > res.size() - 1) {
            res.add(node.val);
        } else if (node.val > res.get(level)) {
            res.set(level, node.val);
        }

        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root;
        if (flds.length() == 0) {
            root = null;
        } else {
            root = ope_t.createTreeNode(flds);
        }
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        List<Integer> result = largestValues(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
