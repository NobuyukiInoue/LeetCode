# coding: utf-8

import os
import sys
import time

class Solution:
#   def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    def shiftGrid(self, grid, k):
        n, m = len(grid), len(grid[0])
        newGrid = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):                                    
                i1 = ((i + k//m) + (j + k%m) // m) % n
                j1 = (j + k%m) % m  
                newGrid[i1][j1] = grid[i][j]
        return newGrid

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
    str_args = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip()
    flds = str_args.split("]],[")

    grid = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
    print("grid = {0}".format(grid))

    k = int(flds[1].replace("]",""))
    print("k = {0:d}".format(k))

    time0 = time.time()

    sl = Solution()
    result = sl.shiftGrid(grid, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
