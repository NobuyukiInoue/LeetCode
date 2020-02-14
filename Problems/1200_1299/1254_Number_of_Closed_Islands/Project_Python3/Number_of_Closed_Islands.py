# coding: utf-8

import os
import sys
import time

class Solution:
#   def closedIsland(self, grid: List[List[int]]) -> int:
    def closedIsland(self, grid):
        # 136ms
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j, val):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = val
                dfs(i, j+1, val)
                dfs(i+1, j, val)
                dfs(i-1, j, val)
                dfs(i, j-1, val)
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j, 1)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 1)
                    res += 1
        return res

    def closedIsland2(self, grid):
        # 144ms
        def helper(x, y):
            if not (0 <= x < n and 0 <= y < m):
                return False
            if grid[x][y] == 1 or (x, y) in visited:
                return True
            visited.add((x, y))
            return all([helper(x + 1, y), helper(x - 1, y), helper(x, y + 1), helper(x, y - 1)])

        n = len(grid)
        m = len(grid[0])
        visited = set()
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if helper(i, j):
                        res += 1
        return res


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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("grid = {0}".format(grid))

    time0 = time.time()

    sl = Solution()
    result = sl.closedIsland(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
