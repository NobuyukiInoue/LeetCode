# coding: utf-8

import collections
import os
import sys
import time

class Solution:
#   def maxDistance(self, grid: List[List[int]]) -> int:
    def maxDistance(self, grid):
        # 560ms
        m,n = len(grid), len(grid[0])
        q = collections.deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        if len(q) == m*n or len(q) == 0:
                return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x + i, y + j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1
        return level - 1

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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()

    grid_str = flds.split("],[")
    grid = [[int(col) for col in data.split(",")] for data in grid_str]
    print("grid = {0}".format(grid))

    time0 = time.time()

    sl = Solution()
    result = sl.maxDistance(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
