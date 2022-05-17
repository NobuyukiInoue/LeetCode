# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # 32ms - 35ms
        ans = 0
        for i, _ in enumerate(number):
            if number[i] == digit:
                ans = max(ans, int(number[:i] + number[i+1:]))
        return str(ans)

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
    flds = temp.replace(" ","").replace("\"","").replace("[","").replace("]","").rstrip().split(",")

    number, digit = flds[0], flds[1]
    print("number = {0}, digit = {1}".format(number, digit))

    sl = Solution()
    time0 = time.time()

    result = sl.removeDigit(number, digit)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
