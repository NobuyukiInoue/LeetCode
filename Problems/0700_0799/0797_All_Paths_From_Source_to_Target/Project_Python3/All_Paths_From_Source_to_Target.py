# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        # 92ms
        dest_index = len(graph) - 1
        path = []
        dfs_stack = [(0, [0])]
        while dfs_stack:
            cur_node_index, tracking = dfs_stack.pop()
            for neighbor_index in graph[cur_node_index]:
                if neighbor_index == dest_index:
                    path.append(tracking + [neighbor_index])
                else:
                    dfs_stack.append((neighbor_index, tracking + [neighbor_index] ))
        return path

    def allPathsSourceTarget2(self, graph: [[int]]) -> [[int]]:
        # 104ms
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res

    def allPathsSourceTarget_work(self, graph: [[int]]) -> [[int]]:
        nodes = []
        for i, _ in enumerate(graph):
            print(graph[i])
            if len(graph[i]) > 0:
                for dist in graph[i]:
                    nodes.append([i, dist])
        print(nodes)
        ans = []
        for i in range(len(nodes) - 1):
            if nodes[i][0] == 0:
                for j in range(i + 1, len(nodes)):
                    if nodes[j][0] == nodes[i][1]:
                        temp = nodes[i].copy()
                        temp.append(nodes[j][1])
                        ans.append(temp)
        return ans

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")
    graph = []
    for i, _ in enumerate(flds):
        if len(flds[i]) == 0:
            graph.append([])
        else:
            graph.append([int(num) for num in flds[i].split(",")])
    print("graph = {0}".format(graph))

    sl = Solution()
    time0 = time.time()

    result = sl.allPathsSourceTarget(graph)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
