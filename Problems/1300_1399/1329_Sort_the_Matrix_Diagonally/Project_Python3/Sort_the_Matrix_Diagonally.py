import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # 62ms - 73ms
        m, n = len(mat), len(mat[0])
        for c in range(n - 1):
            d = sorted(mat[i][c + i] for i in range(min(n - c, m)))
            for i in range(len(d)):
                mat[i][c + i] = d[i]
        for r in range(1, m - 1):
            d = sorted(mat[r + i][i] for i in range(min(n, m - r)))
            for i in range(len(d)):
                mat[r + i][i] = d[i]
        return mat

    def diagonalSort2(self, mat: List[List[int]]) -> List[List[int]]:
        # 71ms - 77ms
        d = {}
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if i - j in d:
                    d[i - j].append(mat[i][j])
                else:
                    d[i - j] = [mat[i][j]]
        for k in d.keys():
            d[k].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop(0)
        return mat

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i, _ in enumerate(grid):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:2d}".format(grid[i][j]), end = "")
            else:
                print(",{0:2d}".format(grid[i][j]), end = "")
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

    mat = [[int(col) for col in row.split(",")] for row in flds.split("],[")]
    printGrid("mat", mat)

    sl = Solution()
    time0 = time.time()

    result = sl.diagonalSort(mat)

    time1 = time.time()

    printGrid("result", result)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
