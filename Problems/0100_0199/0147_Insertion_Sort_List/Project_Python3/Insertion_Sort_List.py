import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 40ms
        if not head:
            return head
        nodeList = []
        cur = head
        while cur != None:
            nodeList.append(cur.val)
            cur = cur.next

        nodeList.sort()
        print(nodeList)
        res = ListNode(nodeList[0])
        cur = res
        for i in range(1, len(nodeList)):
            cur.next = ListNode(nodeList[i])
            cur = cur.next
        return res

    def insertionSortList2(self, head: ListNode) -> ListNode:
        # 128ms
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            temp = cur.next
            cur.next = temp.next
            temp.next = p.next
            p.next = temp
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
    flds = temp.replace(", ", ",").replace("\"", "").replace("[", "").replace("]", "").rstrip()

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.insertionSortList(head)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
