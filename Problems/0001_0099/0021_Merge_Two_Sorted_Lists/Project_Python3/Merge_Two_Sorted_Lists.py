import os
import sys
import time

from typing import List, Dict, Tuple, Optional

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 54ms - 66ms
        newHead = dummyHead = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 68ms - 79ms
        nums = []
        cur = list1
        while not cur is None:
            nums.append(cur.val)
            cur = cur.next
        cur = list2
        while not cur is None:
            nums.append(cur.val)
            cur = cur.next
        if len(nums) == 0:
            return None
        nums.sort()
        i, newHead = 1, ListNode(nums[0])
        cur = newHead
        while i < len(nums):
            cur.next = ListNode(nums[i])
            cur = cur.next
            i += 1
        return newHead
    
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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    ope_l = OperateListNode()
    if flds[0] == "[]":
        list1 = None
    else:
        list1 = ope_l.createListNode(flds[0])
    if flds[1] == "[]":
        list2 = None
    else:
        list2 = ope_l.createListNode(flds[1])
    print("list1 = {0}".format(ope_l.ListNodeToString(list1)))
    print("list2 = {0}".format(ope_l.ListNodeToString(list2)))

    sl = Solution()
    time0 = time.time()

    result = sl.mergeTwoLists(list1, list2)

    time1 = time.time()

    print("result = {0}".format(ope_l.ListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
