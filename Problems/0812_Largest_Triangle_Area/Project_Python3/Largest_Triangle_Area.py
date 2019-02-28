# coding: utf-8

import os
import sys
import time

class Solution:

#    def largestTriangleArea(self, points: List[List[int]]) -> float:
    def largestTriangleArea(self, points):
        area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    x3 = points[k][0]
                    y3 = points[k][1]
                    temparea = x1 * (y2- y3) - y1 * (x2 - x3) + (x2 * y3 - x3 * y2)
                    area = max(area, abs(temparea))
        return area / 2.0

    def largestTriangleArea3(self, points):
        def calcArea(x, y, z):
            return 0.5*abs(x[0]*y[1] + y[0]*z[1] + z[0]*x[1] - y[0]*x[1] - z[0]*y[1] - x[0]*z[1])
        maxA = A = i = 0
        while i < len(points):
            j = i+1 
            k = j+1
            while j < k:
                k = j+1
                while k < len(points):
                    A = calcArea(points[i], points[j], points[k])
                    maxA = max(maxA, A)
                    k += 1
                j += 1
            i += 1
        return maxA

def main():
    argv = sys.argv
    argc = len(argv)

    if (argc < 2):
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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    points = [[]*2]*len(flds)
    for i in range(len(flds)):
        pt = flds[i].split(",")
        points[i] = [int(pt[0]), int(pt[1])]

    print("points[] = %s" %points)

    time0 = time.time()

    sl = Solution()
    result = sl.largestTriangleArea(points)
    print("result = %s" %result)

    time1 = time.time()

    print("Execute time ... : %f[s]" %(time1 - time0))
    print()

if __name__ == "__main__":
    main()
