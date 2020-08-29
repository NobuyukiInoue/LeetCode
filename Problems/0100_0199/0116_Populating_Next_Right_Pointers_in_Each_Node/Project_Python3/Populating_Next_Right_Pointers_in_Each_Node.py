# coding: utf-8

import os
import sys
import time

from Node.Node import Node
from Node.OperateNode import OperateNode

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 64m
        if not root:
            return None
        cur  = root
        next = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next
                next = cur.left
        
        return root

    def connect2(self, root: 'Node') -> 'Node':
        # 80ms
        if root is None:
            return root
        self.levels, self.pos = [], []
        self.get_node(root, 0)
        self.set_next(root, 0)
        return root

    def get_node(self, node, level):
        if len(self.levels) <= level:
            self.levels.append([node])
            self.pos.append(0)
        else:
            self.levels[level].append(node)
        if node.left is not None:
            self.get_node(node.left, level + 1)
        if node.right is not None:
            self.get_node(node.right, level + 1)

    def set_next(self, node, level):
        if len(self.levels[level]) > self.pos[level] + 1:
            node.next = self.levels[level][self.pos[level] + 1]
            self.pos[level] += 1
        else:
            node.next = None
        if node.left is not None:
            self.set_next(node.left, level + 1)
        if node.right is not None:
            self.set_next(node.right, level + 1)

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

    ope_n = OperateNode()
    root = ope_n.createNode(flds)
    print("root = \n{0}".format(ope_n.treeToStaircaseString(root)))

    sl = Solution()
    time0 = time.time()

    result = sl.connect(root)

    time1 = time.time()

    print("result = \n{0}".format(ope_n.treeToStaircaseString_with_next(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
