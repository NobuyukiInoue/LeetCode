import collections
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # 1713ms - 1717ms
        m, n = len(grid), len(grid[0])
        ht, q = dict(), collections.deque()
        x = y = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] not in ht:
                    ht[grid[i][j]] = set()
                elif (i, j) not in ht[grid[i][j]]:
                    q.append((i, j))
                    while len(q) > 0:
                        x, y = q.popleft()
                        if (x, y) not in ht[grid[i][j]]:
                            ht[grid[i][j]].add((x, y))
                        elif len(ht[grid[i][j]]) > 2:
                            return True
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == grid[i][j]:
                                if (nx, ny) not in ht[grid[i][j]]:
                                    q.append((nx, ny))
        return False

    def containsCycle2(self, grid: List[List[str]]) -> bool:
        # 2130ms - 2202ms
        m, n = len(grid), len(grid[0])
        visited = set()

        def neighbors(i, j):
            return [(ni, nj) for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j]]

        def dfs(i, j, ch, prev, seen):
            if (i, j) in seen:
                return True
            seen.add((i, j))
            visited.add((i, j))
            for ni, nj in neighbors(i, j):
                if not prev or prev != (ni, nj):
                    if dfs(ni, nj, ch, (i, j), seen):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    seen = set()
                    if dfs(i, j, grid[i][j], None, seen):
                        return True
        return False

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0}".format(grid[i][j]), end = "")
            else:
                print(", {0}".format(grid[i][j]), end = "")
        print("]")
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

    grid = [[col for col in row.split(",")] for row in flds.split("],[")]
    printGrid("grid", grid)

    sl = Solution()
    time0 = time.time()

    result = sl.containsCycle(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
