# coding: utf-8

import collections
import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 432ms
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        
        def minD(distances, arrived):
            max_arrival_time = sys.maxsize
            min_index = -1
            for v in range(1, n + 1):
                if distances[v] < max_arrival_time and arrived[v] == False:
                    max_arrival_time = distances[v]
                    min_index = v
            return min_index
        
        self.distances = [sys.maxsize]*(n + 1)
        def start(src):
            self.distances[src] = 0
            arrived = [False]*(n + 1)
            for _ in range(n):
                u = minD(self.distances, arrived)
                arrived[u] = True
                for v in range(1, n + 1):
                    if v in graph[u] and arrived[v] == False and self.distances[v] > self.distances[u] + graph[u][v]:
                        self.distances[v] = self.distances[u] + graph[u][v]

        start(k)
        return -1 if sys.maxsize in self.distances[1:] else max(self.distances[1:])  

    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        # 496ms
        graph,ans = collections.defaultdict(dict), 0
        for u, v, t in times:
            graph[u][v] = t
        bfs, visited=[(0, k)], set()
        while bfs:
            t, node = heapq.heappop(bfs)
            if node not in visited:
                ans = t
                visited.add(node)
                for next_node in graph[node]:
                    heapq.heappush(bfs,(t + graph[node][next_node], next_node))
        return ans if len(visited) == n else -1

    def networkDelayTime3(self, times: List[List[int]], n: int, k: int) -> int:
        # 616ms
        q, t, adj = [(0, k)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(t.values()) if len(t) == n else -1

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
    flds = temp.replace("\"", "").replace(" ", "").rstrip().split("]],[")
    times = [[int(cols) for cols in flds0.split(",")] for flds0 in flds[0].replace("[[[", "").split("],[")]
    flds1 = flds[1].split("],[")
    n, k = int(flds1[0]), int(flds1[1].replace("]]", ""))
    print("times = {0}, n = {1:d}, k = {2:d}".format(times, n, k))

    sl = Solution()

    time0 = time.time()

    result = sl.networkDelayTime(times, n, k)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
