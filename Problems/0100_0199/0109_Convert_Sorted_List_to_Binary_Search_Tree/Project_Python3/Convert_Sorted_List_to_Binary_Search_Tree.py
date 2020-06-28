# coding: utf-8

import os
import sys
import time

from ListNode.ListNode import ListNode
from ListNode.OperateListNode import OperateListNode
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
#   def sortedListToBST(self, head: ListNode) -> TreeNode:
    def sortedListToBST(self, head):
        # 128ms
        if not head:
            return None
        result = []
        while head:
            result.append(TreeNode(head.val))
            head = head.next
        return self.helper(result)

    def helper(self, treelist):
        if len(treelist) == 0:
            return None
        if len(treelist) == 1:
            return treelist[0]
        mid = len(treelist)//2
        treelist[mid].left = self.helper(treelist[:mid])
        treelist[mid].right = self.helper(treelist[mid + 1:])
        return treelist[mid]

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
    head = ope_l.createListNode(flds)
    print("head = {0}".format(ope_l.ListNodeToString(head)))

    sl = Solution()
    time0 = time.time()
    result = sl.sortedListToBST(head)

    time1 = time.time()

    ope_t = OperateTreeNode()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
