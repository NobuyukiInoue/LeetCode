# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 1124ms
        def check2dPeak(low, high, arr):
            mid = low + (high - low) // 2
            col_max = 0
            for i in range(len(arr)):
                if arr[i][mid] > col_max:
                    col_max = arr[i][mid]
                    row = i
                    col = mid
            if arr[row][col] < arr[row][col - 1]:
                return check2dPeak(low, col, arr)
            elif col + 1 < len(arr[row]) and arr[row][col] < arr[row][col + 1]:
                return check2dPeak(col, high, arr)
            else:
                return [row, col]
        return check2dPeak(0, len(mat[0]), mat)

    def findPeakGrid2(self, mat: List[List[int]]) -> List[int]:
        # 1156ms
        m, n = len(mat), len(mat[0])
        i = j = 0
        def check(i: int, j: int, no: int):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            if mat[i][j] <= no:
                return 2
            else:
                return 0
        while i < m:
            while j < n:
                if check(i + 1, j, mat[i][j]) != 0 and check(i, j + 1, mat[i][j]) != 0 and check(i - 1, j, mat[i][j]) != 0 and check(i, j + 1, mat[i][j]) != 0:
                    return [i, j]
                if check(i + 1, j, mat[i][j]) == 0:
                    i += 1
                elif check(i, j + 1, mat[i][j]) == 0:
                    j += 1
                elif check(i - 1, j, mat[i][j]) == 0:
                    i -= 1
                elif check(i, j - 1, mat[i][j]) == 0:
                    j -= 1

    def findPeakGrid3(self, mat: List[List[int]]) -> List[int]:
        # 1340ms
        if mat is None or mat[0] is None:
            return 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                neighbors = []
                if i > 0:
                    neighbors.append(mat[i - 1][j])
                if i < m - 1:
                    neighbors.append(mat[i + 1][j])
                if j > 0:
                    neighbors.append(mat[i][j - 1])
                if j < n - 1:
                    neighbors.append(mat[i][j + 1])
                if mat[i][j] > max(neighbors):
                    return [i, j]
        return [-1, -1]

def printGrid(title, grid):
    print("{0} = [".format(title))
    for i in range(len(grid)):
        if i == 0:
            print(" [", end = "")
        else:
            print(",[", end = "")
        for j in range(len(grid[i])):
            if j == 0:
                print("{0:3d}".format(grid[i][j]), end = "")
            else:
                print(",{0:3d}".format(grid[i][j]), end = "")
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

    result = sl.findPeakGrid(mat)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
