# coding: utf-8

import copy
import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    def reverseBetween(self, head, m, n):
        # 40ms
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next

    def reverseBetween2(self, head, m, n):
        # 36ms
        hat = ListNode(0)
        hat.next, start = head, hat

        for i in range(m):
            beforeStart, start = start, start.next

        for i in range(n - m):
            beforeStart.next, start.next, beforeStart.next.next = start.next, start.next.next, beforeStart.next

        return hat.next

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds[0])
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    flds1 = flds[1].split(",")
    m, n = int(flds1[0]), int(flds1[1])
    print("m = {0:d}, n = {1:d}".format(m, n))

    sl = Solution()
    time0 = time.time()

    result = sl.reverseBetween(head, m, n)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
