import collections
import os
import sys
import time
import math

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode
from typing import List, Dict, Tuple, Optional

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 1873ms - 1917ms
        val_to_node, childs = {}, set()
        for parent, child, left in descriptions:
            childs.add(child)
            parent_node = val_to_node.setdefault(parent, TreeNode(parent))
            child_node = val_to_node.setdefault(child, TreeNode(child))
            if left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        return val_to_node[(val_to_node.keys() - childs).pop()]

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    descriptions = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("descriptions", descriptions)

    sl = Solution()
    time0 = time.time()

    result = sl.createBinaryTree(descriptions)

    time1 = time.time()

    ope_t = OperateTreeNode()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
