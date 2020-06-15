import java.util.*;

public class Solution {
    List<Integer> res;

    public List<Integer> preorderTraversal(TreeNode root) {
        // 0ms
        res = new ArrayList<>();
        helper(root);
        return res;
    }

    private void helper(TreeNode node) {
        if (node == null)
            return;
        res.add(node.val);
        if (node.left != null)
            helper(node.left);
        if (node.right != null)
            helper(node.right);
        return;
    }

    public List<Integer> preorderTraversal2(TreeNode root) {
        // 0ms
        List<Integer> res = new LinkedList<Integer>();
        Stack<TreeNode> rights = new Stack<TreeNode>();
        while(root != null) {
            res.add(root.val);
            if (root.right != null) {
                rights.push(root.right);
            }
            root = root.left;
            if (root == null && !rights.isEmpty()) {
                root = rights.pop();
            }
        }
        return res;
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr.append("," + Integer.toString(list.get(i)));
        }

        return resultStr.append("]").toString();
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds.split(","));
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        List<Integer> result = preorderTraversal(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
