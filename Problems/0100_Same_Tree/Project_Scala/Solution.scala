object Solution {
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
