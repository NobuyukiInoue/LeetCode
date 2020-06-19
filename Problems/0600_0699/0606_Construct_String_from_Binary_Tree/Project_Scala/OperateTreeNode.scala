object OperateTreeNode {
    def createTreeNode(flds:String):TreeNode = {
        return createSubTreeNode(flds.split(","), 0, 0)
    }

    def createSubTreeNode(flds:Array[String], depth:Int, pos:Int):TreeNode = {
        if (flds.size <= 0)
            return null

        var cur_pos:Int = 0
        for (i <- 0 until depth)
            cur_pos = cur_pos + Math.pow(2, i).toInt
        
        if (cur_pos + pos > flds.size - 1)
            return null
        
        if (flds(cur_pos + pos) == "null")
            return null

        try {
            var node:TreeNode = new TreeNode(flds(cur_pos + pos).toInt)
            node.left = createSubTreeNode(flds, depth + 1, 2*pos)
            node.right = createSubTreeNode(flds, depth + 1, 2*pos + 1)

            return node

        } catch {
            case e: Exception =>

            println("\n" +  e + "\n" + "createTreeNode() Error ... flds(" + (cur_pos + pos).toString + ") = " + flds(cur_pos + pos) + "\n");
            sys.exit()
        }
    }

    var resultList:Array[String] = Array.empty

    def treeToStaircaseString(node:TreeNode):String = {
        var resultStr:String = treeToStaircaseSubString(node, 0)
        resultList = Array.empty;

        return resultStr;
    }

    def treeToStaircaseSubString(node:TreeNode, n:Int):String = {
        if (node == null)
            return ""
        
        if (resultList.size <= n) {
            resultList = resultList :+ "(" + node.value.toString() + ")"
        } else
            resultList(n) = resultList(n) + ",(" + node.value.toString() + ")"

        if (node.left != null)
            treeToStaircaseSubString(node.left, n + 1)
        if (node.right != null)
            treeToStaircaseSubString(node.right, n + 1)

        return resultList.mkString("\n") + "\n";
    }

    def tree2str(node:TreeNode):String = {
        if (node == null)
            return ""

        var resultStr:String = node.value.toString()

        if (node.left == null && node.right == null)
            return resultStr

        resultStr = resultStr + "(" + tree2str(node.left) + ")"
        if (node.right != null)
            resultStr = resultStr + "(" + tree2str(node.right) + ")"

        return resultStr
    }
}
