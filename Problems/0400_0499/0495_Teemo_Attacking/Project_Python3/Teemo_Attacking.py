# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # 236ms
        total = duration
        for i in range(len(timeSeries) - 2, -1, -1):
            diff = timeSeries[i + 1] - timeSeries[i]
            if diff > duration:
                total += duration
            else:
                total += diff
        return total

    def findPoisonedDuration2(self, timeSeries: List[int], duration: int) -> int:
        # 240ms
        total = 0
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i - 1]
            if diff > duration:
                total += duration
            else:
                total += diff
        return total + duration

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
    flds = temp.replace(" ","").replace("\"","").replace("[[","").replace("]]","").rstrip().split("],[")

    timeSeries = [int(_) for _ in flds[0].split(",")]
    duration = int(flds[1])
    print("timeSeries = {0}".format(timeSeries))
    print("duration = {0}".format(duration))

    sl = Solution()
    time0 = time.time()

    result = sl.findPoisonedDuration(timeSeries, duration)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
