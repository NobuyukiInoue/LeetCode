# coding: utf-8

import copy
import os
import sys
import time

class Solution:
#   def minimumTotal(self, triangle: List[List[int]]) -> int:
    def minimumTotal(self, triangle):
        # 64ms
        if not triangle:
            return 
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])

    def minimumTotal_bad(self, triangle):
        total, index = triangle[0][0], 0
        for i in range(1, len(triangle)):
            if triangle[i][index] < triangle[i][index + 1]:
                total += triangle[i][index]
                index = index
            else:
                total += triangle[i][index + 1]
                index = index + 1
        return total

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

    triangle = [[] for i in range(len(flds))]

    for i in range(len(flds)):
        line = flds[i].split(",")
        for j in range(len(line)):
            triangle[i].append(int(line[j]))
        print("triangle[{0:d}] = {1}".format(i, triangle[i]))

    sl = Solution()
    time0 = time.time()
    result = sl.minimumTotal(triangle)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
