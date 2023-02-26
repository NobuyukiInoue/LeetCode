# coding: utf-8

import os
import re
import sys
import time
from typing import List, Dict, Tuple, Optional

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # 35ms - 43ms
        self.maxDiff = 0
        def helper(self, node: Optional[TreeNode], v_min: int, v_max: int) -> int:
            if node is None:
                return
            self.maxDiff = max(self.maxDiff, abs(v_min - node.val))
            self.maxDiff = max(self.maxDiff, abs(v_max - node.val))
            v_min = min(v_min, node.val)
            v_max = max(v_max, node.val)
            helper(self, node.left, v_min, v_max)
            helper(self, node.right, v_min, v_max)
        helper(self, root, root.val, root.val)
        return self.maxDiff

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

    result = sl.maxAncestorDiff(root)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
