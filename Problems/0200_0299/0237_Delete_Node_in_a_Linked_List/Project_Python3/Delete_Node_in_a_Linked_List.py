# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node is not None:
            if node.next is not None:
                prev_node = node
                node.val = node.next.val
                node = node.next
            else:
                break
        prev_node.next = None

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
    node = ope_l.createListNode(flds[0])
    print("node = {0}".format(ope_l.ListNodeToString(node)))

    sl = Solution()
    time0 = time.time()

    sl.deleteNode(node)

    time1 = time.time()
    print("node = {0}".format(ope_l.ListNodeToString(node)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
