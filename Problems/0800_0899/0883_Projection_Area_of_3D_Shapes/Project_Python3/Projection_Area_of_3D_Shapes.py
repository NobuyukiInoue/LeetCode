# coding: utf-8

import os
import sys
import time

class Solution:
#   def projectionArea(self, grid: List[List[int]]) -> int:
    def projectionArea(self, grid):
        # 40ms
        return (sum(map(lambda L: sum([1 if elem > 0 else 0 for elem in L]), grid)) + #xy plane - number of points that aren't 0
                sum(map(lambda L: max(L), grid)) + #xz max amongst y axis (max of each sublist)
                sum(map(lambda L: max(L), zip(*grid)))) #yz max amongst x axis (max of each sublbist of transposed grid)

    def projectionArea(self, grid):
        # 44ms
        return sum(max(grid[i]) + max(row[i] for row in grid) + sum(v != 0 for v in grid[i]) for i in range(len(grid)))

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    grid = [[int(col) for col in data.split(",")] for data in flds]
    print("grid = %s" %grid)

    time0 = time.time()

    sl = Solution()
    result = sl.projectionArea(grid)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
