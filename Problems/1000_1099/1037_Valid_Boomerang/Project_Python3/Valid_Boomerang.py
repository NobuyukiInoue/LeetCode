# coding: utf-8

import os
import sys
import time

class Solution:
#   def isBoomerang(self, points: List[List[int]]) -> bool:
    def isBoomerang(self, points):
        return (points[0][0] - points[1][0]) * (points[0][1] - points[2][1]) != (points[0][0] - points[2][0]) * (points[0][1] - points[1][1])

    def isBoomerang2(self, points):
        X, Y, Z = points
        x1, y1 = X
        x2, y2 = Y
        x3, y3 = Z
        return (X != Y or Y != Z or X != Z) and (y2 - y1)*(x3 - x2) != (y3 - y2)*(x2 - x1)

    def isBoomerang_work(self, points):
        sloop = [0.0] * len(points)
        for i in range(len(points)):
            sloop[i] = points[i][1] / points[i][0]
        for i in range(0, len(sloop) - 1):
            if sloop[i] != sloop[i + 1]:
                return True
        return False

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
    print("points = %s" %points)

    time0 = time.time()

    sl = Solution()
    result = sl.isBoomerang(points)

    time1 = time.time()

    print("result = %s" %result)
    print("Execute time ... : %f[s]\n" %(time1 - time0))

if __name__ == "__main__":
    main()
