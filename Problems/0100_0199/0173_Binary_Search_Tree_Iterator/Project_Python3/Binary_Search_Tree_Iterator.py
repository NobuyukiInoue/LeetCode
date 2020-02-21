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

class BSTIterator:
    # 72ms

#   def __init__(self, root: TreeNode):
    def __init__(self, root):
        self.nums = []
        def dfs(node):
            if node == None:
                return
            if node.left != None:
                dfs(node.left)
            self.nums.append(node.val)
            if node.right != None:
                dfs(node.right)                

        dfs(root)
        self.index = 0

#   def next(self) -> int:
    def next(self):
        """
        @return the next smallest number
        """
        if self.index < len(self.nums):
            self.index += 1
            return self.nums[self.index - 1]

#   def hasNext(self) -> bool:
    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.nums)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Solution:
    def main(self, cmds, mynode):
        for cmd in cmds:
            if cmd == "BSTIterator":
                BI = BSTIterator(mynode)
                print("BSTIterator iterator = new BSTIterator(root);")
            elif cmd == "next" and BI != None:
                print("iterator.next();\t ... {0:d}".format(BI.next()))
            elif cmd == "hasNext" and BI != None:
                print("iterator.hasNext();\t ... {0}".format(BI.hasNext()))

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
    flds = temp.replace("\"","").replace(", ",",").rstrip().split("],[[[")
    cmds = flds[0].replace("[[", "").split(",")

    node_flds = (flds[1].split("]],["))[0]
    if len(node_flds) <= 0:
        mynode = None
    else:
        mynode = set_node(node_flds.split(","), 0, 0)

    ol = output_TreeNode()
    print("mynode = \n[%s]" %(ol.output(mynode)))

    time0 = time.time()

    sl = Solution()
    sl.main(cmds, mynode)

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
