import collections
import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode


class Solution:
#   def detectCycle(self, head: ListNode) -> ListNode:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 48ms
        nodes = collections.defaultdict(lambda: [0])
        while (head != None):
            temp = nodes[head]
            if (temp[0]):
                return head
            else:
                temp[0] = 1
            head = head.next
        return None

    def detectCycle2(self, head):
        # 52ms
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while head != fast:
                    fast = fast.next
                    head = head.next
                return head
        return None

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds[0])
    pos = int(flds[1])
    print("head = {0}, x = {1:d}".format(ope_l.ListNodeToString(head), pos))

    time0 = time.time()

    sl = Solution()
    result = sl.detectCycle(head)

    time1 = time.time()

    if result != None:
        print("result = {0}".format(ope_l.ListNodeToString(result)))
    else:
        print("result = None")
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
