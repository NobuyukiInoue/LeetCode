# coding: utf-8

import os
import sys
import time

class Solution:
#   def countServers(self, grid: List[List[int]]) -> int:
    def countServers(self, grid):
        # 504ms
        x, y = tuple(map(sum, grid)), tuple(map(sum, zip(*grid)))
        return sum(x[i] + y[j] > 2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])

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
    result = sl.countServers(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
