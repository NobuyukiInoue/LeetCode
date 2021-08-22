# coding: utf-8

import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # 1768ms
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        que = [start]
        visited = set()
        while que:
            node = que.pop()
            if node in visited:
                continue
            if node == end:
                return True
            visited.add(node)
            for i in graph[node]:
                que.append(i)
        return False

    def validPath2(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # 2296ms
        def cyclic(graph: List[int], node: int, visited: List[int]):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    cyclic(graph, child, visited)
        graph = {}
        visited = set()
        for i in range(n):
            graph[i] = []
        for u ,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if start not in visited and end not in visited:
                cyclic(graph, i, visited)
            elif start in visited and end in visited:
                return True
            elif start in visited and end not in visited:
                return False
            elif start not in visited and end in visited:
                return False
        return True

    def validPath_bad(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        if not edges:
            return False
        dic = {}
        for edge in edges:
            if not edge[0] in dic:
                dic[edge[0]] = [edge[1]]
            else:
                dic[edge[0]].append(edge[1])
        print(dic)
        def helper(start: int, end: int) -> bool:
            if start == end:
                return True
            if start in dic:
                for num in dic[start]:
                    if num == end:
                        return True
                    if helper(num, end):
                        return True
            return False
        return helper(start, end)

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
    flds = temp.replace(" ","").replace("\"","").rstrip().split("],[[")

    n = int(flds[0].replace("[", ""))
    flds1 = flds[1].split("]],[")
    if len(flds1[0]) == 0:
        edges = []
    else:
        edges = [[int(col) for col in data.split(",")] for data in flds1[0].replace("[[", "").split("],[")]
    flds2 = flds1[1].replace("]]", "").split("],[")
    start, end = int(flds2[0]), int(flds2[1])
    print("n = {0:d}, edges = {1}, start = {2:d}, end = {3:d}".format(n, edges, start, end))

    sl = Solution()
    time0 = time.time()

    result = sl.validPath(n, edges, start, end)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
