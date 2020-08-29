# coding: utf-8

import os
import sys
import time

from TreeNode.Codec import Codec
from TreeNode.TreeNode import TreeNode
from TreeNode.OperateTreeNode import OperateTreeNode

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        def traverse(root):
            if root is None:
                return
            else:
                traverse(root.left)
                inorder.append(root)
                traverse(root.right)
        traverse(root)
        n = len(inorder)
        for i in range(n-2, -1, -1):
            inorder[i].val += inorder[i+1].val
        return root
    
    def convertBST_work(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nums = []
        self.getAllVal(root)
        self.nums.sort(reverse=True)
        self.setGreater(root)
        return root
  
    def getAllVal(self, node):
        if node is None:
            return
        self.nums.append(node.val)
        if node.left is not None:
            self.getAllVal(node.left)
        if node.right is not None:
            self.getAllVal(node.right)

    def setGreater(self, node):
        if node is None:
            return
        node.val += self.calc_addVal(node.val)
        if node.left is not None:
            self.setGreater(node.left)
        if node.right is not None:
            self.setGreater(node.right)
    
    def calc_addVal(self, currentVal):
        addVal = 0
        for i in range(len(self.nums)):
            if self.nums[i] > currentVal:
                addVal += self.nums[i]
            else:
                break
        return addVal

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

    result = sl.convertBST(root)

    time1 = time.time()
    print("result = \n{0}".format(ope_t.treeToStaircaseString(result)))
    print("result = {0}".format(ope_t.tree2str(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
