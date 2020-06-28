# coding: utf-8

import os
import sys
import time

class Solution:
#   def orangesRotting(self, grid: List[List[int]]) -> int:
    def orangesRotting(self, grid):
        def getNeighbor(x, y, v):
            neighbors = []
            if x > 0 and grid[x-1][y] == v:
                neighbors.append((x-1,y))
            if x < len(grid)-1 and grid[x+1][y] == v:
                neighbors.append((x+1,y))
            if y > 0 and grid[x][y-1] == v:
                neighbors.append((x,y-1))
            if y < len(grid[0])-1 and grid[x][y+1] == v:
                neighbors.append((x,y+1))
            return neighbors
        
        fresh_count, minutes, rottens = 0, 0, []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh_count += 1
                    neighbor_rotten = getNeighbor(r, c, 2)
                    if len(neighbor_rotten) > 0:
                        rottens.append((r,c))
                        grid[r][c] = 3 # previously fresh, not rotten
                        
        if fresh_count == 0:
            return 0
        
        while len(rottens) > 0:
            minutes += 1
            fresh_count -= len(rottens)
            next_rottens = []
            for x, y in rottens:
                for u, v in getNeighbor(x,y,1):
                    next_rottens.append((u, v))
                    grid[u][v] = 3
            rottens = next_rottens
                        
        return -1 if fresh_count > 0 else minutes

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    grid = [[int(col) for col in data.split(",")] for data in flds]
    print("grid = {0}".format(grid))

    sl = Solution()
    time0 = time.time()
    result = sl.orangesRotting(grid)
    print("result = {0:d}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
