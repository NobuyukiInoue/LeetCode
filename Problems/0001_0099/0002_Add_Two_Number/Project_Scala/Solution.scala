object Solution {
    def addTwoNumbers(l1: ListNode, l2: ListNode): ListNode = {
        var dummyHead:ListNode = new ListNode(0)
        var p:ListNode = l1
        var q:ListNode = l2
        var curr:ListNode = dummyHead
        var carry:Int = 0

        while (p != null || q != null)
        {
            var x:Int = 0
            var y:Int = 0

            if (p != null)
                x = p.x
            else
                x = 0

            if (q != null)
                y = q.x
            else
                y = 0

            var sum:Int = carry + x + y
            carry = sum / 10
            curr.next = new ListNode(sum % 10)
            curr = curr.next
            if (p != null)
                p = p.next
            if (q != null)
                q = q.next
        }

        if (carry > 0)
        {
            curr.next = new ListNode(carry)
        }

        return dummyHead.next
    }

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

    def main(args:String) {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var nums1:Array[Int] = str_to_int_array(flds(0))
        var nums2:Array[Int] = str_to_int_array(flds(1))
        println("nums1 = " + print_int_array(nums1))
        println("nums2 = " + print_int_array(nums2))

        var l1:ListNode = Operate_ListNode.set_ListNode(nums1, 0)
        var l2:ListNode = Operate_ListNode.set_ListNode(nums2, 0)
        println("l1 = " + Operate_ListNode.output_ListNode(l1))
        println("l2 = " + Operate_ListNode.output_ListNode(l2))
 
        val time_start = System.currentTimeMillis

        var result:ListNode = addTwoNumbers(l1, l2);

        val time_end = System.currentTimeMillis

        println("result = " + Operate_ListNode.output_ListNode(result) )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
