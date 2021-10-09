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

        p.value == q.value && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    def main(args:String): Unit = {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var s:TreeNode = OperateTreeNode.createTreeNode(flds(0));
        var t:TreeNode = OperateTreeNode.createTreeNode(flds(1));
        print("s = \n" + OperateTreeNode.treeToStaircaseString(s))
        println("s = \n" + OperateTreeNode.tree2str(s))
        print("t = \n" + OperateTreeNode.treeToStaircaseString(t))
        println("t = \n" + OperateTreeNode.tree2str(t))

        val time_start = System.currentTimeMillis

        var result: Boolean = isSubtree(s, t)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
