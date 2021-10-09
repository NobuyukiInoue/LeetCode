object Solution {
    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        if (p == null && q == null) return true
        if (p == null || q == null) return false

        p.value == q.value && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
    }

    def main(args:String): Unit = {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var p:TreeNode = OperateTreeNode.createTreeNode(flds(0));
        var q:TreeNode = OperateTreeNode.createTreeNode(flds(1));
        print("p = \n" + OperateTreeNode.treeToStaircaseString(p))
        println("p = " + OperateTreeNode.tree2str(p))
        print("q = \n" + OperateTreeNode.treeToStaircaseString(q))
        println("q = " + OperateTreeNode.tree2str(q))

        val time_start = System.currentTimeMillis

        var result: Boolean = isSameTree(p, q)

        val time_end = System.currentTimeMillis

        println("result = " + result.toString)
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
