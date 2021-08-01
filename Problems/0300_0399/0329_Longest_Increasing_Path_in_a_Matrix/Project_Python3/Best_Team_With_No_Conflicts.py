# coding: utf-8

import bisect
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 516ms
        def dfs(i, j):
            if not dp[i][j]:
                dp[i][j] = 1 + max((dfs(x, y) for x, y in ((i - 1, j),(i + 1, j),(i, j - 1), (i, j + 1)) if 0  <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]),default = 0)
            return dp[i][j]
        m, n, = len(matrix), len(matrix and matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max((dfs(i, j) for i in range(m) for j in range(n)),default = 0)

    def longestIncreasingPath2(self, matrix: List[List[int]]) -> int:
        # 504ms
        def length(z):
            if z not in memo:
                memo[z] = 1 + max([length(Z)
                                   for Z in [z+1, z-1, z+1j, z-1j]
                                   if Z in matrix and matrix[z] > matrix[Z]]
                                  or [0])
            return memo[z]
        memo = {}
        matrix = {i + j*1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        return max(map(length, matrix), default = 0)

    def longestIncreasingPath3(self, matrix: List[List[int]]) -> int:
        # 480ms
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dirs = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
            for x, y in dirs:
                if 0 <= x < n and 0 <= y < m:
                    if matrix[x][y] > matrix[i][j]:
                        dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]
        
        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res

    def longestIncreasingPath4(self, matrix: List[List[int]]) -> int:
        # Time Limit Exceeded.
        self.max_count = 0
        check = [[False for col in row] for row in matrix]

        def dfs(check: List[List[int]], i:int, j:int, v:int, count:int):
            if i < 0 or i >= len(matrix):
                return
            if j < 0 or j >= len(matrix[i]):
                return
            if check[i][j]:
                return
            if matrix[i][j] <= v:
                return
            check[i][j] = True
            self.max_count = max(self.max_count, count + 1)
            dfs(check, i - 1, j, matrix[i][j], count + 1)
            dfs(check, i + 1, j, matrix[i][j], count + 1)
            dfs(check, i, j - 1, matrix[i][j], count + 1)
            dfs(check, i, j + 1, matrix[i][j], count + 1)
            check[i][j] = False
            return

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dfs(check, i, j, -1, 0)
        return self.max_count

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

    matrix = [[int(n) for n in fld.split(",")] for fld in flds]
    print("matrix = {0}".format(matrix))

    sl = Solution()

    time0 = time.time()

    result = sl.longestIncreasingPath(matrix)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
