import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def rotateRight(self, head: ListNode, k: int) -> ListNode:
    def rotateRight(self, head, k):
        # 24ms
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        i = 0
        while fast.next is not None:
            fast = fast.next
            i += 1

        j = i - k%i
        while j > 0:
            slow = slow.next
            j -= 1

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next

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
    k = int(flds[1])
    print("head = {0}, k = {1:d}".format(ope_l.ListNodeToString(head), k))

    sl = Solution()
    time0 = time.time()

    result = sl.rotateRight(head, k)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
