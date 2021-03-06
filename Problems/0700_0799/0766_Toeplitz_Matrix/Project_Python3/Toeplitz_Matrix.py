# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    def isToeplitzMatrix(self, matrix):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    data0 = flds[0].split(",")
    matrix = [[0 for j in range(len(data0))] for i in range(len(flds))]

    for i in range(len(flds)):
        line = flds[i].split(",")
        for j in range(len(line)):
            matrix[i][j] = int(line[j])
        print("matrix[{0:d}] = {1}".format(i, matrix[i]))

    sl = Solution()
    time0 = time.time()

    result = sl.isToeplitzMatrix(matrix)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
