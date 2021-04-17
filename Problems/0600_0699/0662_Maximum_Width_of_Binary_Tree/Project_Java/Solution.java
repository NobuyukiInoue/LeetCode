import java.util.*;

public class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        // 1ms
        List<Integer> lefts = new ArrayList<Integer>();
        return dfs(root, 1, 0, lefts);
    }

    private int dfs(TreeNode n, int id, int d, List<Integer> lefts) {
        if (n == null)
            return 0;
        if (d >= lefts.size())
            lefts.add(id);
        return Math.max(id + 1 - lefts.get(d), Math.max(dfs(n.left, id*2, d + 1, lefts), dfs(n.right, id*2 + 1, d + 1, lefts)));
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

        int result = widthOfBinaryTree(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
