# coding: utf-8

import os
import operator
import sys
import time

class Solution:
#   def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def kthSmallest(self, matrix, k):
        # 172ms
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo <= hi:
            mid = lo + (hi-lo)//2
            count = self.getLessEqual(matrix, mid)
            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def getLessEqual(self, matrix, val):
        res = 0
        n = len(matrix)
        i, j = n-1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > val:
                i -= 1
            else:
                res += i + 1
                j += 1
        return res

    def kthSmallest2(self, matrix, k):
        # 180ms
        m, n = len(matrix), len(matrix[0])
        data = []
        for i in range(m):
            for j in range(n):
                data.append(matrix[i][j])
        data.sort()
        return data[k - 1]

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
    flds = temp.replace(" ","").replace("\"","").replace("[[[","").rstrip().split("]],[")

    if len(flds[0]) > 0:
        matrix = [[int(col) for col in data.split(",")] for data in flds[0].split("],[")]
        printGrid("matrix", matrix)
    else:
        matrix = [[]]
        printGrid("matrix", matrix)

    k = int(flds[1].replace("]]", ""))
    print("k = {0:d}".format(k))

    time0 = time.time()

    sl = Solution()
    result = sl.kthSmallest(matrix, k)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
