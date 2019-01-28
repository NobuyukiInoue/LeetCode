import scala.io.Source

object Main {
    def set_node(flds:Array[String], depth:Int, pos:Int):TreeNode = {
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
        node.left = set_node(flds, depth + 1, 2*pos)
        node.right = set_node(flds, depth + 1, 2*pos + 1)

        return node
    }

    def print_int_array(nums:Array[Int]):String = {
        if (nums.size <= 0)
            return ""

        var resultStr:String = nums(0).toString
        for (i <- 1 until nums.length) {
            resultStr += ", " + nums(i).toString
        }

        return resultStr
    }

    def loop_main(args:String) {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var nums_str1:Array[String] = flds(0).split(",")
        var nums_str2:Array[String] = flds(1).split(",")

        var t1:TreeNode = set_node(nums_str1, 0, 0);
        var t2:TreeNode = set_node(nums_str2, 0, 0);
        println("t1 = \n" + OutputTreeNode.output(t1))
        println("t2 = \n" + OutputTreeNode.output(t1))
        println("t1 = " + OutputTreeNode.tree2str(t1))
        println("t2 = " + OutputTreeNode.tree2str(t2))

        val time_start = System.currentTimeMillis

        var result:TreeNode = Solution.mergeTrees(t1, t2)

        val time_end = System.currentTimeMillis

        println("result = \n" + OutputTreeNode.output(result))
        println("result = " + OutputTreeNode.tree2str(result))
        println("Execute time: " + (time_end - time_start) + " ms")
    }

    def main(args:Array[String]) {
        var className:String = new Object(){}.getClass().getEnclosingClass().getName()

        if (args.size < 1) {
            println("Usage)\n" +
                    "scala " + className.diff("$") + " <testdataFile>\n")
            sys.exit()
        }

        val s = Source.fromFile(args(0))
        try {
            for (line <- s.getLines) {
                println("args = " + line)
                loop_main(line)
            }
        } finally {
            s.close
        }
    }
}
