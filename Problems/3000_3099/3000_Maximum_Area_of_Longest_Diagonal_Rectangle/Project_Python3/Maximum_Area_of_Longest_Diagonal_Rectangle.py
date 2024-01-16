import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # 74ms - 78ms
        max_diag, max_area = 0, 0
        for rect in dimensions:
            diag = rect[0]**2 + rect[1]**2
            area = rect[0]*rect[1]
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
        return max_area

    def areaOfMaxDiagonal_2liner(self, dimensions: List[List[int]]) -> int:
        # 75ms - 82ms
        l, w = max(dimensions, key = lambda x: (x[0]*x[0]+x[1]*x[1], (x[0]*x[1])))
        return l*w


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
    flds = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    
    dimensions = [[int(col) for col in data.split(",")] for data in flds.split("],[")]
    print("dimensions = {0}".format(dimensions))

    sl = Solution()
    time0 = time.time()

    result = sl.areaOfMaxDiagonal(dimensions)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
