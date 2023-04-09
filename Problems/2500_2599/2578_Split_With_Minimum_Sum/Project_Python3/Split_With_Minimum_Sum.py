# coding: utf-8

import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def splitNum(self, num: int) -> int:
        # 30ms - 39ms
        s = ''.join(sorted(str(num)))
        return int(s[::2]) + int(s[1::2])

    def splitNum2(self, num: int) -> int:
        # 24ms - 37ms
        num1, num2 = [], []
        for i, ch in enumerate(sorted(str(num))):
            (num1 if i % 2 == 0 else num2).append(ch)
        return int(''.join(num1)) + int(''.join(num2))

    def splitNum3(self, num: int) -> int:
        # 24ms - 41ms
        nums = [int(ch) for ch in str(num)]
        n = len(nums)
        if n == 2:
            return sum(nums)
        nums.sort()
        s_num = "".join([str(ch) for ch in nums])
        num1, num2 = "", ""
        for i in range(n):
            if i % 2:
                num1 += s_num[i]
            else:
                num2 += s_num[i]
        return int(num1) + int(num2)

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
    num = int(flds)
    print("num = {0:d}".format(num))

    sl = Solution()

    time0 = time.time()

    result = sl.splitNum(num)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
