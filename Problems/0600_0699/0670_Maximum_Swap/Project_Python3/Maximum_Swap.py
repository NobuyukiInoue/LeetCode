# coding: utf-8

import os
import sys
import time
import math
from typing import List, Dict, Tuple

class Solution:
    def maximumSwap(self, num: int) -> int:
        # 24ms
        if num <= 11:
            return num
        else:
            digits = [int(c) for c in str(num)]
            mins = [0]
            for i in range(1, len(digits)):
                if digits[i] < digits[mins[-1]]:
                    mins.append(i)
                else:
                    mins.append(mins[-1])

            maxs = [len(digits) - 1]
            for i in reversed(range(len(digits) -1)):
                if digits[i] > digits[maxs[-1]]:
                    maxs.append(i)
                else:
                    maxs.append(maxs[-1])
            maxs = maxs[::-1]

            for i in range(len(digits)):
                if digits[mins[i]] < digits[maxs[i]]:
                    digits[mins[i]], digits[maxs[i]] = digits[maxs[i]], digits[mins[i]]
                    break

            return int(''.join([str(d) for d in digits]))

    def maximumSwap2(self, num: int) -> int:
        # 32ms
        places = [10**i for i in range(len(str(num)))]
        return max(num + num//p%10*(q - p) + num//q%10*(p - q)
               for p in places for q in places)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()

    time0 = time.time()

    result = sl.maximumSwap(num)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
