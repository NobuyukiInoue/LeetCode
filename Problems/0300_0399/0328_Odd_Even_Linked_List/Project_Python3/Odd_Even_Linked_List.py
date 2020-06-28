import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
#   def oddEvenList(self, head: ListNode) -> ListNode:
    def oddEvenList(self, head):
        # 40ms
        if not head or not head.next:
            return head

        next_head = head.next
        cursor = head
        count = 1
        last_odd_node = None

        while cursor:
            if count % 2 == 1:
                last_odd_node = cursor
            temp_next = cursor.next
            if cursor.next:
                cursor.next = cursor.next.next
            cursor = temp_next
            count += 1

        last_odd_node.next = next_head

        return head

    def oddEvenList2(self, head):
        # 48ms
        if head == None:
            return None
        count = 0
        list_odd, list_even = [], []
        while head != None:
            if count % 2 == 0:
                list_even.append(head.val)
            else:
                list_odd.append(head.val)
            count += 1
            head = head.next

        if len(list_even) > 0:
            res = ListNode(list_even[0])
            res_head = res
            for i in range(1, len(list_even)):
                res.next = ListNode(list_even[i])
                res = res.next

            if len(list_odd) > 0:
                res.next = ListNode(list_odd[0])
                res = res.next
                for i in range(1, len(list_odd)):
                    res.next = ListNode(list_odd[i])
                    res = res.next

        return res_head

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
    if len(flds) == 0:
        head = None
    else:
        head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()

    result = sl.oddEvenList(head)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
