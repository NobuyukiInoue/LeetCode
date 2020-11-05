import java.util.*;

public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        // 1ms
        List<List<Integer>> results = new ArrayList<>();
        pathSum(root, sum, results, new ArrayList<>());
        return results;
    }

    private void pathSum(TreeNode root, int sum, List<List<Integer>> list, ArrayList<Integer> path) {
        if (root == null)
            return;
        path.add(root.val);
        if (root.left == null && root.right == null && sum == root.val) {
            List<Integer> current = new ArrayList<>(path);
            list.add(current);
        }
        pathSum(root.left, sum - root.val, list, path);
        pathSum(root.right, sum - root.val, list, path);
        path.remove(path.size() - 1);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds[] = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));
        int sum = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        List<List<Integer>> result = pathSum(root, sum);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
