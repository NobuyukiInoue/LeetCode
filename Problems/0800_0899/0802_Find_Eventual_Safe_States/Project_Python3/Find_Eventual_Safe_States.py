# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 737ms
        memo = [None]*len(graph)

        def canJump(node: int) -> bool:
            if memo[node] is not None:
                return memo[node]
            memo[node] = False
            for child in graph[node]:
                if not canJump(child):
                    return False
            memo[node] = True
            return memo[node]

        result = []
        for i, _ in enumerate(graph):
            if canJump(i):
                result.append(i)
        return result

    def eventualSafeNodes2(self, graph: List[List[int]]) -> List[int]:
        # 658ms
        self.safe_sites = [None for _ in range(len(graph))]
        ans = []
        
        def dfs(site):
            if self.safe_sites[site] != None:
                if self.safe_sites[site] == -1:
                    self.safe_sites[site] = 0
                return self.safe_sites[site]
            if not graph[site]:
                self.safe_sites[site] = 1
                return 1
            self.safe_sites[site] = -1
            for pos in graph[site]:
                if dfs(pos) == 0:
                    self.safe_sites[site] = 0
                    return 0
            self.safe_sites[site] = 1
            return 1
        
        for ind in range(len(graph)):
            if dfs(ind):
                ans.append(ind)
        return ans

    def eventualSafeNodes3(self, graph: List[List[int]]) -> List[int]:
        # 820ms
        n = len(graph)
        visited = [False]*n
        recStack = [False]*n
        nodeInCycle = [False]*n
        res = []
        for i, n in enumerate(graph):
            if not visited[i]:
                self.checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, i, n)
        for i, n in enumerate(graph):
            if not nodeInCycle[i]:
                res.append(i)
        return res

    def checkIfNodeIsSafe(self, graph: List[List[int]], nodeInCycle: List[bool], visited: List[bool], recStack: List[bool], i: int, n: int) -> bool:
        if recStack[i]:
            nodeInCycle[i] = True
            return False
        if visited[i]:
            return True
        visited[i] = True
        recStack[i] = True
        for j in  graph[i]:
            if not self.checkIfNodeIsSafe(graph, nodeInCycle, visited, recStack, j, n):
                nodeInCycle[i] = True
                return False
        nodeInCycle[i] = False
        recStack[i] = False
        return True

    def eventualSafeNodes4(self, graph: List[List[int]]) -> List[int]:
        # 950m
        seen, safe = set(), set()
        def dfs(u, path):
            if u in seen: return u in safe
            seen.add(u)
            if all(dfs(v, path|{v}) for v in graph[u]):
                safe.add(u)
                return True
        return list(filter(lambda u: dfs(u, {u}), range(len(graph))))

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:3d}".format(grid[i][j]), end = "")
            else:
                print(",{0:3d}".format(grid[i][j]), end = "")
        print("]")
    print("]")

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
    print("]")

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

#   graph = [[int(col) if col != "" for col in data.split(",")] for data in flds.split("],[")]
    graph = []
    for data in flds.split("],["):
        row = []
        for col in data.split(","):
            if col != "":
                row.append(int(col))
        graph.append(row)
    print("graph = {0}".format(graph))
  
    sl = Solution()
    time0 = time.time()

    result = sl.eventualSafeNodes(graph)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
