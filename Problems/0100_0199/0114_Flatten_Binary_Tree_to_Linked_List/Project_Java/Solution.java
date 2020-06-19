import java.util.*;

public class Solution {
    private TreeNode prev = null;

    public void flatten(TreeNode root) {
        // 0ms
        if (root == null)
            return;
        flatten(root.right);
        flatten(root.left);
        root.right = prev;
        root.left = null;
        prev = root;
    }

    public void flatten2(TreeNode root) {
        // 2ms
        if (root == null)
            return;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while (!stk.isEmpty()){
            TreeNode curr = stk.pop();
            if (curr.right != null)
                 stk.push(curr.right);
            if (curr.left != null)
                 stk.push(curr.left);
            if (!stk.isEmpty())
                 curr.right = stk.peek();
            curr.left = null;
        }
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
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

        flatten(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("result = " + ope_t.tree2str(root));
        System.out.println((end - start)  + "ms\n");
    }
}
