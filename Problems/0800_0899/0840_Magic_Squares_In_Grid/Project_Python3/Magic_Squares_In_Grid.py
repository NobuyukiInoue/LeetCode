# coding: utf-8

import os
import sys
import time

class Solution:
#    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    def numMagicSquaresInside(self, grid):
        def isMagic(i, j):
            s = "".join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    grid = [0]*len(flds)
    for i in range(len(flds)):
        pt = flds[i].split(",")
        grid[i] = [0]*len(pt)
        for j in range(len(pt)):
            grid[i][j] = int(pt[j])
    
    print("grid = %s" %grid)

    time0 = time.time()

    sl = Solution()
    result = sl.numMagicSquaresInside(grid)
    print("result = %d" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
