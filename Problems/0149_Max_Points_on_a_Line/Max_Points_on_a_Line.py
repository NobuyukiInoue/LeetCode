# coding: utf-8

import sys
import time


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
        return 0


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
    args = sys.argv
    argc = len(args)

    print("args[0] = %s %s" %(args[0], args[1]) )
    tempStr = args[1].rstrip()
    tempStr = tempStr.replace("[[","").replace("]]","")
    flds = tempStr.split("],[")
    p = set_Points(flds)
    print("p = %s" %(output_Points(p)))

    time0 = time.time()

    sl = Solution()
    print("common_node = %s" %(sl.maxPoints(p)))

    time1 = time.time()
    print("Execute time ... : %f[s]" %(time1 - time0))
    print()


if __name__ == "__main__":
    main()
