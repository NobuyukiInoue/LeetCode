import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Operate_TreeNode {
    public TreeNode set_TreeNode(String[] flds) {
         return set_TreeNode(flds, 0, 0);
    }

    public TreeNode set_TreeNode(String[] flds, int depth, int pos) {
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
            node.left = set_TreeNode(flds, depth + 1, 2*pos);
            node.right = set_TreeNode(flds, depth + 1, 2*pos + 1);

            return node;
        } catch (Exception e) {
            System.out.println("\n" +  e + "\n" +
                              "set_TreeNode() Error ... flds[" + Integer.toString(cur_pos + pos) + "] = " + flds[cur_pos + pos] + "\n");
            System.exit(1);

            return null;
        }
    }

    List<String> resultStr;

    public String output_TreeNode(TreeNode node) {
        resultStr = new ArrayList<String>();

        String outStr = set_ResultStr(node, 0);
        resultStr.clear();

        return outStr;
    }

    private String set_ResultStr(TreeNode node, int n) {
        if (node == null)
            return "";
        
        if (resultStr.size() <= n)
            resultStr.add("(" + Integer.toString(node.val) + ")");
        else
            resultStr.set(n, resultStr.get(n) + ",(" + Integer.toString(node.val) + ")");

        if (node.left != null)
            set_ResultStr(node.left, n + 1);
        if (node.right != null)
            set_ResultStr(node.right, n + 1);

        String outputStr = "";
        for(String s : resultStr) {
            outputStr += s + "\n";
        }

        return outputStr;
    }

    public String Tree2str(TreeNode t) {
        if (t == null)
            return "";

        String resultStr = Integer.toString(t.val);

        if (t.left == null && t.right == null)
            return resultStr;

        resultStr += "(" + Tree2str(t.left) + ")";
        if (t.right != null)
            resultStr += "(" + Tree2str(t.right) + ")";

        return resultStr;
    }
}
