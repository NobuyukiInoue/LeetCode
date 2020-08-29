import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def partition(self, head: ListNode, x: int) -> ListNode:
    def partition(self, head, x):
        # 32ms
        cur = head
        smaller_sentinel = ListNode(None)
        smaller_cur = smaller_sentinel
        larger_sentinel = ListNode(None)
        larger_cur = larger_sentinel

        while cur is not None:
            if cur.val < x:
                smaller_cur.next = cur
                smaller_cur = smaller_cur.next
            else:
                larger_cur.next = cur
                larger_cur = larger_cur.next
            cur = cur.next
        
        larger_cur.next = None
        smaller_cur.next = larger_sentinel.next

        return smaller_sentinel.next

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
    head = ope_l.createListNode(flds[0])
    x = int(flds[1])
    print("head = {0}, x = {1:d}".format(ope_l.ListNodeToString(head), x))

    sl = Solution()
    time0 = time.time()

    result = sl.partition(head, x)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
