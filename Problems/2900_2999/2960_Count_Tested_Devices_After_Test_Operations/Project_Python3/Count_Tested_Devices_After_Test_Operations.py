import functools
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        # 56ms - 57ms
        ans = 0
        for target in batteryPercentages:
            ans += target > ans
        return ans

    def countTestedDevices2(self, batteryPercentages: List[int]) -> int:
        # 52ms - 57ms
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - ans > 0:
                ans += 1
        return ans

    def countTestedDevices_1liner(self, batteryPercentages: List[int]) -> int:
        # 58ms - 59ms
        return functools.reduce(lambda sofar, v: sofar + int(v > sofar),  batteryPercentages, 0)


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
    flds = temp.replace("[","").replace("]","").replace(", ",",").rstrip()
    batteryPercentages = [int(n) for n in flds.split(",")]
    print("batteryPercentages = {0}".format(batteryPercentages))

    sl = Solution()

    time0 = time.time()

    result = sl.countTestedDevices(batteryPercentages)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
