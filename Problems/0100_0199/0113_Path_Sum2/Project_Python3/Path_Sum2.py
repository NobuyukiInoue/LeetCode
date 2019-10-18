# coding: utf-8

import copy
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
#   def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    def pathSum(self, root, sum):
        # 52ms
        results = []
        self.dfs(root, sum, [], results)
        return results

    def dfs(self, root, sum, tmp, results):
        if not root:
            return
        if root.left == None and root.right == None and sum == root.val:
            results.append(tmp+[root.val])
            return
        self.dfs(root.left, sum-root.val, tmp+[root.val], results)
        self.dfs(root.right, sum-root.val, tmp+[root.val], results)

    def pathSum_work(self, root, sum):
        # 384ms
        self.results = []
        if root == None or root.val == None:
            return None
        arr = []
        total = 0
        self.helper(root, arr, total, sum)
        return self.results

    def helper(self, node, arr, total, sum):
        if node.val == None:
            return
        arr.append(node.val)
        total += node.val
        if node.left == None and node.right == None:
            if total == sum:
                self.results.append(arr)
                return
        if node.left != None:
            self.helper(node.left, copy.deepcopy(arr), total, sum)
        if node.right != None:
            self.helper(node.right, copy.deepcopy(arr), total, sum)
        return

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    root = set_node(flds[0].split(","), 0, 0)
    sum = int(flds[1])

    ol = output_TreeNode()
    print("root = \n{0}".format(ol.output(root)))
    print("root = \n{0}".format(ol.tree2str(root)))
    print("sum = {0:d}".format(sum))

    time0 = time.time()

    sl = Solution()
    result = sl.pathSum(root, sum)

    time1 = time.time()
    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
