object Solution {
    def mergeTrees(t1: TreeNode, t2: TreeNode): TreeNode = {
        if (t1 == null &&  t2 == null) {
            return null
        } else if (t1 != null && t2 != null) {
            var node:TreeNode = new TreeNode(t1.value + t2.value)
            node.left = mergeTrees(t1.left, t2.left)
            node.right = mergeTrees(t1.right, t2.right)
            return node
        } else if (t1 != null) {
            var node:TreeNode = new TreeNode(t1.value)
            node.left = mergeTrees(t1.left, null)
            node.right = mergeTrees(t1.right, null)
            return node
        } else if (t2 != null) {
            var node:TreeNode = new TreeNode(t2.value)
            node.left = mergeTrees(null, t2.left)
            node.right = mergeTrees(null, t2.right)
            return node
        } else {
            return null
        }
    }
}
