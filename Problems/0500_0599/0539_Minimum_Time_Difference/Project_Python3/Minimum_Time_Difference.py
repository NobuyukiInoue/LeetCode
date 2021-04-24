import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 64ms
        timePointsInt = [int(t[:2])*60 + int(t[-2:]) for t in timePoints]
        sortedTime = sorted(timePointsInt)
        minimum = 1440
        for i in range(1, len(sortedTime)):
            diff = sortedTime[i] - sortedTime[i - 1]
            minimum = min(minimum, diff)
        diff = sortedTime[0] - sortedTime[-1] + 1440
        return min(minimum, diff)

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
    flds = temp.replace(", ", ",").replace("\"","").replace("[","").replace("]","").rstrip()

    timePoints = flds.split(",")
    print("timePoints = {0}".format(timePoints))

    sl = Solution()
    time0 = time.time()

    result = sl.findMinDifference(timePoints)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()