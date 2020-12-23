# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # 228ms
        if len(nums) == 0:
            return None
        i, n = self.maxnode(nums)
        node = TreeNode(n)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node

    def maxnode(self, nums: List[int]) -> Tuple:
        maxnum = -sys.maxsize
        for i, n in enumerate(nums):
            if n > maxnum:
                maxnum = n
                pos = i
        return pos, maxnum

    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        # 220ms
        def construct(l, r):
            if l > r:
                return
            elif l == r:
                return TreeNode(nums[l])
            maximum = -float('inf')
            for i in range(l, r + 1):
                if maximum < nums[i]:
                    maximum = nums[i]
                    max_index = i
            left = construct(l, max_index - 1)
            right = construct(max_index + 1,r)
            root = TreeNode(maximum)
            root.left = left
            root.right = right
            return root
        return construct(0, len(nums) - 1)

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

    nums = [int(n) for n in flds.split(",")]
    print("nums = \n{0}".format(nums))

    sl = Solution()
    time0 = time.time()

    result = sl.constructMaximumBinaryTree(nums)

    time1 = time.time()

    ope_t = OperateTreeNode()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
