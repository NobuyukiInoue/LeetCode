import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def middleNode(self, head: ListNode) -> ListNode:
    def middleNode(self, head):
        if not head.next:
            return head
        ar, depth = [], 1
        while head.next:
            head = head.next
            depth += 1
            ar.append(head)
        ar.append(head)
        return ar[depth//2 - 1]

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.middleNode(head)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
