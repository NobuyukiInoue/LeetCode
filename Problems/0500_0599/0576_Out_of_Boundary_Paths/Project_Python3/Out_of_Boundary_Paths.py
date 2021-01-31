# coding: utf-8

import os
import sys
import time
import numpy
from typing import List, Dict, Tuple

class Solution:
    def findPaths(self, m, n, N, i, j):
        # 104ms
        paths = numpy.zeros((m, n), dtype = numpy.int64)
        paths[i][j] = 1
        out = 0
        mod = 10**9 + 7
        for _ in range(N):
            prev = paths % mod
            paths = prev - prev
            paths[1:] += prev[:-1]
            paths[:-1] += prev[1:]
            paths[:,1:] += prev[:,:-1]
            paths[:,:-1] += prev[:,1:]
            out += 4 * prev.sum() - paths.sum()
        return int(out % mod)

    def findPaths3(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # 148ms
        return reduce(lambda M, _:
              [[(x == 0 or M[x - 1][y]) + (x + 1 == m or M[x + 1][y])
              + (y == 0 or M[x][y - 1]) + (y + 1 == n or M[x][y + 1])
              for y in range(n)] for x in range(m)], range(N),
              [[0 for x in range(n)] for y in range(m)])[i][j] % (10 ** 9 + 7)

    def findPaths4(self, m: int, n: int, N: int, x: int, y: int) -> int:
        # 160ms
        return reduce(lambda M, _:
              [[(x == 0 or M[x - 1][y]) + (x + 1 == m or M[x + 1][y])
              + (y == 0 or M[x][y - 1]) + (y + 1 == n or M[x][y + 1])
              for y in range(n)] for x in range(m)], range(N),
              [[0 for x in range(n)] for y in range(m)])[i][j] % (10 ** 9 + 7)

    def findPaths5(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # 464ms
        MOD = 10**9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[i][j] = 1
        ans = 0
        for time in range(N):
            cur = nxt
            nxt = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD
        return ans

    def findPaths6(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # Time Limit Exceeded.
        self.res = 0
        def dfs(i, j, hopCount): 
            if i < 0 or m <= i:
                if hopCount <= N:
                    self.res += 1
                return
            if j < 0 or n <= j:
                if hopCount <= N:
                    self.res += 1
                return
            if hopCount + 1 > N:
                return
            dfs(i - 1, j, hopCount + 1)
            dfs(i + 1, j, hopCount + 1)
            dfs(i, j - 1, hopCount + 1)
            dfs(i, j + 1, hopCount + 1)
        dfs(i, j, 0)
        return self.res

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")
    m, n, N, i, j = int(flds[0]), int(flds[1]), int(flds[2]), int(flds[3]), int(flds[4])
    print("m = {0:d}, n = {1:d}, N = {2:d}, i = {3:d}, j = {4:d}".format(m, n, N, i, j))

    sl = Solution()

    time0 = time.time()

    result = sl.findPaths(m, n, N, i, j)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
