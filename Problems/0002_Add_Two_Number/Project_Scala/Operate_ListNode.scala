object Operate_ListNode {
    def set_ListNode(nums:Array[Int]):ListNode = {
        return set_ListNode(nums, 0)
    }

    def set_ListNode(nums:Array[Int], index:Int):ListNode = {
        if (index >= nums.size)
            return null
        
        var node:ListNode = new ListNode(nums(index))
        node.next = set_ListNode(nums, index + 1)

        return node
    }

    def output_ListNode(ll:ListNode):String = {
        var retStr:String = ll.x.toString

        if (ll.next != null)
            retStr += " -> " + output_ListNode(ll.next)

        return retStr
    }
}
