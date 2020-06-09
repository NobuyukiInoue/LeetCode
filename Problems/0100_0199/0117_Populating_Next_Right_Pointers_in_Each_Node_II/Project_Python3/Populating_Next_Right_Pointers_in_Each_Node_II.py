# coding: utf-8

import os
import sys
import time

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 52ms
        node = root
        tail = dummy = Node(0)
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
        return root

    def connect2(self, root: 'Node') -> 'Node':
        # 64ms
        if root == None:
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
        if node.left != None:
            self.get_node(node.left, level + 1)
        if node.right != None:
            self.get_node(node.right, level + 1)

    def set_next(self, node, level):
        if len(self.levels[level]) > self.pos[level] + 1:
            node.next = self.levels[level][self.pos[level] + 1]
            self.pos[level] += 1
        else:
            node.next = None
        if node.left != None:
            self.set_next(node.left, level + 1)
        if node.right != None:
            self.set_next(node.right, level + 1)

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

    def output_with_next(self, node):
        self.resultStr = []
        self.output_TreeNode_with_next(node, 0)
        return self.print_resultStr()

    def output_TreeNode_with_next(self, node, n):
        if node == None:
            return
        if len(self.resultStr) <= n:
            self.resultStr.append("(" + str(node.val) + ")")
        else:
            self.resultStr[n] += ",(" + str(node.val) + ")"
        if node.next == None:
            self.resultStr[n] += ",(#)"
        if node.left != None:
            self.output_TreeNode_with_next(node.left, n + 1)
        if node.right != None:
            self.output_TreeNode_with_next(node.right, n + 1)
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

    node = Node(int(flds[cur_pos + pos]))
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

    time0 = time.time()

    sl = Solution()
    result = sl.connect(root)

    time1 = time.time()

    print("result = \n%s" %(ol.output_with_next(result)))
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
