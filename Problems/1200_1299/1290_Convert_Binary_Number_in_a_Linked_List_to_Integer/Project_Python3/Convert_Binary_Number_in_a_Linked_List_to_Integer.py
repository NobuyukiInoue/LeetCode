import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def getDecimalValue(self, head: ListNode) -> int:
    def getDecimalValue(self, head):
        # 24ms
        total = 0
        while head is not None:
            total *= 2
            total += head.val
            head = head.next
        return total

    def getDecimalValue2(self, head):
        # 28ms
        total = 0
        while head is not None:
            total <<= 1
            total += head.val
            head = head.next
        return total

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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.getDecimalValue(head)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
