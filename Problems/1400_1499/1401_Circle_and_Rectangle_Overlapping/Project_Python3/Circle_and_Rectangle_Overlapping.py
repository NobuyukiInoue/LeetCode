# coding: utf-8

import os
import sys
import time

class Solution:
#   def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        # 28ms
        c1 = (x2 + x1) / 2
        c2 = (y2 + y1) / 2
        v1 = abs(x_center - c1)
        v2 = abs(y_center - c2)
        h1 = (x2 - x1) / 2
        h2 = (y2 - y1) / 2
        u1 = max(0, v1 - h1)
        u2 = max(0, v2 - h2)
        return (u1 * u1 + u2 * u2 <= radius * radius)

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
    flds = temp.replace("[[","").replace("]]","").replace("\"","").replace(" ","").rstrip().split("],[")

    rec1 = []*3
    pt1 = flds[0].split(",")
    radius = int(pt1[0])
    x_center, y_center = int(pt1[1]), int(pt1[2])
    print("radius = {0:d}, x_center = {1:d}, y_center = {2:d}".format(radius, x_center, y_center))

    rec2 = []*4
    pt2 = flds[1].split(",")
    x1, y1, x2, y2 = int(pt2[0]), int(pt2[1]), int(pt2[2]), int(pt2[3])
    print("x1, y1, x2, y2 = {0:d}, {1:d}, {2:d}, {3:d}".format(x1, y1, x2, y2))

    sl = Solution()
    time0 = time.time()

    result = sl.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
