import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Wrong Answer 38 / 41 testcases passed
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points) - 1):
            cur = 0
            overlap = 0
            lines = {}
            for j in range(i + 1,len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == dy == 0:
                    overlap += 1
                    continue
                key = None if dx == 0 else 10.0 * dy / dx
                lines[key] = lines.get(key, 0) + 1
                cur = max(cur, lines[key])
            res = max(res, cur + overlap)
        return res + 1

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
    points = [[int(col) for col in row.split(",")] for row in flds]

    sl = Solution()

    time0 = time.time()

    result = sl.maxPoints(points)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
