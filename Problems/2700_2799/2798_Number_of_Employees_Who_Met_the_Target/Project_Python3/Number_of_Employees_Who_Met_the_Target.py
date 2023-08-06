import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # 37ms - 42ms
        ans = 0
        for h in hours:
            if h >= target:
               ans += 1
        return ans

    def numberOfEmployeesWhoMetTarget_1liner(self, hours: List[int], target: int) -> int:
        # 48ms - 49ms
        return sum(h >= target for h in hours)

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
    str_args = temp.replace("\"","").replace("[[","").replace("]]","").rstrip()
    flds = str_args.split("],[")

    hours = [int(n) for n in flds[0].split(",")]
    target = int(flds[1])
    print("hours = {0}, target = {1:d}".format(hours, target))

    sl = Solution()
    time0 = time.time()

    result = sl.numberOfEmployeesWhoMetTarget(hours, target)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
