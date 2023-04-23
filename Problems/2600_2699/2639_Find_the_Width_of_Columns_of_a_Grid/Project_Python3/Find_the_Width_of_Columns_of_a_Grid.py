import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # 107ms - 111ms
        return [max(len(str(col)) for col in row) for row in zip(*grid)]
    
    def findColumnWidth_1liner2(self, grid: List[List[int]]) -> List[int]:
        # 106ms - 113ms
        return [max(map(len, map(str, row))) for row in zip(*grid)]

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:d}".format(grid[i][j]), end = "")
            else:
                print(",{0:d}".format(grid[i][j]), end = "")
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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    grid = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("grid", grid)

    sl = Solution()
    time0 = time.time()

    result = sl.findColumnWidth(grid)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
