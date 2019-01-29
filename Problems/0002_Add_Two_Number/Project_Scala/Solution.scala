/* Definition for singly-linked list. */

class ListNode(var _x: Int = 0) {
    var next: ListNode = null
    var x: Int = _x
}

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
}
