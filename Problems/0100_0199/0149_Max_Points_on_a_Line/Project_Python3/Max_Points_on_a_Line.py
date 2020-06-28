# coding: utf-8

import os
import sys
import time
import math

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points) - 1):
            cur = 0
            overlap = 0
            lines = {}
            # y = a x + b
            for j in range(i + 1,len(points)):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                if dx == dy == 0:
                    overlap += 1
                    continue
                key = None if dx == 0 else 10.0 * dy / dx
                lines[key] = lines.get(key, 0) + 1
                cur = max(cur, lines[key])
            res = max(res, cur + overlap)
        return res + 1

def set_Points(flds):
    p = [Point()]*len(flds)
    for i in range(len(flds)):
        tempStr = flds[i].split(",")
        p[i] = Point(int(tempStr[0]), int(tempStr[1]))
    return p


def output_Points(p):
    if len(p) == 0:
        return ""
    result = "[[" + str(p[0].x) + "," + str(p[0].y) + "]"
    for i in range(1,len(p)):
        result += ",[" + str(p[i].x) + "," + str(p[i].y) + "]"
    return result

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
    flds = temp.replace("[[","").replace("]]","").rstrip().split("],[")
    p = set_Points(flds)
    print("p = {0}".format(output_Points(p)))

    sl = Solution()
    time0 = time.time()
    result = sl.maxPoints(p)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
