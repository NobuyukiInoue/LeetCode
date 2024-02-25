import os
import sys
import time

from typing import List, Dict, Tuple, Optional
from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 38ms - 41ms
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        node = head
        part_size, extra = length//k, length%k
        ans = []
        for _i in range(k):
            ans.append(node)
            current_part_size = part_size + 1 if extra > 0 else part_size
            extra -= 1
            for _j in range(current_part_size - 1):
                node = node.next
            if node:
                node.next, node = None, node.next
        return ans

def arrListNodeToString(list_arr) -> str:
    res = ""
    ope_l = OperateListNode()
    for arr in list_arr:
        if res == "":
            res += "[" + ope_l.ListNodeToString(arr) + "]"
        else:
            res += ", [" + ope_l.ListNodeToString(arr) + "]"
    return "[" + res + "]"

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
    head = ope_l.createListNode(flds[0])
    k = int(flds[1])
    print("head = {0}, k = {1:d}".format(ope_l.ListNodeToString(head), k))

    sl = Solution()
    time0 = time.time()

    result = sl.splitListToParts(head, k)

    time1 = time.time()

    print("result = {0}".format(arrListNodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
