object Operate_TreeNode {
    def set_TreeNode(flds:Array[String]):TreeNode = {
        return set_TreeNode(flds, 0, 0)
    }

    def set_TreeNode(flds:Array[String], depth:Int, pos:Int):TreeNode = {
        if (flds.size <= 0)
            return null

        var cur_pos:Int = 0
        for (i <- 0 until depth)
            cur_pos = cur_pos + Math.pow(2, i).toInt
        
        if (cur_pos + pos > flds.size - 1)
            return null
        
        if (flds(cur_pos + pos) == "null")
            return null

        var node:TreeNode = new TreeNode(flds(cur_pos + pos).toInt)
        node.left = set_TreeNode(flds, depth + 1, 2*pos)
        node.right = set_TreeNode(flds, depth + 1, 2*pos + 1)

        return node
    }

    var resultStr:Array[String] = Array.empty

    def output_TreeNode(node:TreeNode):String = {
        set_resultStr(node, 0)
        return get_resultStr()
    }

    def set_resultStr(node:TreeNode, n:Int) {
        if (node == null)
            return
        
        if (resultStr.size <= n) {
            resultStr = resultStr :+ "(" + node.value.toString() + ")"
        } else
            resultStr(n) = resultStr(n) + ",(" + node.value.toString() + ")"

        if (node.left != null)
            set_resultStr(node.left, n + 1)
        if (node.right != null)
            set_resultStr(node.right, n + 1)

        return
    }

    def get_resultStr():String = {
        var outputStr:String = ""

        for (temp_str <- resultStr) {
            outputStr = outputStr + temp_str + "\n"
        }

        resultStr = Array.empty
        return outputStr
    }

    def tree2str(t:TreeNode):String = {
        if (t == null)
            return ""

        var resultStr:String = t.value.toString()

        if (t.left == null && t.right == null)
            return resultStr

        resultStr = resultStr + "(" + tree2str(t.left) + ")"
        if (t.right != null)
            resultStr = resultStr + "(" + tree2str(t.right) + ")"

        return resultStr
    }
}
