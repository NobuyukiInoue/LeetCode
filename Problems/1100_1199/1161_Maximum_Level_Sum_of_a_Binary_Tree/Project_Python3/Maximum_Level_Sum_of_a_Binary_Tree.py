# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # 276ms
        row = [root]
        max_sum = root.val
        depth = 0
        ans = 1
        while row:
            depth += 1
            new_row = []
            cur_sum = 0
            for node in row:
                cur_sum += node.val
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            if cur_sum > max_sum:
                max_sum = cur_sum
                ans = depth
            row = new_row
        return ans
    
    def maxLevelSum2(self, root: TreeNode) -> int:
        # 328ms
        sums = []
        def dfs(node, level):
            if node is None:
                return
            if len(sums) <= level:
                sums.append(node.val)
            else:
                sums[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return sums.index(max(sums)) + 1

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

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds)
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.maxLevelSum(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
