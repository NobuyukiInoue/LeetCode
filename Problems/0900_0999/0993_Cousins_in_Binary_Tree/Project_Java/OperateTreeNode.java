import java.util.ArrayList;
import java.util.List;

public class OperateTreeNode {
    public TreeNode createTreeNode(String flds) {
         return createTreeNode(flds.split(","), 0, 0);
    }

    public TreeNode createTreeNode(String[] flds, int depth, int pos) {
        if (flds.length == 0)
            return null;

        int cur_pos = 0;
        for (int i = 0; i < depth; ++i)
            cur_pos += (int)Math.pow(2, i);
        
        if (cur_pos + pos > flds.length - 1)
            return null;
        
        if (flds[cur_pos + pos].equals("null"))
            return null;

        try {
            TreeNode node = new TreeNode(Integer.parseInt(flds[cur_pos + pos]));
            node.left = createTreeNode(flds, depth + 1, 2*pos);
            node.right = createTreeNode(flds, depth + 1, 2*pos + 1);

            return node;

        } catch (Exception e) {
            System.out.println("\n" +  e + "\n" +
                              "createTreeNode() Error ... flds[" + Integer.toString(cur_pos + pos) + "] = " + flds[cur_pos + pos] + "\n");
            System.exit(1);

            return null;

        }
    }

    List<String> resultList;

    public String treeToStaircaseString(TreeNode node) {
        resultList = new ArrayList<String>();

        String resultStr = treeToStaircaseSubString(node, 0);
        resultList.clear();

        return resultStr;
    }

    private String treeToStaircaseSubString(TreeNode node, int n) {
        if (node == null)
            return "";
        
        if (resultList.size() <= n)
            resultList.add("(" + Integer.toString(node.val) + ")");
        else
            resultList.set(n, resultList.get(n) + ",(" + Integer.toString(node.val) + ")");

        if (node.left != null)
            treeToStaircaseSubString(node.left, n + 1);
        if (node.right != null)
            treeToStaircaseSubString(node.right, n + 1);

        return String.join("\n", resultList) + "\n";
    }

    public String tree2str(TreeNode node) {
        if (node == null)
            return "";

        String resultStr = Integer.toString(node.val);

        if (node.left == null && node.right == null)
            return resultStr;

        resultStr += "(" + tree2str(node.left) + ")";
        if (node.right != null)
            resultStr += "(" + tree2str(node.right) + ")";

        return resultStr;
    }
}
