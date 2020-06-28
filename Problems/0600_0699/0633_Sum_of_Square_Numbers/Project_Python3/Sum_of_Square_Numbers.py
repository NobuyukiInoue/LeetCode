# coding: utf-8

import math
import os
import sys
import time

class Solution:
#    def judgeSquareSum(self, c: int) -> bool:
    def judgeSquareSum(self, c):
        for a in range(int(math.sqrt(c / 2)) + 1):
            if math.sqrt(c - a ** 2).is_integer():
                return True
        return False

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
    flds = temp.replace("[","").replace("]","").rstrip()
    c = int(flds)

    sl = Solution()
    time0 = time.time()
    result = sl.judgeSquareSum(c)
    print("result = {0}".format(result))

    time1 = time.time()

    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
