# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

from Node.Node import Node
from Node.OperateNode import OperateNode

class Solution:
    def cloneGraph_1liner(self, node: 'Node') -> 'Node':
        # 36ms
        return copy.deepcopy(node)

#   def cloneGraph_BFS(self, node: 'Node') -> 'Node':
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 40ms
        if not node:
            return
        nodes = {}
        source = Node(node.val)
        nodes[source.val] = source
        q = collections.deque([node])
        while q:
            u = q.popleft()
            for nei in u.neighbors:
                if nei.val not in nodes:
                    new_node = Node(nei.val)
                    nodes[nei.val] = new_node
                    q.append(nei)
                nodes[u.val].neighbors.append(nodes[nei.val])
        return source

    def cloneGraph_DFS(self, node: 'Node') -> 'Node':
        # 40ms
        def dfs(node):
            for nei in node.neighbors:
                if nei.val not in nodes:
                    new_node = Node(nei.val)
                    nodes[nei.val] = new_node
                    dfs(nei)
                nodes[node.val].neighbors.append(nodes[nei.val])
            
        if not node:
            return
        nodes = {}
        source = Node(node.val)
        nodes[source.val] = source
        dfs(node)
        return source

    def cloneGraph_DFS_iter(self, node):
        # 41ms
        if not node:
            return
        nodes = {}
        source = Node(node.val)
        nodes[source.val] = source
        stack = [node]
        while stack:
            u = stack.pop()
            for nei in u.neighbors:
                if nei.val not in nodes:
                    new_node = Node(nei.val)
                    nodes[nei.val] = new_node
                    stack.append(nei)
                nodes[u.val].neighbors.append(nodes[nei.val])
        return source

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

    ope_n = OperateNode()
    if flds == "":
        node = Node(None)
    elif flds == "[]":
        node = Node(None, None)
    else:
        data = [[int(col) for col in row.split(",")] for row in flds.split("],[")]
        node = ope_n.createNode(data)

    print("node = \n{0}".format(ope_n.nodeToString(node)))

    sl = Solution()
    time0 = time.time()

    result = sl.cloneGraph(node)

    time1 = time.time()

    print("result = \n{0}".format(ope_n.nodeToString(result)))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
