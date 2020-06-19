import java.util.*;

public class OperateNode {
    public Node createNode(String flds) {
         return createSubNode(flds.split(","), 0, 0);
    }

    public Node createSubNode(String[] flds, int depth, int pos) {
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
            Node node = new Node(Integer.parseInt(flds[cur_pos + pos]));
            node.left = createSubNode(flds, depth + 1, 2*pos);
            node.right = createSubNode(flds, depth + 1, 2*pos + 1);

            return node;
        } catch (Exception e) {
            System.out.println("\n" +  e + "\n" +
                              "createSubNode() Error ... flds[" + Integer.toString(cur_pos + pos) + "] = " + flds[cur_pos + pos] + "\n");
            System.exit(1);

            return null;
        }
    }

    List<String> resultList;

    public String treeToStaircaseString(Node node) {
        resultList = new ArrayList<String>();

        String resultStr = treeToStaircaseSubString(node, 0);
        resultList.clear();

        return resultStr;
    }

    private String treeToStaircaseSubString(Node node, int n) {
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

        String resultStr = "";
        for(String s : resultList) {
            resultStr += s + "\n";
        }

        return resultStr;
    }

    public String treeToStaircaseString_with_next(Node node) {
        resultList = new ArrayList<String>();

        String resultStr = treeToStaircaseSubString_with_next(node, 0);
        resultList.clear();

        return resultStr;
    }

    private String treeToStaircaseSubString_with_next(Node node, int n) {
        if (node == null)
            return "";
        
        if (resultList.size() <= n)
            resultList.add("(" + Integer.toString(node.val) + ")");
        else
            resultList.set(n, resultList.get(n) + ",(" + Integer.toString(node.val) + ")");

        if (node.next == null)
                resultList.set(n, resultList.get(n) + ",(#)");

        if (node.left != null)
            treeToStaircaseSubString_with_next(node.left, n + 1);
        if (node.right != null)
            treeToStaircaseSubString_with_next(node.right, n + 1);

        String resultStr = "";
        for(String s : resultList) {
            resultStr += s + "\n";
        }

        return resultStr;
    }


    public String tree2str(Node node) {
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
