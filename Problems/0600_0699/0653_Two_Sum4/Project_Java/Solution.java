import java.util.HashSet;
import java.util.Iterator;

public class Solution {
    public boolean findTarget(TreeNode root, int k) {
        HashSet<Integer> set = new HashSet<>();

        return dfs(root, set, k);
    }

    public boolean dfs(TreeNode root, HashSet<Integer> set, int k) {
        if (root == null)
            return false;

        if (set.contains(k - root.val))
            return true;

        set.add(root.val);

        return dfs(root.left, set, k) || dfs(root.right, set, k);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        Integer k = Integer.parseInt(flds[1]);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        boolean result = findTarget(root, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
