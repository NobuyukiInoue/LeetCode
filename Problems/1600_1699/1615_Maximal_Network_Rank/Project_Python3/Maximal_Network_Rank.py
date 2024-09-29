import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 261ms - 269ms
        connections = [0] * n
        graph = [[False] * n for _ in range(n)]
        for a, b in roads:
            connections[a] += 1
            connections[b] += 1
            graph[a][b] = graph[b][a] = True
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = connections[i] + connections[j]
                if graph[i][j]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank

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
    flds = temp.replace("]]]","").rstrip().split("],[[")
    n = int(flds[0].replace("[[", ""))
    roads = [[int(col) for col in row.split(",")] for row in flds[1].replace("]]", "").split("],[")]
    print("n = {0:d}, roads = {1}".format(n, roads))

    sl = Solution()
    time0 = time.time()

    result = sl.maximalNetworkRank(n, roads)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
