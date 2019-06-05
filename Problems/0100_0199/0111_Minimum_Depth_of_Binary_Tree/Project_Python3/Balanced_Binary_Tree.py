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
#   def isBalanced(self, root: TreeNode) -> bool:
    def isBalanced(self, root):
        # 56ms
        if not root:
            return True
        def depth(node):
            if not node:    #leaves
                return 0
            left = depth(node.left) #left child's depth
            right = depth(node.right) #right child's depth
            if abs(left-right)>1:
                raise Exception #stop recursion and report unbalance
            return max(left, right)+1
        try:
            return abs(depth(root.left)-depth(root.right))<=1
        except:
            return False

    def isBalanced2(self, root):
        # 70ms
        def getNodeDepth(node):
            if node == None:
                return 0
            stack = [(node,1)]
            dep = 1
            while(len(stack)):
                first,dep=stack.pop(0)
                if first.left != None:
                    stack.append((first.left,dep+1))
                if first.right != None:
                    stack.append((first.right,dep+1))
            return dep
        if root == None:
            return True
        l = getNodeDepth(root.left)
        r = getNodeDepth(root.right)
        return abs(l-r) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

class output_TreeNode:
    def output(self, node):
        self.rootStr = []
        self.output_TreeNode(node, 0)
        return self.print_rootStr()

    def output_TreeNode(self, node, n):
        if node == None:
            return
        if len(self.rootStr) <= n:
            self.rootStr.append("(" + str(node.val) + ")")
        else:
            self.rootStr[n] += ",(" + str(node.val) + ")"
        if node.left != None:
            self.output_TreeNode(node.left, n + 1)
        if node.right != None:
            self.output_TreeNode(node.right, n + 1)
        return

    def print_rootStr(self):
        outputStr = ""
        for i in range(len(self.rootStr)):
            outputStr += self.rootStr[i] + "\n"
        self.rootStr.clear()
        return outputStr

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""

        rootStr = str(t.val)

        if t.left == None and t.right == None:
            return rootStr

        rootStr += "(" + self.tree2str(t.left) + ")"
        if t.right != None:
            rootStr += "(" + self.tree2str(t.right) + ")"

        return rootStr

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

    if (argc < 2):
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
    flds = temp.replace("\"","").replace("[","").replace("]","").rstrip()

    root = set_node(flds.split(","), 0, 0)
    ol = output_TreeNode()
    print("root = \n%s" %(ol.output(root)))
    print("root = %s\n" %(ol.tree2str(root)))

    time0 = time.time()

    sl = Solution()
    result = sl.isBalanced(root)

    time1 = time.time()

    ol = output_TreeNode()
    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
