import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        if head is None or k < 2:
            return head
        
        next_head = head
        for i in range(k - 1):
            next_head = next_head.next
            if next_head is None:
                return head
        ret = next_head
        
        current = head
        while next_head:
            tail = current
            prev = None
            for i in range(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            tail.next = next_head or current
                
        return ret

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_l = OperateListNode()
    head = ope_l.createListNode(flds[0])
    k = int(flds[1])
    print("head = {0}, k = {1:d}".format(ope_l.ListNodeToString(head), k))

    sl = Solution()
    time0 = time.time()

    result = sl.reverseKGroup(head, k)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
