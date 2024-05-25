import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        # 39ms - 41ms
        def isPossible(i: int, j: int) -> bool:
            cnt_w, cnt_b = 0, 0
            for x in range(i, i + 2):
                for y in range(j, j + 2):
                    if grid[x][y] == 'W':
                        cnt_w += 1
                    else:
                        cnt_b += 1
            if cnt_w > 2 or cnt_b > 2:
                return True
            return False

        for i in range(2):
            for j in range(2):
                if isPossible(i, j):
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
                print(",{0}".format(grid[i][j]), end = "")
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

    result = sl.canMakeSquare(grid)

    time1 = time.time()

    print("result = {0}\n".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
