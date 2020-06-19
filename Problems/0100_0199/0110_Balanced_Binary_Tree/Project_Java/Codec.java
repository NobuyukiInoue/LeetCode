/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.*;

public class Codec {
    // 8ms

    private static final String SPLITTER = ",";
    private static final String NULLSTR = "null";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        int size = sb.length();
        return sb.delete(size - 1, size).toString();
    }

    private void buildString(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append(NULLSTR).append(SPLITTER);
        } else {
            sb.append(node.val).append(SPLITTER);
            buildString(node.left, sb);
            buildString(node.right,sb);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(SPLITTER)));
        return buildTree(nodes);
    }

    private TreeNode buildTree(Deque<String> nodes) {
        if (nodes.size() <= 0) {
            return null;
        }

        String val = nodes.remove();
        if (val.equals(NULLSTR)) {
            return null;
        } else {
            TreeNode node;
            if (val.equals("null")) {
                node = null;
            } else {
                node = new TreeNode(Integer.valueOf(val));
                node.left = buildTree(nodes);
                node.right = buildTree(nodes);
            }
            return node;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
