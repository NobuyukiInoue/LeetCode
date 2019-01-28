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
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans

    def mergeTrees_work(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        elif t1 != None and t2 != None:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif t1 != None:
            node = TreeNode(t1.val)
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
        elif t2 != None:
            node = TreeNode(t2.val)
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)

        return node

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None) and (q == None):
            return True
        elif (p == None) or (q == None):
            return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False

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

        if t.left != None:
            resultStr += "(" + self.tree2str(t.left) + ")"
        else:
            resultStr += "()"

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

    if (argc < 2):
        print("Usage: python %s <testdata.txt>" %(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("%s not found..." %argv[1])
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        print("argv[1] = %s" %temp)
        loop_main(temp)
    #    print("Hit Return to continue...")
    #    input()

def loop_main(temp):
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")
    t1 = set_node(flds[0].split(","), 0, 0)
    t2 = set_node(flds[1].split(","), 0, 0)

    ol = output_TreeNode()
    print("t1 = \n%s" %(ol.output(t1)))
    print("t2 = \n%s" %(ol.output(t2)))
    print("t1 = %s" %(ol.tree2str(t1)))
    print("t2 = %s" %(ol.tree2str(t2)))

    time0 = time.time()

    sl = Solution()
    result = sl.mergeTrees(t1, t2)

    time1 = time.time()
    print("result = \n%s" %(ol.output(result)))
    print("result = %s" %(ol.tree2str(result)))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
