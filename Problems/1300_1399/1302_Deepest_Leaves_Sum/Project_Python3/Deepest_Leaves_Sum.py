# coding: utf-8

import collections
import os
import re
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode
from typing import List, Dict, Tuple, Optional

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # 186ms - 195ms
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)

    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        # 211ms - 225ms
        def helper(node: Optional[TreeNode], depth: int, highest_depth: int, total: int) -> Tuple[int, int]:
            if node.left is not None:
                (highest_depth, total) = helper(node.left, depth + 1, highest_depth, total)
            if node.right is not None:
                (highest_depth, total) = helper(node.right, depth + 1, highest_depth, total)
            if node.left is None and node.right is None:
                if depth > highest_depth:
                    highest_depth = depth
                    total = node.val
                elif depth == highest_depth:
                    total += node.val
            return (highest_depth, total)
        (_, res) = helper(root, 0, 0, 0)
        return res

    def deepestLeavesSum3(self, root: Optional[TreeNode]) -> int:
        # 237ms - 245ms
        def helper(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            sums[depth] += node.val
            if not node.left is None:
                helper(node.left, depth + 1)
            if not node.right is None:
                helper(node.right, depth + 1)
        sums = collections.defaultdict(int)
        helper(root, 0)
        return sums[max(sums.keys())]

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
    temp = re.sub('#.*', "", temp)
    temp = re.sub('//.*', "", temp)
    if len(temp) == 0:
        return

    flds = temp.replace(", ",",").replace("\"","").replace("[","").replace("]","").rstrip()

    ope_t = OperateTreeNode()
    root = ope_t.createTreeNode(flds.split(","))
    print("root = \n{0}".format(ope_t.treeToStaircaseString(root)))
    print("root = {0}".format(ope_t.tree2str(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.deepestLeavesSum(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
