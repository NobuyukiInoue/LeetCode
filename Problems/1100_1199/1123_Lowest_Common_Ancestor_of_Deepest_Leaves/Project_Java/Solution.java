import java.util.*;
public class Solution {
    // 0ms

    private class Result {
        public int depth;
        public TreeNode node;
        public Result(int depth, TreeNode node) {
            this.depth = depth;
            this.node = node;
        }
    }

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        Result res = get_deepest_node(root, 0);
        return res.node;
    }

    private Result get_deepest_node(TreeNode node, int depth) {
        if (node == null)
            return new Result(0, null);
        Result left = get_deepest_node(node.left, depth + 1);
        Result right = get_deepest_node(node.right, depth + 1);
        if (left.depth > right.depth)
            return new Result(left.depth + 1, left.node);
        if (left.depth < right.depth)
            return new Result(right.depth + 1, right.node);
        return new Result(left.depth + 1, node);
    }

/*
    // 0ms
	public TreeNode lcaDeepestLeaves(TreeNode root) {
		if (root == null) {
			return null;
		}

		int left = height(root.left);
		int right = height(root.right);
		if (left == right){
			return root;
		} else if (left > right){
			return lcaDeepestLeaves(root.left);
		} else {
			return lcaDeepestLeaves(root.right);
		}
	}

	private int height(TreeNode root){
		if (root == null) {
			return 0;
		}
		return 1 + Math.max(height(root.left), height(root.right));
	}
*/

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

        TreeNode result = lcaDeepestLeaves(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
