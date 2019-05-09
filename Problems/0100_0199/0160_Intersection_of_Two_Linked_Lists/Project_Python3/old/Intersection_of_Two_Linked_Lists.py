# coding: utf-8

import sys
import time

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        reset = 0
        runner_a = headA
        runner_b = headB
        while reset <= 2:
            if not runner_a:
                runner_a = headB
                reset += 1
            if not runner_b:
                runner_b = headA
                reset += 1
            if runner_a == runner_b:
                return runner_a
            else:
                runner_a = runner_a.next
                runner_b = runner_b.next
        return None

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempHeadA = headA
        while tempHeadA != None:
            tempHeadB = headB
            while tempHeadB != None:
                if self.check_equal(tempHeadA, tempHeadB):
                    return tempHeadA
                tempHeadB = tempHeadB.next
            tempHeadA = tempHeadA.next
        return None

    def check_equal(self, headA, headB):
        tempHeadA = headA
        tempHeadB = headB
        while tempHeadA.val == tempHeadB.val:
            if tempHeadA.next == None and tempHeadB.next == None:
                return True
            elif tempHeadA.next == None:
                return False
            elif tempHeadB.next == None:
                return False
            tempHeadA = tempHeadA.next
            tempHeadB = tempHeadB.next
        return False

    def check_equal_old(self, headA, headB):
        if headA == None and headB == None:
            return True
        elif headA == None:
            return False
        elif headB == None:
            return False
        if headA.val == headB.val:
            return self.check_equal(headA.next, headB.next)


def set_node(data):
    node = ListNode(data[0])
    temp_node = node

    for i in range(1,len(data)):
        temp_node.next = ListNode(data[i])
        temp_node = temp_node.next
    
    return node


def output_node(node):
    if node == None:
        return 'None'
    tempStr = node.val
    temp_node = node.next
    while temp_node != None:
        tempStr += ',' + temp_node.val
        temp_node = temp_node.next
    return tempStr


def main():
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    tempStr = args[1].rstrip()
    tempArgs = tempStr.split('\t')

    flds1 = tempArgs[0].split(',')
    flds2 = tempArgs[1].split(',')
    node1 = set_node(flds1)
    node2 = set_node(flds2)

    print("node1 p = %s" %(output_node(node1)))
    print("node2 p = %s" %(output_node(node2)))

    time0 = time.time()

    sl = Solution()
    common_node = sl.getIntersectionNode(node1, node2)
    print("common_node = %s" %(output_node(common_node)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
