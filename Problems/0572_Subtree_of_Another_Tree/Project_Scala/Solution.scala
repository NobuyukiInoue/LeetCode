object Solution {
    def isSubtree(s: TreeNode, t: TreeNode): Boolean = {
        if (s.value == t.value)
            if (isSameTree(s, t))
                return true;
        if (s.left != null)
            if (isSubtree(s.left, t))
                return true;
        if (s.right != null)
            if (isSubtree(s.right, t))
                return true;
        return false;
    }

    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) return true
        if (p == null || q == null) return false

        p._value == q._value && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    def isSameTree_work(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) {
            return true;
        }
        else if (p == null || q == null)
        {
            return false;
        }

        if (p.value == q.value) {
            if (isSameTree(p.left, q.left)) {
                return isSameTree(p.right, q.right)
            }
            else {
                return false
            }
        }
        else {
            return false
        }
    }
}
