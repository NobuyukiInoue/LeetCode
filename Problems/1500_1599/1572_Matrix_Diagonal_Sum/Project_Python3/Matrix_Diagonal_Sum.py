# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def diagonalSum(self, mat: List[List[int]]) -> int:
    def diagonalSum(self, mat):
        # 108ms
        total, len_mat = 0, len(mat)
        for i, _ in enumerate(mat):
            total += mat[i][i] + mat[len_mat - 1 - i][i]
        return total if len_mat % 2 == 0 else total - mat[len_mat//2][len_mat//2]

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

    result = sl.diagonalSum(mat)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
