# coding: utf-8

import collections
import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 152ms
        sorted_boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        cnt_unit, cnt_box = 0, 0
        for i, target in enumerate(sorted_boxTypes):
            if cnt_box + target[0] <= truckSize:
                cnt_unit += target[0]*target[1]
                cnt_box += target[0]
            else:
                if target[0] <= truckSize - cnt_box:
                    i = target[0]
                else:
                    i = truckSize - cnt_box
                cnt_unit += target[1]*i
                cnt_box += i
            if cnt_box == truckSize:
                break
        return cnt_unit

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
    flds = temp.replace("[[[","").replace("\"","").replace(" ","").rstrip().split("]],[")

    boxTypes  = [[int(n) for n in row.split(",")] for row in flds[0].split("],[")]
    truckSize = int(flds[1].replace("]", ""))
    print("boxTypes  = {0}".format(boxTypes))
    print("truckSize = {0:d}".format(truckSize))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumUnits(boxTypes, truckSize)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
