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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 68ms
        if p == root or q == root:
            return root
        if not root:
            return None
        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        if left_node and right_node:
            return root
        if left_node:
            return left_node
        return right_node


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

def set_target_node(node: 'TreeNode', target: int) -> 'TreeNode':
        if not node:
            return None
        if node.val == target:
            return node
        left_node = set_target_node(node.left, target)
        right_node = set_target_node(node.right, target)
        if left_node and right_node:
            return node
        if left_node:
            return left_node
        return right_node

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")
    root = set_node(flds[0].split(","), 0, 0)
    p = set_target_node(root, int(flds[1]))
    q = set_target_node(root, int(flds[2]))

    ol = output_TreeNode()
    print("root = \n%s" %(ol.output(root)))
    print("root = %s\n" %ol.tree2str(root))
    print("p = %s, q = %s" %(ol.tree2str(p), ol.tree2str(q)))

    time0 = time.time()

    sl = Solution()
    result = sl.lowestCommonAncestor(root, p, q)

    time1 = time.time()
    print("result = \n%s" %ol.output(result))
    print("result = %s\n" %ol.tree2str(result))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
