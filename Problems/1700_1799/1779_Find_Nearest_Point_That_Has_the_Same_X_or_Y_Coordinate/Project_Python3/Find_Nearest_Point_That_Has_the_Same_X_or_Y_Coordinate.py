import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # 724ms
        smallest, index = sys.maxsize, -1
        for i, point in enumerate(points):
            dx, dy = x - point[0], y - point[1]
            if dx * dy == 0 and abs(dx) + abs(dy) < smallest:
                smallest = abs(dx) + abs(dy)
                index = i
        return index

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
    flds = temp.replace(", ",",").replace("\"","").replace("]]]","").rstrip().split("],[[")

    flds0 = flds[0].replace("[[", "").split("],[")
    x, y = int(flds0[0]), int(flds0[1])
    print("x = {0}, y = {1}".format(x, y))

    points = [[int(data) for data in item.split(",")] for item in flds[1].split("],[")]
    print("points = {0}".format(points))

    sl = Solution()
    time0 = time.time()

    result = sl.nearestValidPoint(x, y, points)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
