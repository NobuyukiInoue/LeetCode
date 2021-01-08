import os
import sys
import time
from typing import List, Dict, Tuple

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 64ms
        l1_str, l2_str = "", ""
        temp = l1
        while temp is not None:
            l1_str += str(temp.val)
            temp = temp.next
        temp = l2
        while temp is not None:
            l2_str += str(temp.val)
            temp = temp.next
        res_str = str(int(l1_str) + int(l2_str))
        res = ListNode(res_str[0])
        i = 1
        temp = res
        while i < len(res_str):
            temp.next = ListNode(res_str[i])
            temp = temp.next
            i += 1
        return res

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_l = OperateListNode()
    l1 = ope_l.createListNode(flds[0])
    l2 = ope_l.createListNode(flds[1])
    print("l1 = {0}".format(ope_l.ListNodeToString(l1)))
    print("l2 = {0}".format(ope_l.ListNodeToString(l2)))

    sl = Solution()
    time0 = time.time()

    result = sl.addTwoNumbers(l1, l2)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
