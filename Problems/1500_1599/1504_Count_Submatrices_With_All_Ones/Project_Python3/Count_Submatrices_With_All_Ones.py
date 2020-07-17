# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def numSubmat(self, mat: List[List[int]]) -> int:
    def numSubmat(self, mat):
        # 524ms
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(1, cols):
                if mat[r][c]:
                    if c > 0:
                        mat[r][c] = mat[r][c - 1] + 1

        submatrices = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]:
                    row = r
                    min_value = mat[r][c]
                    while row < rows and mat[row][c]:
                        min_value = min(min_value, mat[row][c])
                        submatrices += min_value
                        row += 1
        return submatrices

    def numSubmat2(self, mat):
        # 1008ms
        m, n = len(mat), len(mat[0])
        count = 0
        for left in range(n):
            row_sums = [0 for _ in range(m)]
            for right in range(left, n):
                consec_count = 0
                width = right - left + 1
                for bottom in range(m):
                    row_sums[bottom] += mat[bottom][right]
                    if row_sums[bottom] != width:
                        consec_count = 0
                    else:
                        consec_count += 1
                        count += consec_count
        return count

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
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

def printResult(title, result):
    print("{0} = [".format(title))
    for i in range(len(result)):
        print(result[i])
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

    mat = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("mat", mat)
  
    sl = Solution()
    time0 = time.time()

    result = sl.numSubmat(mat)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
