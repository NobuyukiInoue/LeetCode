# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix):
        # 140ms
        """
        Do not return anything, modify matrix in-place instead.
        """
        t_row, t_col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in t_row:
                        t_row.append(i)
                    if j not in t_col:
                        t_col.append(j)
        for i in range(len(matrix)):
            if i in t_row:
                matrix[i] = [0 for col in range(len(matrix[0]))]
            #   matrix[i] = [0]*len(matrix[0])
            else:
                for j in range(len(matrix[0])):
                    if j in t_col:
                        matrix[i][j] = 0

    def setZeroes2(self, matrix):
        # 132ms
        all_zero = [0] * len(matrix[0])
        zero_idx = list()
        not_zero = list()
		
        for i, m in enumerate(matrix):
            if 0 in m:
                for j, n in enumerate(m):
                    if not n and j not in zero_idx:
                        zero_idx.append(j)
                matrix[i] = all_zero
            else:
                not_zero.append(i)
		
        for n in not_zero:
            for i in zero_idx:
                matrix[n][i] = 0

    def setZeroes3(self, matrix):
        # 144ms
        row = [False for _ in range(len(matrix))]
        col = [False for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i],col[j] = True, True 

        for i in range(len(row)):
            if row[i]:
                for val in range(len(matrix[i])):
                    matrix[i][val] = 0

        for j in range(len(col)):
            if col[j]:
                for val in range(len(matrix)):
                    matrix[val][j] = 0

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
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

def loop_main(temp):
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip()

    matrix = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    printGrid("matrix", matrix)
  
    time0 = time.time()

    sl = Solution()
    sl.setZeroes(matrix)

    time1 = time.time()

    printGrid("result", matrix)
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
