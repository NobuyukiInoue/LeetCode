# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target):
        # 60ms
        if not matrix or not matrix[0]:
            return False
        if matrix[0] == target:
            return True
        matrixLen = len(matrix)
        if len(matrix[0]) == 0:
            for i in range(matrixLen):
                if matrix[i] == target:
                    return True
                if matrix[i] > target:
                    return False
        if matrix[0][0] == target:
            return True
        i = 0
        while i < matrixLen:
            if i + 1 < matrixLen:
                if matrix[i + 1][0] == target:
                    return True
                if matrix[i + 1][0] < target:
                    i += 1
                    continue
            if matrix[i][0] == target:
                return True
            if matrix[i][0] < target:
                for j in range(1, len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
                    if matrix[i][j] > target:
                        return False
            return False
        return False

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip().split("]],[")

    if len(flds[0]) > 0:
        matrix = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
        printGrid("matrix", matrix)
    else:
        matrix = [[]]
        printGrid("matrix", matrix)

    target = int(flds[1].replace("]]", ""))
    print("target = {0:d}".format(target))

    sl = Solution()
    time0 = time.time()

    result = sl.searchMatrix(matrix, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
