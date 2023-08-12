import java.util.*;

public class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        // 60ms - 63ms
        Map<Integer,TreeNode> map = new HashMap<Integer, TreeNode>();
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < descriptions.length; i++) {
            TreeNode parent, child;
            if (map.containsKey(descriptions[i][0])) {
                parent = map.get(descriptions[i][0]);  
            } else {
                parent = new TreeNode(descriptions[i][0]); 
                map.put(descriptions[i][0],parent);
                set.add(descriptions[i][0]);
            }

            if (map.containsKey(descriptions[i][1])) {
                child = map.get(descriptions[i][1]);  
                set.remove(descriptions[i][1]);
            } else {
                child = new TreeNode(descriptions[i][1]);
                map.put(descriptions[i][1],child);
                set.remove(descriptions[i][1]);
            }
            if (descriptions[i][2] == 1) {
                parent.left = child;
            } else {
                parent.right = child;
            }
        }
        int root = 0;
        for (int value : set) {
            root = value;
        }
        return map.get(root);
    }

    public TreeNode createBinaryTree2(int[][] descriptions) {
        // 80ms - 88ms
        Set<Integer> childs = new HashSet<>();
        Map<Integer, TreeNode> valToNode = new HashMap<>();
        for (int[] d : descriptions) {
            int parent = d[0], child = d[1], left = d[2];
            valToNode.putIfAbsent(parent, new TreeNode(parent));
            valToNode.putIfAbsent(child, new TreeNode(child));
            childs.add(child);
            if (left == 1) {
                valToNode.get(parent).left = valToNode.get(child);
            } else {
                valToNode.get(parent).right = valToNode.get(child);
            }
        }
        valToNode.keySet().removeAll(childs);
        return valToNode.values().iterator().next();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] descriptions = ml.stringToIntIntArray(str_mat);
        System.out.println("descriptions = " + ml.matrixToString(descriptions));

        long start = System.currentTimeMillis();

        TreeNode result = createBinaryTree(descriptions);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
