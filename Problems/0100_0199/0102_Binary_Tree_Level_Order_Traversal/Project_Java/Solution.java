import java.util.*;

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // 0ms
        List<List<Integer>> resultList = new ArrayList<List<Integer>>();
        helper(root, resultList, 0);
        return resultList;
    }

    private void helper(TreeNode node, List<List<Integer>> resultList, int level) {
        if (node == null)
            return;
        if (resultList.size() < level + 1)
            resultList.add(new LinkedList<Integer>());
        resultList.get(level).add(node.val);
        helper(node.left, resultList, level + 1);
        helper(node.right, resultList, level + 1);
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

        List<List<Integer>> result = levelOrder(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
