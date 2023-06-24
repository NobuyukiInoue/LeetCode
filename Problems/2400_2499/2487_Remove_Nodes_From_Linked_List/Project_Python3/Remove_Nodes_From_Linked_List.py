import os
import sys
import time
import math

from typing import List, Dict, Tuple, Optional

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def removeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1259ms - 1309ms
        if head:
            head.next = self.removeNodes2(head.next)
            if head.next and head.val < head.next.val:
                return head.next
        return head

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1004ms - 1081ms
        head = self.reverseList(head)
        maximum = -math.inf
        current = head
        prev = None
        while (current):
            tmp_next = current.next
            if current.val >= maximum:
                maximum = current.val
                if (prev):
                    prev.next = current
                    current.next = None
                else:
                    head.next = None
                prev = current
            current = tmp_next
        return self.reverseList(head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while (current):
            old_next = current.next
            current.next = prev
            prev = current
            current = old_next
        return prev

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.removeNodes(head)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
