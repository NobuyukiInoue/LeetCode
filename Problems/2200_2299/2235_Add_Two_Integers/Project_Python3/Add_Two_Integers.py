# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # 19ms - 37ms
        return num1 + num2

    def sum2(self, num1: int, num2: int) -> int:
        # 28ms - 39ms
        if num2 >= 0:
            adder = 1
        else:
            adder, num2 = -1, -num2
        for _ in range(0, num2):
            num1 += adder
        return num1

    def sum_circuit(self, num1: int, num2: int) -> int:
        # Time Limit Exceeded
        def add(x, y) -> int:
            if y == 0:
                return x
            elif x < 0 and y < 0:
                s= ~x^~y
                c = (~x&~y)<<1
                return ~add(add(s, c), 1)
            s = x^y
            c = (x&y)<<1
            return add(s, c)
        return add(num1, num2)

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
    flds = temp.replace("[", "").replace("]", "").replace(", ", ",").rstrip()
    nums = [int(n) for n in flds.split(",")]
    num1, num2 = nums[0], nums[1]
    print("num1 = {0:d}, num2 = {1:d}".format(num1, num2))

    sl = Solution()

    time0 = time.time()

    result = sl.sum(num1, num2)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
