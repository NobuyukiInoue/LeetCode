# coding: utf-8

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
        return maxPoints2(points, 0, 0)


    def maxPoints2(self, points, index, maxNumberOfPoints):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        
        if len(points) - index <= maxNumberOfPoints:
            return maxNumberOfPoints
        
        maxKey = 0.0
        duplicatePoints = 0

        for i in range(index, len(points)):
            if areEqual(points[i], points[index]):
                duplicatePoints += 1
            else:
                slope = getSlope(points[index], points[i])
                maxKey = incrementSlopeCount(slope, slopeToCountMap, maxKey)
             
        if incrementSlopeCount.ContainsKey(mapKey):
            maxNumberOfPoints = 0
        else:
            maxNumberOfPoints = 0

        return MaxPoints(points, index + 1, maxNumberOfPoints)


    def areEqual(self, a, b):
        return a.x == b.x and a.y == b.y


    def getSlope(self, left, right):
        dx = left.x - right.x
        dy = left.y - right.y

        slope = 0.0
        if dy != 0:
            slope = dx / dy
        
        return slope


    def incrementSlopeCount(self, slope, slopeToCountMap, maxKey):
        if slopeToCountMap.ContainsKey(slope):
            slopeToCountMap[slope] += 1
        else:
            slopeToCountMap[slope] = 1
        if not slopeToCountMap.ContainsKey(maxKey) or  slopeToCountMap[slope] >= slopeToCountMap[maxKey]:
            maxKey = slope
        
        return maxKey


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
