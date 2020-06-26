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

    def main(args:String): Unit = {
        var temp:String = args.stripLineEnd.replaceAll(" ", "").replaceFirst("\\[\\[", "").replaceFirst("\\]\\]", "")
        var flds:Array[String] = temp.split("\\],\\[")

        var l1:ListNode = OperateListNode.createListNode(flds(0))
        var l2:ListNode = OperateListNode.createListNode(flds(1))
        println("l1 = " + OperateListNode.listNodeToString(l1))
        println("l2 = " + OperateListNode.listNodeToString(l2))
 
        val time_start = System.currentTimeMillis

        var result:ListNode = addTwoNumbers(l1, l2);

        val time_end = System.currentTimeMillis

        println("result = " + OperateListNode.listNodeToString(result) )
        println("Execute time: " + (time_end - time_start) + " ms\n")
    }
}
