from .ListNode import ListNode

class OperateListNode:
    def createListNode(self, flds):
        if len(flds) <= 0:
            return None
        nums = [int(val) for val in flds.split(",")]
        return self.createSubListNode(nums, 0)

    def createSubListNode(self, nums, index):
        if index >= len(nums):
            return None

        node = ListNode(nums[index])
        node.next = self.createSubListNode(nums, index + 1)

        return node

    def ListNodeToString(self, ll):
        if ll is None:
            return ""
        retStr = str(ll.val) 

        if ll.next is not None:
            retStr += " -> " + self.ListNodeToString(ll.next)
        return retStr
