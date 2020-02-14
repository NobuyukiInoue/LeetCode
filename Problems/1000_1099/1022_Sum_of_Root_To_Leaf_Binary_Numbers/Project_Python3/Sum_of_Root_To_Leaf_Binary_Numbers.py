# coding: utf-8

import os
import sys
import time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
#   def sumRootToLeaf(self, root: TreeNode) -> int:
    def sumRootToLeaf(self, root):
        # 36ms-44ms
        if not root:
            return 0

        def sub_sumRootToLeaf(root, val):
            val = val*2 + root.val
            if root.left == root.right:
                return val
            l, r = 0, 0
            if root.left != None:
                l = sub_sumRootToLeaf(root.left, val)
            if root.right != None:
                r = sub_sumRootToLeaf(root.right, val)
            return l + r

        return sub_sumRootToLeaf(root, 0)

    def sub_sumRootToLeaf2(self, root):
        # 44-60ms
        if not root:
            return []

        def sumRootToLeafSub(node, route):
            if node == None:
                self.result.append([route])
                return
            route.append(node.val)
            if node.left == None and node.right == None:
                self.result.append(route)
                return
            if node.left != None:
                sumRootToLeafSub(node.left, route[:])
            if node.right != None:
                sumRootToLeafSub(node.right, route[:])
            return

        route = []
        self.result = []
        sumRootToLeafSub(root, route)

        total = 0
        for tmp in self.result:
            subtotal = 0
            for i in range(len(tmp)):
                subtotal = subtotal*2 + tmp[i]
            total += subtotal
        return total

class output_TreeNode:
    def output(self, node):
        self.resultStr = []
        self.output_TreeNode(node, 0)
        return self.print_resultStr()

    def output_TreeNode(self, node, n):
        if node == None:
            return
        if len(self.resultStr) <= n:
            self.resultStr.append("(" + str(node.val) + ")")
        else:
            self.resultStr[n] += ",(" + str(node.val) + ")"
        if node.left != None:
            self.output_TreeNode(node.left, n + 1)
        if node.right != None:
            self.output_TreeNode(node.right, n + 1)
        return

    def print_resultStr(self):
        outputStr = ""
        for i in range(len(self.resultStr)):
            outputStr += self.resultStr[i] + "\n"
        self.resultStr.clear()
        return outputStr

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""

        resultStr = str(t.val)

        if t.left == None and t.right == None:
            return resultStr

        resultStr += "(" + self.tree2str(t.left) + ")"
        if t.right != None:
            resultStr += "(" + self.tree2str(t.right) + ")"

        return resultStr

def set_node(flds, depth, pos):
    if len(flds) <= 0:
        return None

    cur_pos = 0
    for i in range(depth):
        cur_pos += 2 ** i
    
    if cur_pos + pos > len(flds) - 1:
        return None

    if flds[cur_pos + pos] == 'null':
        return None

    node = TreeNode(int(flds[cur_pos + pos]))
    node.left = set_node(flds, depth + 1, 2*pos)
    node.right = set_node(flds, depth + 1, 2*pos + 1)

    return node

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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip().split(",")
    root = set_node(flds, 0, 0)

    ol = output_TreeNode()
    print("root = \n%s" %(ol.output(root)))
    print("root = %s\n" %(ol.tree2str(root)))

    time0 = time.time()

    sl = Solution()
    result = sl.sumRootToLeaf(root)

    time1 = time.time()

    print("result = %d" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
