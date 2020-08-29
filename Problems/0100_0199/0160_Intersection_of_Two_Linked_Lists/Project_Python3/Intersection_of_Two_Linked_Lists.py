# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

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
            #if runner_a == runner_b:
            if self.isSameNode(runner_a, runner_b):
                return runner_a
            else:
                runner_a = runner_a.next
                runner_b = runner_b.next
        return None
    
    def isSameNode(self, nodeA, nodeB):
        if nodeA.val != nodeB.val:
            return False
        if nodeA.next is None or nodeB.next is None:
            return True
        return self.isSameNode(nodeA.next, nodeB.next)

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tempHeadA = headA
        while tempHeadA is not None:
            tempHeadB = headB
            while tempHeadB is not None:
                if self.check_equal(tempHeadA, tempHeadB):
                    return tempHeadA
                tempHeadB = tempHeadB.next
            tempHeadA = tempHeadA.next
        return None

    def check_equal(self, headA, headB):
        tempHeadA = headA
        tempHeadB = headB
        while tempHeadA.val == tempHeadB.val:
            if tempHeadA.next is None and tempHeadB.next is None:
                return True
            elif tempHeadA.next is None:
                return False
            elif tempHeadB.next is None:
                return False
            tempHeadA = tempHeadA.next
            tempHeadB = tempHeadB.next
        return False

    def check_equal_old(self, headA, headB):
        if headA is None and headB is None:
            return True
        elif headA is None:
            return False
        elif headB is None:
            return False
        if headA.val == headB.val:
            return self.check_equal(headA.next, headB.next)

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_l = OperateListNode()
    node1 = ope_l.createListNode(flds[0])
    node2 = ope_l.createListNode(flds[1])

    print("node1 = {0}".format(ope_l.ListNodeToString(node1)))
    print("node2 = {0}".format(ope_l.ListNodeToString(node2)))

    sl = Solution()
    time0 = time.time()

    common_node = sl.getIntersectionNode(node1, node2)

    time1 = time.time()

    print("common_node = {0}".format(ope_l.ListNodeToString(common_node)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
