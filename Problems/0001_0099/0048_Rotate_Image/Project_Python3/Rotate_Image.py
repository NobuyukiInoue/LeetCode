# coding: utf-8

import os
import sys
import time

class Solution:
#   def rotate(self, matrix: List[List[int]]) -> None:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 32ms
        n = len(matrix)
        for l in range(n // 2):
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache

"""
Top to Right
[0][0]      [0][n-1]
[0][1]      [1][n-1]
[0][2]      [2][n-1]
...
[0][n-1]    [n-1][n-1]

Right to Bottom
[0][n-1]    [n-1][n-1]
[1][n-1]    [n-1][n-1-1]
[2][n-1]    [n-1][n-1-2]
...
[n-1][n-1]    [n-1][0]

Bottom to Left
[n-1][n-1]  [0][0]
[n-1][n-1-1]    [1][0]
[n-1][n-1-2]    [2][0]
...
[n-1][0]    [n-1][0]
"""


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

    matrix = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("matrix = {0}".format(matrix))

    sl = Solution()
    time0 = time.time()

    sl.rotate(matrix)

    time1 = time.time()

    print("result = {0}".format(matrix))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
