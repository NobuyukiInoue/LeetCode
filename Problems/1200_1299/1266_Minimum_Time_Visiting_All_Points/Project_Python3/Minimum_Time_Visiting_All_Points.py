# coding: utf-8

import os
import sys
import time

import collections

class Solution:
#   def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    def minTimeToVisitAllPoints(self, points):
        # 56ms
        return sum(max(abs(points[i-1][0] - points[i][0]), abs(points[i-1][1] - points[i][1])) for i in range(1, len(points)))

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    points = [[int(col) for col in data.split(",")] for data in flds]
    print("points = {0}".format(points))

    time0 = time.time()

    sl = Solution()
    result = sl.minTimeToVisitAllPoints(points)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
