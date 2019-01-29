import scala.io.Source

object Main {
    def str_to_int_array(flds:String):Array[Int] = {
        var nums_str:Array[String] = flds.split(",")
        var nums:Array[Int] = new Array[Int](nums_str.size)

        for (i <- 0 until nums_str.length) {
            nums(i) = nums_str(i).toInt
        }

        return nums
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

    def set_nodes(nums:Array[Int], index:Int):ListNode = {
        if (index >= nums.size)
            return null
        
        var node:ListNode = new ListNode(nums(index))
        node.next = set_nodes(nums, index + 1)

        return node
    }

    def output_nodes(ll:ListNode):String = {
        var retStr:String = ll.x.toString

        if (ll.next != null)
            retStr += " -> " + output_nodes(ll.next)

        return retStr
    }

    def loop_main(args:String) {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var nums1:Array[Int] = str_to_int_array(flds(0))
        var nums2:Array[Int] = str_to_int_array(flds(1))
        println("nums1 = " + print_int_array(nums1))
        println("nums2 = " + print_int_array(nums2))

        var l1:ListNode = set_nodes(nums1, 0)
        var l2:ListNode = set_nodes(nums2, 0)
        println("l1 = " + output_nodes(l1))
        println("l2 = " + output_nodes(l2))
 
        val time_start = System.currentTimeMillis

        var result:ListNode = Solution.addTwoNumbers(l1, l2);

        val time_end = System.currentTimeMillis

        println("result = " + output_nodes(result) )
        println("Execute time: " + (time_end - time_start) + " ms\n")
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
