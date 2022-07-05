import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 120ms
        fast = slow = lo = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        hi = None
        while slow:
            slow.next, slow, hi = hi, slow.next, slow
        
        while lo != hi and lo.next != hi:
            lo.next, lo, hi.next, hi = hi, lo.next, lo.next, hi.next

        return head 

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 124ms
        if head is None:
            return None
        C, A = head, []
        while C is not None:
            A.append(C);
            C = C.next
        M = len(A)//2
        for i in range(M):
            A[i].next, A[-(i+1)].next = A[-(i+1)], A[i+1]
        A[M].next = None

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

    sl.reorderList(head)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(head)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
