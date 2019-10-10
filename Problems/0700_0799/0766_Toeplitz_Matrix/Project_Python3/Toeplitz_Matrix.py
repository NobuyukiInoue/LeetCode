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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")

    data0 = flds[0].split(",")
    matrix = [[0 for j in range(len(data0))] for i in range(len(flds))]

    for i in range(len(flds)):
        line = flds[i].split(",")
        for j in range(len(line)):
            matrix[i][j] = int(line[j])
        print("matrix[%d] = %s" %(i, matrix[i]))

    time0 = time.time()

    sl = Solution()
    result = sl.isToeplitzMatrix(matrix)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
