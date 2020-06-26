object OperateListNode {
    def createListNode(flds:String):ListNode = {
        if (flds.length <= 0)
            return null
        return createSubListNode(Mylib.stringToIntArray(flds), 0)
    }

    def createSubListNode(nums:Array[Int], index:Int):ListNode = {
        if (index >= nums.size)
            return null
        
        var node:ListNode = new ListNode(nums(index))
        node.next = createSubListNode(nums, index + 1)

        return node
    }

    def listNodeToString(ll:ListNode):String = {
        if (ll == null)
            return ""

        var retStr:String = ll.x.toString

        if (ll.next != null)
            retStr += " -> " + listNodeToString(ll.next)

        return retStr
    }
}
