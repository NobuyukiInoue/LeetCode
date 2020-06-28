# coding: utf-8

import bisect
import os
import sys
import time
import heapq

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 40ms
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        return any(target in row for row in matrix)

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 44ms
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False

    def searchMatrix_work(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        i, j = 0, 0
        while matrix[i][j] < target:
            if i < len(matrix) - 1:
                if matrix[i + 1][j] == target:
                    return True
                if j < len(matrix[i]) - 1:
                    if matrix[i][j + 1] == target:
                        return True
                    if matrix[i + 1][j] < target and matrix[i + 1][j] > matrix[i][j + 1]:
                        i += 1
                    else:
                        j += 1
                else:
                    i += 1
            else:
                if j < len(matrix[i]) - 1:
                    j += 1
                else:
                    return False
        if matrix[i][j] == target:
            return True
        return False

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
    flds = temp.split("]],[")
    flds[0] = flds[0].replace("[[[", "")
    if len(flds[0]) > 0:
        dataStr = flds[0].split("],[")
        matrix = [[int(n) for n in data.split(",") ] for data in dataStr]
    else:
        matrix = [[]]
    target = int(flds[1].replace("]", ""))

    print("matrix = [")
    for i in range(len(matrix)):
        if i == 0:
            print("  {0}".format(matrix[i]))
        else:
            print(", {0}".format(matrix[i]))
    print("]")
    print("target = {0:d}".format(target))

    sl = Solution()
    time0 = time.time()
    result = sl.searchMatrix(matrix, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
