# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        curr = dummy
        while head:
            if head.val != val:
                curr.next = head
                curr = curr.next
                head = head.next
            else:
                head = head.next
        curr.next = None
        return dummy.next

    def removeElements_work(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp_node = head
        while temp_node is not None:
            if temp_node.next is not None:
                if temp_node.next.val == val:
                    temp_node.next = temp_node.next.next
            temp_node = temp_node.next
        return head

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
    str_args = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds[0])
    print("nodes = {0}".format(ope_l.ListNodeToString(head)))

    val = int(flds[1])
    print("val = {0:d}".format(val))

    sl = Solution()
    time0 = time.time()

    result = sl.removeElements(head, val)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
